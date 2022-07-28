# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: iostancu <iostancu@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/07/28 19:11:33 by iostancu          #+#    #+#              #
#    Updated: 2022/07/28 23:05:15 by iostancu         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

BLUE	=\033[0;35m
GREEN	=\033[0;36m
YELLOW	=\033[0;33m

DOCKER_PATH = ./docker/build/Dockerfile

APPNAME = docker_otp:latest
CONTAINER = otp_container
COMPOSE	= ./docker/docker-compose.yml
COMP_CMD = docker-compose ps -a 

ARG := yes

all:	up	exec

list:
	@echo "${GREEN}All containers:"
	@echo "------------------------------"
	@docker-compose -f $(COMPOSE) ps -a
	@echo "${YELLOW}Existing images:"
	@echo "----------------------------------------------"
	@docker-compose -f $(COMPOSE) images
	@echo "${GREEN}"
	docker images
	@echo "${GREEN}"
	docker ps -a

begin:
      if [ "$(TEST)" = "ON" ]; then echo "PASSED"; else echo "FAILED"; fi

up:
	docker-compose -f $(COMPOSE) up -d

build:
	docker build -f $(DOCKER_PATH) . -t $(APPNAME)

down:
	docker-compose -f $(COMPOSE) down

delete:
	ifeq ($(ARGS),$(ARG))
		docker rm -fv $(CONTAINER)
	endif
exec:
	docker exec -it ${CONTAINER} /bin/sh -c bash

help:
	@echo "${BLUE}GENERAL COMMANDS:\033[2;37m"
	@echo "[make] executes 'up' and 'exec' builds main image, and run a container with compose and execute it with bash"
	@echo "[up] builds images and run containers"
	@echo "[exec] execute container with bash"
	@echo "[list] shows images and all containers with compose"
	@echo "[down] stops containers and delete them and the images too"
	@echo "[build] rebuilds the image"