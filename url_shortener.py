import requests
import os
from dotenv import load_dotenv



def shorten_link(full_link, link_name):
    load_dotenv()
    KEY = os.getenv('API_KEY')
    BASE_URL = 'https://cutt.ly/api/api.php'

    payload = {'key': KEY, 'short': full_link, 'name': link_name}
    request = requests.get(BASE_URL, params=payload)
    data = request.json()

    print('')

    try:
        title = data['url']['title']
        short_link = data['url']['shortLink']

        print('Title', title)
        print('Link', short_link)
    except:
        status = data['url']['status']
        print('Uh Oh, Error Status:', status)

link = input('Enter a link: >>')
name = input('Enter a link name: >>')

shorten_link(link, name)
