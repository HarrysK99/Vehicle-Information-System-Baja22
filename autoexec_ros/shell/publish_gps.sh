#!/bin/sh

cd $2
exec rosrun driver_system ex_publish_gps.py

# echo "publish_gps testing"