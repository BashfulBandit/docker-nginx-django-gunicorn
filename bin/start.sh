#!/usr/bin/env bash

if [ ! -e README.md ]; then
	echo "You appear to be in the wrong directory for this script."
	exit 1
else
	PROJECT_DIR=$( pwd )
fi

COMPOSE_FILE="docker-compose.yml"

echo "Going to use: ${COMPOSE_FILE} for docker-compose"

touch ${PROJECT_DIR}/nginx/logs/{access.log,error.log}

echo "Starting the docker-compose stack..."
docker-compose \
	-f ${COMPOSE_FILE} \
	up -d

echo "Waiting a few seconds for both Django and DB to settle..."
sleep 10s

exit 0
