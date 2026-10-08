# Lint all services using flake8
lint:
	docker compose run --rm store_service flake8 .
	docker compose run --rm inventory_service flake8 .
	docker compose run --rm customer_sim flake8 .

# Format all services using black
format:
	docker compose run --rm store_service black .
	docker compose run --rm inventory_service black .
	docker compose run --rm customer_sim black .

# Run all tests using pytest
test:
	docker compose run --rm store_service pytest .
	docker compose run --rm inventory_service pytest .
	docker compose run --rm customer_sim pytest .

# Format + lint together
check:
	make format
	make lint

