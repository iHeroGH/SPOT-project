pip install virtualenv
python -m virtualenv --python=python spot_env
source spot_env/bin/activate

python -m pip install --upgrade bosdyn-client bosdyn-mission bosdyn-choreography-client

pip list --format=columns | findstr bosdyn

ping 192.168.80.3
