# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: iostancu <iostancu@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/07/28 19:11:33 by iostancu          #+#    #+#              #
#    Updated: 2022/08/02 00:07:00 by iostancu         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

LILA	=\033[1;36m
BLUE	=\033[1;34m
GREEN	=\033[2;32m
YELLOW	=\033[1;33m
END		=\033[1;37m

DOCKER_PATH = ./docker/build/Dockerfile

APPNAME = docker_otp:latest
CONTAINER = otp_container
COMPOSE	= ./docker/docker-compose.yml
COMP_CMD = docker-compose ps -a 



all:	up	exec

list:
	@echo "${LILA}Current compose running containers:"
	@echo "------------------------------"
	@docker-compose -f $(COMPOSE) ps -a
	@echo "------------------------------"
	@echo "${BLUE}Current compose images:"
	@echo "----------------------------------------------"
	@docker-compose -f $(COMPOSE) images
	@echo "${GREEN}Running containers: ${END}"
	@docker ps -a
	@echo "${GREEN}Existing docker images: ${END}"
	@docker images 
	

up:
	docker-compose -f $(COMPOSE) up -d

build:
	docker build -f $(DOCKER_PATH) . -t $(APPNAME)

down:
	docker-compose -f $(COMPOSE) down

delete: down
	docker rm -fv $(CONTAINER)
	docker rmi -f $(DOCKER_PATH) $(APPNAME)

exec:
	docker exec -it ${CONTAINER} /bin/sh -c bash

help:
	@echo "${LILA}GENERAL COMMANDS:\033[2;37m"
	@echo "[make] executes 'up' and 'exec' builds main image, and run a container with compose and execute it with bash"
	@echo "[up] builds images and run containers"
	@echo "[exec] execute container with bash"
	@echo "[list] shows images and all containers with compose"
	@echo "[delete] stops and deletes containers and images"
	@echo "[build] rebuilds the image"