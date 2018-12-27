#!/bin/bash

# Makes nescessary database migrations and runs the server
chmod 700 dbsetup.sh
python manage.py makemigrations snippets
python manage.py migrate 
python population_script.py