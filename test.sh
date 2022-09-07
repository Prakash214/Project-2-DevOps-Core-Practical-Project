#!/bin/bash
declare -a directories=("front-end" "name-api" "unit-api" "effect-api")
for dir in "${directories[@]}"
do
  cd ${dir}
  sudo apt-get update
  sudo apt-get install python3 python3-pip python3-venv
  python3 -m venv venv
  source venv/bin/activate
  pip3 install -r test_requirements.txt
  python3 -m pytest --cov=application --cov-report=html
  deactivate
  cd ..
done
