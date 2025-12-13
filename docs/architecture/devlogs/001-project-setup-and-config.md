#### General Context

The goal of this backlog item is to prepare the minimal infrastructure needed to run the application services and establish a reproducible development environment with containers and unified configuration. This is based on the Initial Infrastructure Design Log (DL-001).


### Task 1 — Configure Docker and Install Framework in Containers

#### Process and Decisions

1. **Initial Project Structure**  
   Two main folders were created: `store_service` and `inventory_service`, each with its own `Dockerfile` and `requirements.txt`.  
   A root-level `docker-compose.yml` file was added to orchestrate all services.

2. **Backend Framework**  
   - Initially, both services were set up with **FastAPI** to expose a simple health-check endpoint (`/`).
   - This made it possible to verify that containers built correctly, servers started, and requests were handled properly.

3. **Network and Port Configuration**  
   - Ports `8001` and `8002` were mapped for `store_service` and `inventory_service`, respectively.  
   - Both services shared Docker’s internal network, allowing name-based communication (`store_service`, `inventory_service`).

4. **Validation**  
   Running `docker-compose up --build` successfully started all containers, and each service responded on its `/` endpoint.


### Task 2 — Add DB (Postgres) and Database Container

#### Process and Decisions

1. **Database Integration**
   - Added a `db` service using the `postgres:16` image.  
   - Environment variables were externalized to a `.env.development` file:

``` bash
POSTGRES_USER=dev_user
POSTGRES_PASSWORD=dev_password
POSTGRES_DB=dev_db
```

2. **Data Persistence**
   - A named volume `db_data` was added to persist PostgreSQL data between runs.  
   - `store_service` and `inventory_service` were configured with `depends_on: db` to ensure proper startup order.

3. **Initial Validation**
   - The database container started successfully.  
   - Some warnings appeared about missing environment variables, prompting a review of how Docker interprets values from `env_file` and `environment`.


### Task 3 — Environment Variables for Ports and Credentials

#### Process and Decisions

1. **Environment Standardization**
   - Three environment files were planned:
     - `.env.development`: local, non-sensitive configuration
     - `.env.test`: used for CI/CD and testing
     - `.env.example`: reference template

2. **Using Variables in Compose**
   - A consistent pattern was established for environment variable interpolation:
     ```yaml
     environment:
       POSTGRES_USER: ${POSTGRES_USER}
       POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
       POSTGRES_DB: ${POSTGRES_DB}
     ```
   - This ensures both Docker and GitHub Actions can share the same environment configuration, locally or via repository Secrets.

3. **Local Integration Tests**
   - Verified that environment variables loaded correctly inside containers.  
   - Confirmed that both services could reach each other using container hostnames.


### Task 4 — Configure `customer_sim` tier

#### Process and Decisions

This tier is currently planned as a pure Python subproject (no API endpoints).

1. **Created main folder**  
   - `customer_sim/` with its own `Dockerfile` and `app/__init__.py`

2. **Added service** to `docker-compose.yml`

3. **Validation**  
   Running `docker compose up -d customer_sim` successfully built and started the container within the same Docker network as the other services.


### Task 5 — CI, Testing, and Linting Configuration  

#### Process and Decisions

1. **Add test folders and requirements for each tier**  
   - Added to each `requirements.txt`:  
     - `pytest`, `pytest-cov` for unit testing and coverage  
     - `httpx` for services with FastAPI endpoints  
     - `black` and `flake8` for code style and static analysis  
   - Added basic sanity tests in `tests/test_basic.py` for each service  
   - Added a root `.flake8` configuration file for consistent linting  

2. **Create workflow for tests and linting**  
   - Configured GitHub Actions workflow to:  
     - Install dependencies per service  
     - Run tests and measure coverage  
     - Run `black` and `flake8` to enforce linting rules  
   - Triggered on PRs and pushes to main-related branches  

3. **Configure GitHub Ruleset for branch protection**  
   - Enforcement status enabled  
   - Target branch: `main`  
   - Activated:  
     - Restrict deletions  
     - Require pull request before merging  
     - Require status checks to pass  
     - Require branches to be up to date before merging  
     - Require linear history  
     - Block force pushes  

4. **Validation**  
   - Rebuilt containers to ensure dependencies installed correctly. Example for `customer_sim`:
     `docker compose build customer_sim`
   - Verified local execution of linters inside containers. Example for store_service:
     ``` bash
     docker compose run --rm store_service black .
     docker compose run --rm store_service flake8 .
     ```
   - Confirmed workflow triggers automatically and blocks merges until CI passes  


### Task 6 — Environment Variable Strategy for CI (Dummy Values vs. Secrets)

#### Process and Decisions

During the initial CI setup, the workflow attempted to inject environment variables into the Postgres service using GitHub Secrets:

``` yaml
env:
  POSTGRES_USER: ${{ secrets.POSTGRES_USER }}
  POSTGRES_PASSWORD: ${{ secrets.POSTGRES_PASSWORD }}
  POSTGRES_DB: ${{ secrets.POSTGRES_DB }}
```

This caused two major issues:

1. **GitHub Actions cannot interpolate secrets inside service-level environment definitions**  
    The `services:` block (specifically for Docker containers like Postgres) runs before steps, and secrets are not available at that lifecycle stage.  
    As a result, Postgres containers were failing during initialization with errors related to environment variables not being set.
    
2. **GitGuardian flagged the push whenever realistic-looking literals were used**  
    When switching away from secrets and using values such as:

```
POSTGRES_USER: postgres
POSTGRES_PASSWORD: postgres
POSTGRES_DB: control_stock_test
```

3. GitGuardian detected them as potential leaked credentials and blocked the PR.  
    Even though they were not sensitive, their patterns resembled real credentials.

#### Solution: Use Clearly Dummy Literal Values for CI

To satisfy all constraints (GitHub Actions limitations, GitGuardian scanning, and workflow reliability), the project adopted **explicit dummy values** for CI:

```
POSTGRES_USER: test_user
POSTGRES_PASSWORD: test_password_1234
POSTGRES_DB: test_db
```

These values:
- Are not sensitive
- Are clearly fake, so GitGuardian does not flag them
- Do not require GitHub Secrets for the test pipeline
- Allow Postgres to boot correctly inside GitHub Actions
- Are sufficient for all test runs (since CI uses disposable containers)

#### Scope Clarification

- These dummy literals are used **only in `.github/workflows/tests.yml`**, which runs in CI and does not touch production.

- Local development continues using `.env.development`.

- Future production deployments will rely on **real secrets injected at the infrastructure level**, not the repository.

#### Validation

After changing to literal dummy values, the CI pipeline successfully:
- Initialized the Postgres service
- Installed dependencies
- Executed the test suites
- Ran linting checks
- Reported coverage cleanly

This resolved the environment-variable instability that previously caused continuous workflow failures.


### Issue — Workflow push blocked by GitHub security

#### Context
While pushing the branch `config/test-config`, the following Git error occurred:

```
 ! [remote rejected] config/test-config -> config/test-config (refusing to allow a Personal Access Token to create or update workflow `.github/workflows/tests.yml` without `workflow` scope)
error: failed to push some refs to 'https://github.com/nureddyn/demand-supply-sim.git'
```

GitHub rejected the push because the branch included changes to `.github/workflows/tests.yml`, and the local Git client was authenticating using a **Personal Access Token (PAT)** *without* the required `workflow` scope.

GitHub enforces this restriction to prevent workflow injection attacks (e.g., PRs or pushes that could upload malicious CI pipelines).

#### Root Cause
Local Git was using an outdated or insufficiently scoped **PAT (Personal Access Token)** stored in the system credential manager.  
The token lacked the `workflow` permission, which GitHub **requires** for any push that modifies workflow files.

#### Resolution
Authentication was switched from the insecure PAT to **GitHub CLI**, which automatically provisions a token with the correct permissions.

Steps:
1. Run: `gh auth login`
2. Authenticate via browser.
3. Re-push the branch: `git push origin config/test-config`

Push completed successfully afterward.
###### Notes
- This behavior is expected and is part of GitHub’s security model for CI/CD.
- Using `gh auth login` is preferred for development environments because it ensures tokens include appropriate permissions for workflow management.


### Task 7 — Dockerfile Fixes, Volume Configuration, and Makefile Automation

#### Process and Decisions

1. **Fix Dockerfile structure for all services**
    Each service (`store_service`, `inventory_service`, `customer_sim`) had its `Dockerfile` corrected to follow best practices:
    
    - Ensure dependency installation is cached efficiently:
        `COPY requirements.txt . RUN pip install --no-cache-dir -r requirements.txt`
    
    - Move `COPY . .` to the end so the container does not overwrite live-mounted code.
    
    - Remove duplicated or incorrectly ordered COPY blocks.
    
    - Unify structure across all services for maintainability.
    
    These changes ensure:
    - Faster rebuilds
    - Proper local hot-reload behavior
    - Avoiding issues where container code replaced local changes

2. **Fix volume mounts in `docker-compose.yml`**
    The original mounting pattern: `- ./customer_sim/app:/app` caused desynchronization between local and container directories.
    
    Updated to mount the entire project directory:
    
    `- ./customer_sim:/app`
    
    Same adjustment was applied to `inventory_service` and `store_service`.
    
    Additionally, the Compose file required an explicit named volume declaration:
    `volumes:   db_data:`
    
    These changes resolved issues with:
    - Linters running inside containers not modifying local files
    - Code reloading inconsistencies
    - Database persistence warnings

3. **Introduce a Makefile for unified developer workflow**  
    A new `Makefile` was added to streamline linting and testing:
    
    - **`make check`** now runs:
        - Black formatting check
        - Flake8 static analysis
        - Tests (with coverage) for all three services
    
    This allows:
    - Consistent local reproduction of CI behavior
    - A single entry point for developers
    - Reduced friction for common tasks

4. **Validation**  
    After integrating the updated Dockerfiles, corrected volumes, and the Makefile:
    - Running `make check` executed all linters and tests successfully.
    - Verified that local editing + mounted volumes now behave predictably.
    - Confirmed consistent behavior between local Docker environment and GitHub Actions workflow.

###### Notes
- These adjustments align the project with realistic development workflows used in small software teams.

- The updated structure simplifies onboarding, reduces configuration drift, and guarantees reproducible builds across machines.


### Issue — Workflow push blocked by test coverage job

#### Process and Decisions

- Check Coverage locally:
```
docker compose run --rm store_service pytest --cov=app
docker compose run --rm store_service pytest --cov=app --cov-report=term-missing

```

- Add health test for at least a module in ``/app`` (for each service)
- Check locally if coverage is solved
- commit and push


### Issue — Health test coverage blocked by module import errors

#### Context

The initial goal for this task was:

- Add a health-check test for at least one module in each service's `/app` folder
- Verify locally that test coverage reports correctly
- Commit and push

However, while running `pytest` both locally inside Docker containers and in the GitHub Actions workflow, tests failed with import errors:

```
ImportError while importing test module 'tests/test_healthcheck.py'  
ModuleNotFoundError: No module named 'app'
```

This prevented coverage reporting and blocked progress on the health-check tests.

#### Root Cause

- Python did not include the service root directories in the module search path (`PYTHONPATH`) during test execution.
- Inside the containers, even though `working_dir` was set to `/app`, `pytest` did not automatically treat it as a package root.  
- In the GitHub Actions workflow, the default checkout location also did not align with the expected Python module paths.

#### Resolution

1. Created a `pytest.ini` file at the root of each service:
``` ini
[pytest]
pythonpath = .
```

2. Verified that `docker-compose.yml` mounts the full service folder and sets the working directory:
- `store_service`:
``` yaml
working_dir: /app
volumes:
  - ./store_service:/app
```
- `inventory_service`:
``` yaml
working_dir: /app
volumes:
  - ./inventory_service:/app
```
- `customer_sim`:
``` yaml
working_dir: /app
volumes:
  - ./customer_sim:/app
```

3. Ran tests locally inside containers to confirm:
``` bash
docker compose run --rm store_service pytest --cov=app --cov-report=term-missing
```

4. Verified that GitHub Actions workflow tests now run successfully, allowing coverage reporting to proceed.

###### Notes
- This change aligns local development and CI environments regarding Python module search paths.
- Health-check tests for each service can now execute, and coverage can be measured accurately.


### Branch Protection Check Hanging Issue

#### What happened

A branch protection rule on `main` required a specific status check to pass before allowing merges. However, the required check name configured in the rule **did not match** the actual name of the check produced by the workflow defined in `.github/workflows/tests.yml`.

Because of this mismatch:

- GitHub was waiting for a check that **never ran**, since no workflow was producing a check with that name.
- Even though the workflow executed successfully, the PR remained stuck in _“Waiting for status to be reported”_.

In other words, the rule expected **Check A**, while the workflow produced **Check B**, so the validation never completed.

#### What was done to fix it

1. Identified that the branch protection rule referenced a status check name that did not correspond to the workflow’s real job name.

2. Updated the workflow to also run on `push` to `main` so GitHub could surface the **actual check name** generated by the workflow.

3. Once the workflow ran on `main`, the correct status check appeared in the branch protection settings.

4. Re-enabled _Require status checks to pass_ and selected the **proper check name**.

5. With the correct mapping in place, PRs started validating normally.

#### Outcome

- The status check is now correctly registered under the branch protection rule.
- PRs no longer hang.
- The workflow and protection rule are in sync, restoring a clean merge flow.


### Task — Clean Up Environment Variable Strategy in `docker-compose.yml`

#### Process and Changes

The project previously duplicated database environment variables inside the `db` service of `docker-compose.yml`, mixing both:

- `.env.development` via `env_file`, and  
- Hard-coded literals inside `environment:`.

To simplify the configuration and ensure that local development relies strictly on `.env.development`, the hard-coded environment variables were removed from the `environment:` block. Now the Postgres container uses only the values defined in `.env.development`.

After applying the change, the service was validated by:

- Connecting to the running Postgres container  
  ```bash
  docker exec -it demand-supply-sim-db-1 psql -U dev_user -d dev_db -c "SELECT 1;"
  ```

which returned the expected result `(1)`.

- Verifying the database is reachable and running:
``` bash
docker exec -it demand-supply-sim-db-1 psql -U dev_user -d dev_db -c "\dt"
```

returning an empty table list (correct for a fresh database).

#### Result

- Local environment now depends solely on `.env.development`.

- No impact on CI: the GitHub Actions pipeline still uses its own dummy literals (``test_user``, ``test_password_1234``, ``test_db``), ensuring isolation between local dev and CI.

- Configuration is cleaner, more maintainable, and aligned with best practices.

