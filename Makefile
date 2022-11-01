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

up/minimal:
	(cd devops && docker compose up -d elasticsearch)

down:
	(cd devops && docker compose down -v)

# Default value for CLOSESPIDER_ITEMCOUNT
items=0

crawl-motor.es:
	docker run -it --rm \
		--network host \
		-v $(shell pwd)/src:/app \
		${IMAGE_NAME} scrapy crawl motor.es -s CLOSESPIDER_ITEMCOUNT=$(items)

crawl-autoscout24:
	docker run -it --rm \
		--network host \
		-v $(shell pwd)/src:/app \
		${IMAGE_NAME} scrapy crawl autoscout24 -s CLOSESPIDER_ITEMCOUNT=$(items)

crawl-autocasion:
	docker run -it --rm \
		--network host \
		-v $(shell pwd)/src:/app \
		${IMAGE_NAME} scrapy crawl autocasion -s CLOSESPIDER_ITEMCOUNT=$(items)

crawl-all: crawl-motor.es crawl-autoscout24 crawl-autocasion

update:
	git submodule update --init --recursive
