
import requests
from requests.auth import HTTPBasicAuth
import sys

url = 'http://10.180.20.60:3000/rpc'
headers = { 'content-type' : 'application/xml' }
payload = "<lock-configuration/><load-configuration><configuration><system><host-name>"+str(sys.argv[1])+"</host-name></system></configuration></load-configuration><commit/><unlock-configuration/>"
q = requests.post(url, headers=headers, auth=('msmihula', 'juniper123'), data=payload)

print '\nChange Hostname to passed paramter: ' + str(sys.argv)
print q.text