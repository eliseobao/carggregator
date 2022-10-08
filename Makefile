DOCKER_IMAGE_NAME=carggregator-image
DEV_IMAGE_NAME=${DOCKER_IMAGE_NAME}:dev
PROD_IMAGE_NAME=${DOCKER_IMAGE_NAME}:0.0.1

# -------------------- Development -----------------------
dev/build:
	DOCKER_BUILDKIT=1 docker build \
		--build-arg USER_NAME=user \
		--build-arg USER_UID=$(shell id -u) \
		--build-arg USER_GID=$(shell id -g)  \
		-f devops/dev/Dockerfile \
		-t ${DEV_IMAGE_NAME} .

dev/shell:
	docker run -it --rm \
		-v $(shell pwd)/src:/app \
		--entrypoint /bin/bash \
		${DEV_IMAGE_NAME}

dev/up:
	(cd devops/dev/ && docker compose up -d)

dev/down:
	(cd devops/dev/ && docker compose down -v)

dev/crawl-motor.es:
	docker run -it --rm \
		-v $(shell pwd)/src:/app \
		${DEV_IMAGE_NAME} scrapy crawl motor.es
black:
	docker run -it --rm \
		-v $(shell pwd)/src:/app \
		${DEV_IMAGE_NAME} black /app

# -------------------- Production -----------------------
prod/build:
	DOCKER_BUILDKIT=1 docker build \
		-f devops/prod/Dockerfile \
	    -t ${PROD_IMAGE_NAME} .

prod/run:
	docker run -it --rm ${PROD_IMAGE_NAME}