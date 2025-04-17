import pickle
import requests
import joblib

from numpy.distutils.system_info import language_map
from typing_extensions import runtime

movies = pickle.load(open('movies.pkl','rb'))
similarity = joblib.load('similarity_compressed.pkl')
# similarity = pickle.load(open('similarity.pkl','rb'))

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=3300eddcea814fa40e8089cbc151c8d8"
    data = requests.get(url)
    data = data.json()
    # print(data)
    poster_path = data['poster_path']
    full_path = f"https://image.tmdb.org/t/p/w500/{poster_path}"
    return full_path

def fetch_profile_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key=3300eddcea814fa40e8089cbc151c8d8"
    data = requests.get(url)
    data = data.json()

    cast_data = []    # cast_list = [(image, name, character), (image, name, character),.........till 20]
                                    # image is profile_path
    for cast_member in data["cast"]:
        profile_path = cast_member.get("profile_path")
        if profile_path:  # Only include if image is available
            name = cast_member.get("original_name", "Unknown")
            character = cast_member.get("character", "Unknown")
            full_path = f"https://image.tmdb.org/t/p/w500{profile_path}"
            cast_data.append((full_path, name, character))

        if len(cast_data) == 20:  # Stop at 20 valid images
            break

    return cast_data

    # cast_data = [] #  cast_list = [(image, name, character), (image, name, character),.........till 20]

    # for i in range(20):   # If the image not available for any actor then it left black space there.
    #     cast_member = data["cast"][i]
    #     name = cast_member["original_name"]
    #     character = cast_member["character"]
    #     profile_path = cast_member["profile_path"]
    #     full_path = f"https://image.tmdb.org/t/p/w500{profile_path}"
    #
    #     cast_data.append((full_path, name, character))
    #
    # return cast_data

def fetch_movie_details(movie_id):
    """Fetch detailed information about a movie from TMDb API."""
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=3300eddcea814fa40e8089cbc151c8d8"
    data = requests.get(url).json()

    language = data['original_language'].upper()
    release_date = data['release_date']
    runtime = data['runtime']
    budget = data['budget']
    revenue = data['revenue']
    tagline = data['tagline']
    rating = data['vote_average']
    vote_count = data['vote_count']
    overview = data['overview']

    return language, release_date, runtime, budget, revenue, tagline, rating, vote_count, overview

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_lst = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:11]

    recommended_movies_names = []
    recommended_movies_posters = []
    for i in movies_lst:
        movie_id = movies.iloc[i[0]].movie_id

        recommended_movies_names.append(movies.iloc[i[0]].title)

        # Fetch Movie Poster from API
        recommended_movies_posters.append(fetch_poster(movie_id))

    return recommended_movies_names , recommended_movies_posters