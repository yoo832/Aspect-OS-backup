#And you know, we surely CAN NOT run .py file in html. It's impossible until someone can
#prove that I'm totally wrong and it's rarely happens. Gonna fix it!
#with this file we can check the current users in aspectos, we will use this later when 1.0 is finished
import requests
import time

def online(projectid):
  users = []
  projectID = projectid
  url =f'https://clouddata.scratch.mit.edu/logs?projectid={projectID}&limit=40&offset=0'
  response = requests.get(url)
  cloudmonitor = response.json()
  online = False
  for i in cloudmonitor:
    ts = int(f'{round(time.time())}000') - 50000
    timestamp = i["timestamp"]
    if timestamp > ts:
      online = True
      users.append(i['user'])
  users = list(set(users))
  users = str(users)
  if online:
    return({'status':'online', 'users':users})
  else:
    return({'status':'offline', 'users':users})

while True:
  a = '539057425' #I don't know the project id of aspectos can someone put it here (GOT IT!! Or.... at lest the beta. Your welcome :)  
  print("The project is " + online(a)['status'] + ' and the users are: ' + online(a)['users'])