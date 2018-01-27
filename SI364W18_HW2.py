## SI 364
## Winter 2018
## HW 2 - Part 1

## This homework has 3 parts, all of which should be completed inside this file (and a little bit inside the /templates directory).

## Add view functions and any other necessary code to this Flask application code below so that the routes described in the README exist and render the templates they are supposed to (all templates provided are inside the templates/ directory, where they should stay).

## As part of the homework, you may also need to add templates (new .html files) to the templates directory.

#############################
##### IMPORT STATEMENTS #####
#############################
from flask import Flask, request, render_template, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField, ValidationError
from wtforms.validators import Required
import json
import requests

#####################
##### APP SETUP #####
#####################

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hardtoguessstring'

####################
###### FORMS #######
####################




####################
###### ROUTES ######
####################

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/user/<name>')
def hello_user(name):
    return '<h1>Hello {0}<h1>'.format(name)

@app.route('/artistform', methods = ['POST', 'GET'])
def go_to_form():
    return render_template('artistform.html')

@app.route('/artistinfo', methods = ['POST', 'GET'])
def get_artist_info():
    if request.method == 'POST':
        user_artist = request.form.get('artist')

        base_url = 'https://itunes.apple.com/search?entity=musicTrack&attribute=artistTerm&term='
        music_dict = json.loads(requests.get(base_url+user_artist).text)

        result = music_dict['results']

        return render_template('artist_info.html', objects=result)

@app.route('/artistlinks')
def suggest_artists():
    return render_template('artist_links.html')

@app.route('/specific/song/<artist_name>')
def show_artist(artist_name):

    base_url = 'https://itunes.apple.com/search?entity=musicTrack&attribute=artistTerm&term='
    artist_dict = json.loads(requests.get(base_url+artist_name).text)

    artist_result = artist_dict['results']

    return render_template('specific_artist.html', results=artist_result)



if __name__ == '__main__':
    app.run(use_reloader=True,debug=True)
