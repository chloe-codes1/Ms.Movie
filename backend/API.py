import requests
import os

tmdb_api_key = os.getenv("TMDB_API_KEY")
tmdb_ver3_base_url = 'https://api.themoviedb.org/3/'

def get_genres(tmdb_id):
    url = f'{tmdb_ver3_base_url}genre/movie/list?api_key={tmdb_api_key}'
    response = requests.get(url).json()
    data = response['genres']
    for d in data:
        if d.get('id') == tmdb_id:
            return d.get('name')

