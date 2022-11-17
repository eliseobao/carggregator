DOCKER_IMAGE_NAME=carggregator-image
IMAGE_NAME=${DOCKER_IMAGE_NAME}:dev

build:
	DOCKER_BUILDKIT=1 docker build \
		--build-arg USER_NAME=user \
		--build-arg USER_UID=$(shell id -u) \
		--build-arg USER_GID=$(shell id -g)  \
		-f devops/Dockerfile \
		-t ${IMAGE_NAME} .

shell: build
	docker run -it --rm \
		-v $(shell pwd)/src:/app \
		--entrypoint /bin/bash \
		--network host \
		${IMAGE_NAME}

black: build
	docker run -it --rm \
		-v $(shell pwd)/src:/app \
		${IMAGE_NAME} black /app

up: build
	(cd devops && docker compose up -d)

up/minimal: build
	(cd devops && docker compose up -d elasticsearch)

down:
	(cd devops && docker compose down)

down/delete:
	(cd devops && docker compose down -v)

# Default value for CLOSESPIDER_ITEMCOUNT
items=0
DATE=$(LOGPATH)$(shell date).json

crawl-motor.es:
	docker run -it --rm \
		--network host \
		-v $(shell pwd):/app \
		${IMAGE_NAME} bash -c 'cd src && scrapy crawl motor.es \
			-s CLOSESPIDER_ITEMCOUNT=$(items) \
			-o ../crawling_results/motor_es/$(LOGPATH)$(shell  date +%Y_%m_%d__%H_%M_%S).json'

crawl-autoscout24:
	docker run -it --rm \
		--network host \
		-v $(shell pwd):/app \
		${IMAGE_NAME} bash -c 'cd src && scrapy crawl autoscout24 \
			-s CLOSESPIDER_ITEMCOUNT=$(items) \
			-o ../crawling_results/autoscout24/$(LOGPATH)$(shell  date +%Y_%m_%d__%H_%M_%S).json'

crawl-autocasion:
	docker run -it --rm \
		--network host \
		-v $(shell pwd):/app \
		${IMAGE_NAME} bash -c 'cd src && scrapy crawl autocasion \
			-s CLOSESPIDER_ITEMCOUNT=$(items) \
			-o ../crawling_results/autocasion/$(LOGPATH)$(shell  date +%Y_%m_%d__%H_%M_%S).json'

crawl-all: crawl-motor.es crawl-autoscout24 crawl-autocasion

demo:
	devops/demo_script.sh

update:
	git submodule update --init --recursive
