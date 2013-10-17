#!/bin/py

try:
	import requests
except:
	raise Exception('no module named requests')

# my gist on gist.github.com,  that contains all the commands data
r = requests.get('https://api.github.com/gists/xxxxxxxxxxxxxxxxxxx')
t = r.json()['files']['R-terminal']['content']
t = str(t)

# adding gist-data to a new file data.rt
f = open('data.rt', 'w')
f.write(t)
f.close()

echo 'created a new data.rt file'

