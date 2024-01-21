import requests
import json

responce = requests.get('https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow')

for data in responce.json()['items']:
    if data['answer_count'] == 0:
        print(data['title'])
        print(data['link'])
        print()
    else:
        print('skipped')
    print()