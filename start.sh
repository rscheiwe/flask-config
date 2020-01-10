#!/bin/bash
app="ihp-api"
docker build -t ${app} .
docker run -d -p 2222:80 \
  --name=${app} \
  -v $PWD:/app ${app}