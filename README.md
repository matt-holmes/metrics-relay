# Metrics Relay

## Assumptions
This is being setup on an AWS EC2 instance running Ubuntu 18.04

## Setup
### Inside your Linux Shell

#### Install psutil library (https://psutil.readthedocs.io/en/latest/):
1. `$:sudo apt update`
2. `$:sudo apt-get install python3-pip`
3. `$:pip3 install psutil`

#### Inside your home dir
1. Make a new directory called `metrics` 
2. Add the metrics_relay.py file.
3. Create a new https://postb.in/ endpoint.
4. update metrics_relay.py with new URL.

#### Setup your crontab
1. `$:crontab -e`
2. Add to the bottom of file  `* * * * * /usr/bin/python3.7 /home/ubuntu/metrics/metrics_relay.py` and save it.
