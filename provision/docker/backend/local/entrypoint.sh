#!/usr/bin/env bash

poetry install
echo $(poetry env info --path)
source $(poetry env info --path)/bin/activate

while :
do
    if  nc -z ${VAW_DATABASE_HOST} 5432
    then
        sleep 1
        if  nc -z ${VAW_DATABASE_HOST} 5432
        then
            break
        fi
    fi
    echo "Database not up, sleeping for 5 seconds."
    sleep 5
done

python manage.py migrate
python manage.py create_superuser --no-input

exec ${@}
