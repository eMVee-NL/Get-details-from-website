#!/bin/bash
# change the version number to the latest version which is available on: https://github.com/mozilla/geckodriver/releases
export GECKO_DRIVER_VERSION='v0.29.0'
wget https://github.com/mozilla/geckodriver/releases/download/$GECKO_DRIVER_VERSION/geckodriver-$GECKO_DRIVER_VERSION-linux64.tar.gz
tar -xvzf geckodriver-$GECKO_DRIVER_VERSION-linux64.tar.gz
rm geckodriver-$GECKO_DRIVER_VERSION-linux64.tar.gz
chmod +x geckodriver
sudo cp geckodriver /usr/local/bin/
echo 'copied geckodriver to /usr/local/bin/'