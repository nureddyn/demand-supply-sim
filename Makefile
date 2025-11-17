# Lint all services using docker compose
lint:
	docker compose run --rm store_service flake8 .
	docker compose run --rm inventory_service flake8 .
	docker compose run --rm customer_sim flake8 .

# Format all services using black
format:
	docker compose run --rm store_service black .
	docker compose run --rm inventory_service black .
	docker compose run --rm customer_sim black .

# Format + lint together
check:
	make format
	make lint

