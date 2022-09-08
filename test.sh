#!/bin/bash
declare -a directories=("front-end" "fruit" "friend" "characters")
sudo apt-get update
sudo apt-get -y install python3 python3-pip python3-venv
python3 -m venv venv
source venv/bin/activate
pip3 install -r test_requirements.txt
for dir in "${directories[@]}"
do
  cd ${dir}
  pwd
  python3 -m pytest --cov=application 
  pwd
  cd ..
done