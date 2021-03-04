import requests
import json

username = 'vasilesafon'
token = '26b96f871c359f5aa2bd29186aaba80749bb2cb3'
friends_username = 'ennauata'

response = requests.get(f"https://api.github.com/users/{friends_username}/repos",
                        auth=(username, token))

response = json.loads(response.text)

with open('lesson-1_task-1.json', 'w') as write_file:
    json.dump(response, write_file)
