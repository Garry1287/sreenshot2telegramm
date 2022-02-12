#!/bin/bash
source /home/garry/ENVS/selenium-env/bin/activate
/usr/bin/python3 /home/garry/py/screenshot.py
deactivate


0 8,12,16,20 * * * /bin/bash /home/garry/bin/screenshot.sh

