import requests
import json

if __name__ == '__main__':
    id =  '419704'
    url = 'https://api.themoviedb.org/3/movie/{}?api_key=5284936e2774291ab4701bf2b2ac9f6d&language=en-US'.format(id)
    response = requests.post(url, id)
    response_json = response.json()
    

    

    print(response_json)