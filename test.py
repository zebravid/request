

import requests
session=requests.Session()
params={'username':'stasbasko@gmail.com','password':'123456'}
s=session.post('http://wise.shottyapp.com/',data=params)
#print(s.cookies.get_dict())
#print(s.text)

r=requests.get('https://wise.shottyapp.com/#/project/VISA_FIFA/shots')
print(r.text)