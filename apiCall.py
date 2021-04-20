import requests
import json
import base64
import sys

username = "admin"
password = "manish@123"
templateid = sys.argv[1]
base64string = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')

url = 'http://localhost/api/v2/job_templates/'+templateid+'/launch/'

headers = {
  'Authorization': "Basic " + base64string,
  'Content-Type': 'application/json'
}
data = {
    "extra_vars": {
        "swap_file_size_mb": "512",
        "swap_file_state": "present"
      }
}

response = requests.post(url, headers=headers, data=json.dumps(data))

print(response.text)
