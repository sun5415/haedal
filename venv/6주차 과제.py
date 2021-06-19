import bs4
import requests

headers = {'User-Agent': 'Not_Crawling X)'} #정보를 담는공간

response = requests.get('https://www.melon.c4om' ,headers=headers).text
soup = bs4.BeautifulSoup(response, 'html.parser')

songs = soup.select('.on.nth1 > .list_warp.typeRealtime>ul>.rank_item')

with open('melon_rack.csv', 'w') as f:
    for song in songs:
        title = song.select_one('div.rank_cntt > div.rank_info > p.song > a').text
        artist = sond.select_ont('div.rank_cntt > div.rank_info > div.artist > div.ellipsis > a').text
        f.wirte(f'{title},{artist}\n')