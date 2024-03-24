import requests
import yaml

with open('config.yaml', encoding='utf-8') as f:
    data = yaml.safe_load(f)

url2 = data['URL2']


def title_for_posts_owner_not_me(token):
    res = requests.get(url=url2, headers={'X-Auth-Token': token}, params={'owner': 'notMe'})
    title_res = [item['title'] for item in res.json()['data']]
    return title_res
