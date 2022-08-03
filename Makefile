# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: iostancu <iostancu@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/07/28 19:11:33 by iostancu          #+#    #+#              #
#    Updated: 2022/08/02 21:03:30 by iostancu         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

CYAN	=\033[1;36m
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
	@echo "${CYAN}Current compose running containers:"
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
#Check why delete cause error 

exec:
	docker exec -it ${CONTAINER} /bin/sh -c bash

help:
	@echo ""
	@echo "${BLUE}GENERAL COMMANDS:\033[2;37m"
	@echo "\t[ list ] \tShows images and all containers with compose."
	@echo "\t[ make ] \tExecutes 'up' and 'exec'."
	@echo "\t[ up ] \t\tBuilds images and run containers."
	@echo "\t[ exec ] \tExecutes container with bash."
	@echo "\t[ delete ] \tStop and delete containers and images."
	@echo "\t[ build ] \tBuild the image."
	@echo ""
	@echo "\tA normal workflow would be: [ make build ] + [ make ] "
	@echo ""
	@echo "\tThen you can [ make list ] to se all existing images and containers and"
	@echo "\tto delete the images and containers related, execute [ make delete ] "