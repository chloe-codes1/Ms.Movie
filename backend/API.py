import requests
import os
# from dotenv import load_dotenv

# load_dotenv()



tmdb_api_key = os.getenv("TMDB_API_KEY")
# tmdb_api_key = ''
tmdb_ver3_base_url = 'https://api.themoviedb.org/3/'

def get_genres(tmdb_id):
    url = f'{tmdb_ver3_base_url}genre/movie/list?api_key={tmdb_api_key}&language=ko-kr'
    response = requests.get(url).json()
    data = response['genres']
    for d in data:
        if d.get('id') == tmdb_id:
            return d.get('name')

print('장르~', get_genres(12))

# def get_actors():

