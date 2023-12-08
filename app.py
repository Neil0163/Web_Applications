import os
from flask import Flask, request
from lib.album_repository import AlbumRepository 
from lib.database_connection import get_flask_database_connection
from lib.album import Album
from lib.artists_repository import ArtistRepository
from lib.artists import Artists




# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==
#1) create the inital app.route along with path and method
#   def the function
#   return '' (first test) 
@app.route('/albums', methods = ['POST'])
def post_album():
    if has_invalid_album_parameters(request.form):
        return "You need to submit a title, release_year and artist_id", 400
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    album = Album(
        None,
        request.form['title'], 
        request.form['release_year'],
        request.form['artist_id'])  
    repository.create(album)
    return '', 200
#2) create the inital app.route along with path and method
#   def the function 
#   return '' (first test)
#   set up a database connection, connection = get_flask_databe_connection(app)
#   set up a repository passing connection var in parameter will need importing /creating
#   Allow errors to guide 
@app.route('/albums', methods = ['GET'])
def get_album():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    return'\n'.join(
        f"{album}" for album in repository.all()
    )   
def has_invalid_album_parameters(form):
    return 'title' not in form or \
        'release_year' not in form or \
        'artist_id' not in form
        
######## ARTISTS SECTION ################
@app.route('/artists', methods = ['POST'])
def post_artist():
    if 'artist_name' not in request.form or 'genre' not in request.form:
        return 'You need to submit an artist', 400
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artist = Artists(
        None,
        request.form['artist_name'],
        request.form['genre'])
    repository.create(artist)
    return '', 200
    
@app.route('/artists', methods=['GET'])
def get_artists():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artists = repository.all()
    artist_names = [artist.artist_name for artist in artists]
    return ', '.join(artist_names), 200


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))