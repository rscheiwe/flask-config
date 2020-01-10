#!/bin/bash
app="insight-api"
docker build -t ${app} .
docker run -d -p 2223:80 \
  --name=${app} \
  -v $PWD:/app ${app}