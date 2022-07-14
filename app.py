from traceback import print_tb
import requests
from bs4 import BeautifulSoup as soup
from flask import Flask
app = Flask(__name__)


def get_lyrics(track_name):
    try:
        r = requests.get(f'https://gaana.com/song/{track_name}')
        print(r.status_code)
        if r.status_code == 404:
            return {"status": 404, "message": "The Lyrics you are looking for not found!"}
        source = soup(r.text, 'html.parser')
        source.prettify()
    # print(source)
    # print("Break")
    # print(source)
        lyric_container = source.find('div', {'class': 'data'})
        lyric_para = lyric_container.find('p')
        print(lyric_para.text.split("\n"))
        return lyric_para.text.split('\n')
    except:
        return {"status": 500, "message": "There some error occurred while downloading lyrics"}






# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.

 
# Flask constructor takes the name of
# current module (__name__) as argument.

 
# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def index():
    return 'Lyrics Scrapper API'

@app.route('/lyrics/<track_name>')
def lyrics_fetch(track_name):
    lyrics = get_lyrics(track_name)
    return {"lyrics":lyrics}
    

 
# main driver function
if __name__ == '__main__':
 
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()