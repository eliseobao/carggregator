DOCKER_IMAGE_NAME=carggregator-image
DEV_IMAGE_NAME=${DOCKER_IMAGE_NAME}:dev

build:
	DOCKER_BUILDKIT=1 docker build \
		--build-arg USER_NAME=user \
		--build-arg USER_UID=$(shell id -u) \
		--build-arg USER_GID=$(shell id -g)  \
		-f devops/dev/Dockerfile \
		-t ${DEV_IMAGE_NAME} .

shell:
	docker run -it --rm \
		-v $(shell pwd)/src:/app \
		--entrypoint /bin/bash \
		${DEV_IMAGE_NAME}

black:
	docker run -it --rm \
		-v $(shell pwd)/src:/app \
		${DEV_IMAGE_NAME} black /app

up:
	(cd devops/dev/ && docker compose up -d)

down:
	(cd devops/dev/ && docker compose down -v)

crawl-motor.es:
	docker run -it --rm \
		-v $(shell pwd)/src:/app \
		${DEV_IMAGE_NAME} scrapy crawl motor.es
