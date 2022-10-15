DOCKER_IMAGE_NAME=carggregator-image
IMAGE_NAME=${DOCKER_IMAGE_NAME}:dev

build:
	DOCKER_BUILDKIT=1 docker build \
		--build-arg USER_NAME=user \
		--build-arg USER_UID=$(shell id -u) \
		--build-arg USER_GID=$(shell id -g)  \
		-f devops/Dockerfile \
		-t ${IMAGE_NAME} .

shell:
	docker run -it --rm \
		-v $(shell pwd)/src:/app \
		--entrypoint /bin/bash \
		--network host \
		${IMAGE_NAME}

black:
	docker run -it --rm \
		-v $(shell pwd)/src:/app \
		${IMAGE_NAME} black /app

up:
	(cd devops && docker compose up -d)

down:
	(cd devops && docker compose down -v)

crawl-motor.es:
	docker run -it --rm \
		--network host \
		-v $(shell pwd)/src:/app \
		${IMAGE_NAME} scrapy crawl motor.es

crawl-flexicar:
	docker run -it --rm \
		--network host \
		-v $(shell pwd)/src:/app \
		${IMAGE_NAME} scrapy crawl flexicar
