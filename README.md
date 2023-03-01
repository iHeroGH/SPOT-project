## Set up

pip install virtualenv
python -m virtualenv --python=python spot_env
source spot_env/bin/activate

python -m pip install --upgrade bosdyn-client bosdyn-mission bosdyn-choreography-client

pip list --format=columns | findstr bosdyn

ping 192.168.80.3

## Turning on SPOT
Holding down button on left, then press button on right

## Controller
1. Turn on controller (middle button)
2. Either log on to regular account or admin account 

## Finding Wifi password to connect to SPOT
Go to admin console (must be in admin account)

## Undocking SPOT
1. Press stand on controller and move it out of docking station

## Docking SPOT
1. Press '+' button on controller
2. Have SPOT's back-side facing the QR code on the docking station
3. Press 'dock' on the controller

## WASD Example
1. Connect computer to SPOT wifi
2. Go to python/examples/wasd directory in the SDK
3. Type 'python wasd.py 192.168.80.3' in the terminal
4. Press 'space' first to turn off ESTOP and 'tab' to terminate
