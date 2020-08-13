import psutil
import requests
import logging
from datetime import datetime

def post_metrics():
	try:
		url = 'https://postb.in/1597283023263-9918144012335'
		data = get_metrics()

		response = requests.post(url, json=data)

		if response.status_code != 200:
			logging.error(f'Failure to POST data: {data} response: {response}')

		return True

	except:
		logging.exception('')

		return False



'''
https://psutil.readthedocs.io/en/latest/

Why do we use interval=1 in the cpu_percent function?

When cpu_percent interval is 0.0 or None compares system CPU times elapsed since
last call or module import, returning immediately. That means the first
time this is called it will return a meaningless 0.0 value which you
are supposed to ignore. In this case it is recommended for accuracy
that this function be called with at least 0.1 seconds between calls.

'''

def get_metrics():
	return {
		'cpu_percent_used': psutil.cpu_percent(interval=1),
		'memory_percent_used': psutil.virtual_memory().percent,
		'disk_percent_used': psutil.disk_usage('/').percent
	}


filename = '/home/ubuntu/metrics/' + datetime.now().strftime("%m-%d-%Y")+'.log'
logging.basicConfig(level=logging.ERROR, filename=filename)


post_metrics()
