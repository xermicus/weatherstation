#!/bin/bash
set -eo pipefail

TARGET_FILE="/usr/bin/probe.py"
SERVICE_FILE="/etc/systemd/system/probe.service"

if [ "$1" == "uninstall" ] || [ "$1" == "-u" ] ; then
	echo "Removing systemd service"
	sudo systemctl stop probe.service
	sudo systemctl disable probe.service
	sudo rm $SERVICE_FILE

	echo "Removing $TARGET_FILE"
	sudo rm $TARGET_FILE
	exit 0
fi

echo "Installing into $TARGET_FILE"
sudo cp probe.py $TARGET_FILE
sudo chmod 755 $TARGET_FILE

echo "Installing systemd service"
sudo cp probe.service $SERVICE_FILE
sudo systemctl daemon-reload
sudo systemctl enable probe.service
echo "Starting systemd service"
sudo systemctl start probe.service

