# Retrieve Spotify artist IDs.

import streamlit
import spotipy
import time
from PIL import Image


def get_artist_ids(names):
    """
    Retrieves an artist with their associated ID.
    :param names
        Name of the artist.
    :return dict
        A dictionary containing artists and their associated IDs.
    """
    spotify = spotipy.Spotify(auth_manager=spotipy.SpotifyClientCredentials())
    data = {}

    for name in names:
        for artist_info in spotify.search(q=f'artist:{name}', type='artist')['artists']['items']:
            if artist_info['name'] == name and name not in data:
                data[name] = artist_info['uri'].split(':')[-1]
            else:
                data[name] = 'Unable to find ID.'
            break

    return data


def generate_download(file_data):
    streamlit.download_button(label='Download file containing IDs.', file_name='id_list',
                              data='\n'.join(f'{k}: {v}' for k, v in file_data.items()))


def main():
    streamlit.set_page_config(page_title='Trieve',
                              layout="centered",
                              initial_sidebar_state="auto")
    image = Image.open('images/trieve_image.png')
    streamlit.image(image)
    artist_names = sorted(streamlit.text_input("Enter the name(s) of the artist.",
                                               help="""Separate multiple artist names with 
                                               a comma and a space.
                                               Artist names are case sensitive.""").split(', '))

    if artist_names != ['']:
        with streamlit.spinner(text='Retrieving IDs...'):
            time.sleep(3)
            generate_download(get_artist_ids(artist_names))


main()
