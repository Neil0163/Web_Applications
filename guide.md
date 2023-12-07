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

   POST/artists                                                             
    Parameters:
    artist_name: string
    genre: number (str)
    artist_id: number    (str)
  Expected response (200 OK):       

  GET/artists

  **********CREATE SOME EXAMPLES**********
    
    Working

    POST/artists
    artist_name: ACDC
    genre: Rock
    artist_id: 2
    Expected response (200 ok)

    GET/artists
    Expected response (200 ok)
    Artists(1, Oasis, Rock, 1)
    Artists(2, ACDC, Rock,  2)

    None working 

      GET/albums
    Expected response (400 bad request) 
    you need to submit a title, artis_name, release_year and artist_id
     Artists(1, Oasis, Rock, 1)
     Artists(2, ACDC, Rock,  2)

**********INITAL TEST**************

1) create the function
2) pass db_connection and web_client as arguments
3) create the seed for db.connection 
4) create response for web_client.post(insert path and data here)
5) assert the response for status code 
6) assert the response for data empty string

def test_post_albums(db_connection, web_client):
    db_connection.seed("seeds/record_store.sql")
    post_response = web_client.post("/albums", data={
        'title': 'Victorla',
        'artist_name': 'Oasis',
        'release_year': '1995',
        'artist_id': '1'
        })
    assert post_response.status_code == 200
    assert post_response.data.decode('utf-8') == ''

Code: @app.route('/albums', methods= ['POST'])
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


