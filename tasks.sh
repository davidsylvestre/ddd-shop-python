#!/bin/bash

activate() {
    source $HOME/.virtualenvs/ddd-shop-python/bin/activate
}

run() {
    activate
    ./manage.py runserver 0.0.0.0:8000
}

tests()
{
    activate
    py.test
}

setup()
{
  activate
  bundle install
  pip install -r requirements.txt
}

public=(setup tests run)

if [[ "${public[@]}" =~ "$1" ]]; then
    eval $1
else
    echo "${public[@]}"
fi
