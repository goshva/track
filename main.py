import requests
from requests.exceptions import HTTPError
import os
import time

from dotenv import load_dotenv
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


API_KEY =   os.environ.get("API_KEY")  
URL = 'https://routing.api.2gis.com/logistics/vrp/1.1.0/create?key='


headers = {
    'Content-Type': 'application/json',
}

params = {
    'key': API_KEY,
    'version': '2.0',
}

json_data = {
  "agents": [
    {
      "agent_id": 0,
      "start_waypoint_id": 0
    },

  ],
  "waypoints": [
    {
      "waypoint_id": 0,
      "point": {
            'lat': 43.91589,
            'lon': 42.71662,
      }
    },
    {
      "waypoint_id": 1,
      "point": {
            'lat': 43.90552,
            'lon': 42.71654,
      }
    },
    {
      "waypoint_id": 2,
      "point": {
            'lat': 43.90371,
            'lon': 42.71116,
      }
    },
    {
      "waypoint_id": 3,
      "point": {
            'lat': 43.89983,
            'lon': 42.71209,
      }
    },

  ]
}
def get_status_task(task_id):
    params = {
    'task_id': task_id,
    'key': API_KEY,
    }
    response = requests.get('https://routing.api.2gis.com/logistics/vrp/1.1.0/status', params=params)  
    print(response.json()) 


try:
    print(1)
    response = requests.post(URL+API_KEY, params=params, headers=headers, json=json_data)
    if response.status_code == 200:
        API_Data  = response.json()
        print(API_Data)
        task_id = API_Data.get('task_id')
        print(task_id)
        #task_id = '84b0fb628637f1d54594a466190208e9'
        time.sleep(10)
        get_status_task(task_id)
    elif response.status_code == 429:
        print('Превышен лимит по пиковой нагрузке. Уменьшите количество запросов в секунду или обратитесь в поддержку')


except HTTPError as e:
    print(e.response.text)




    

