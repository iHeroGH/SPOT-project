## Setting up Virtual Environment

pip install virtualenv
python -m virtualenv --python=<path_to_python=python> <environment_name=spot_env>

## Entering Virtual Environment
source spot_env/bin/activate
(.\spot_env\Scripts\activate on Windows)

## Setting up Boston Dynamics libraries
python -m pip install --upgrade bosdyn-client bosdyn-mission bosdyn-choreography-client
pip list --format=columns | findstr bosdyn

## Checking connection to SPOT
ping 192.168.80.3

## Turning on SPOT
Holding down button on left (blue - power button), then press button on right (red - motor control)

## Using the Controller
1. Turn on controller (middle button on the top)
2. Log on to admin account

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

## Labeling Images
1. Open Terminal
2. Connect to the virtual environment
3. `python -m pip install labelImg` (if you have not yet - must not be on python3.10)
4. Run `labelImg`
