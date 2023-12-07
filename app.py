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
<<<<<<< HEAD
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

=======
#Phase 1
#Create app.route(path, methods)
#Def function name
#Create exsisting name list 
# print statement for exsiting list
# Create add_name var with request for arg.get(argument)
#add print statement f string names to be added from add_name
#Phase 2
#create if statement for add_name
#nested within add name create new_name var set to add_name and split at comma
#print to check new name added
#Phase 3
#create a for loop to iterrate over name in new name
#append to esisting name and strip name
#print final list of names from esisting names using F string 
# return the result using ', '.join to esiting names
#run the app 
#check the broswer at http://127.0.0.1:5001/names?add=Eddie,leo
#check the terminal for print statements 
@app.route('/names', methods = ['GET'])
def get_add_names():
    existing_name = ['Alice', 'Julia', 'Karim']
    print(f" This is the inital existing names{existing_name} ")
    add_name = request.args.get('add')
    print(f" This is checking that the add function works {add_name}")
    if add_name:
        new_name = add_name.split(',')
        print(f" check that the names are returned as list {new_name}")
    for name in new_name:
        existing_name.append(name)
        print(f"Checks that the names are added to existing list {existing_name}")
        existing_name = sorted(existing_name)
        print(f' The list of names should now be in order {existing_name}')
    updated_name = existing_name
    print(f" This should be the final output {updated_name}")
    return', '.join(updated_name)
>>>>>>> 54b43fff3f8b7b2c780a605d139f8fe804278925

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))