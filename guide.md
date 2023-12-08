******SINGLE DESIGN TABLE RECIPE*******
1) Extract the Nouns
    Artist, Name, Genre, Artist, ID

2) Set Table Record, name of table(plural), name of colums 
    Record = Artist            colum names = id, name, Genre, Artist_id
    Table Name = artists

3) Decide colum types e.g text, int etc
    id:Serial  Name:text, genre:text, Artist_id:int 

4) Write the Sql using seed template
    CREATE TABLE albums (
      id SERIAL PRIMARY KEY,
      name text,
      genre text,
      artist_id int
);
5) Create the table 

******SEED FILE**********************

1) Create Seed file naming it to something appropriate 

*******DATABASE CONNECTION************

1) Adjust database connection py file on DEV and TEST enter relvant names
2) Adjust seed_dev_data_py file for connection using your new created seeded file

*******CREATE DATABASE***************

1) Create database for both enviroments DEV and TEST eg record_store, record_store_test
2) Seed the database with the created seed file using python seed_dev_data file

*******ROUTE DESIGN******************
include hhtp method, path and any query or body parameters and type eg string etc

GET/artists
    "Pixes\n" +
    "ABBA\n" +
    "Taylor Swift\n" +
    "Nina Simone"

(no content)

POST/artists                                                             
    Parameters:
    artist_name: string
    genre: string
    Expected response (200 OK):       

  **********CREATE SOME EXAMPLES**********
    
    Working

    GET/artists
    Expected response (200 ok)
        "Pixes\n" +
        "ABBA\n" +
        "Taylor Swift\n" +
        "Nina Simone"

    POST/artists
    name: Wild Nothing
    genre: Indie
    Expected response (200 ok)


    None working 

      GET/artist
    Expected response (400 bad request) 
    you need to submit an artist
        "Pixes\n" +
        "ABBA\n" +
        "Taylor Swift\n" +
        "Nina Simone"

**********INITAL TEST**************

1) create the function
2) pass db_connection and web_client as arguments
3) create the seed for db.connection 
4) create response for web_client.post(insert path and data here)
5) assert the response for status code 
6) assert the response for data empty string

def test_get_artists(db_connection, web_client):
    db_connection.seed("seeds/artiststore.sql")
    response = web_client.get("/artists")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "\n".join([
        "Pixes\n" +
        "ABBA\n" +
        "Taylor Swift\n" +
        "Nina Simone"
        ])
    assert post_response.status_code == 200
    assert post_response.data.decode('utf-8') == ''

Code: @app.route('/artist', methods= ['GET'])
def post_album():
    return ""

7) Within the same test:
    create get repsonse variable for web_client.(method)(path)
    assert on response for status code 
    assert on response for data

     get_response = web_client.get('/albums')
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == '' \
    'Album(1, Masterplan, Oasis, 1995, 1)\n' \
    'Album(4, Victorla, Oasis, 1995, 1)'

code: @app.route('/albums', methods=['GET'])
def get_album():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)

dont forget to import relvant such as:
    import os
    from flask import Flask, request
    from lib.database_connection import get_flask_database_connection
    from lib.album_repositroy import AlbumRepository 

******CREATE REPOSITORY**********

1) Create a new repositroy 
2) Create test for new repository file
3) Start to create test for repository file and start test (see below) for example
        def test_all(db_connection):
    repositrory = AlbumRepository(db_connection)
    assert repositrory.all() == [
        Album(1, 'Masterplan', 'Oasis', 1995, 1)
    ]
    code:

    class AlbumRepository:
    def __init__(self, connection):
        self.connection = connection

    def all(self):
        pass

The test should run in a way where it guides you through.

*******CREATE A METHOD FILE *************8

1) create a neww file for method in this case Album 
2) create a new test file for method 
Refer to previous work if stuck 
test should guide you through 

Create test for post:
    seed the db connection
    set up web_clinet.post 
    set up assert for status code and body data 

    create inital code too pass



Carry on building app.py code, passing a connection to Get, youll be pushed to create Rpository. 
Start to build repository creating a test for all, follow errors. 
Youll notice you need to create Artist file and run test for Artist this will be your 'model" file so it will need test for 
    construct (initaite object), equality, formatting test (dont rush ahead allow errors to guide)
Come back and finish off all method executing SQL 
youll now need to do your test for eq 
All should be working well...go test the app
Notice now youll need to carry on building code in app finish the all() in GET request
Youll now be promted through error to come back to artist and create code for formatting
Once this is done youll then see that Wild Nothing will become an error this is because its a test and function hasnt been made too add 
Follow the errors for creaate youll need to execute SQL again
Create test for get 
    seed the db connection 
    set up web_client.get
    set up assert for status code and data
    add these asserts to post 
    
Next start driving out the POST route behaviour 
Test should now all pass
Create test for error 400 (copy pasting code from POST route with slight modifications)
Modify POST route to account for BAD request



    












