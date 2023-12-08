
######### ALBUM TEST #####################
from flask.testing import FlaskClient


from lib.database_connection import DatabaseConnection


def test_for_post_album(db_connection,web_client):
    db_connection.seed("seeds/record_store.sql")
    post_response = web_client.post('/albums', data = {
        'title': 'Wonderwall',
        'release_year': '2005',
        'artist_id': '1'
    })
    assert post_response.status_code == 200
    assert post_response.data.decode('utf-8') == ''
    get_response = web_client.get('/albums')
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == '' \
        "Album(1, MasterPlan, 2005, 1)\n" \
        "Album(2, Wonderwall, 2005, 1)"   
def test_for_get_albums(db_connection, web_client):
    db_connection.seed("seeds/record_store.sql") 
    get_reponse = web_client.get('/albums')
    assert get_reponse.status_code == 200 
    assert get_reponse.data.decode('utf-8') == '' \
        "Album(1, MasterPlan, 2005, 1)"        
def test_for_album_with_no_data(db_connection, web_client):
    db_connection.seed("seeds/record_store.sql")
    post_response = web_client.post('/albums')
    assert post_response.status_code == 400
    assert post_response.data.decode('utf-8') == '' \
        "You need to submit a title, release_year and artist_id"
    get_response = web_client.get('/albums')
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == '' \
        "Album(1, MasterPlan, 2005, 1)"
############# ARTIST TEST #####################################
def test_for_post_artist(db_connection, web_client):
    db_connection.seed ('seeds/artiststore.sql')
    post_response = web_client.post('/artists', data ={
        'artist_name': 'Wild Nothing',
        'genre': 'Indie'
    })
    assert post_response.status_code ==200
    assert post_response.data.decode('utf-8') == ''
    get_response =web_client.get('/artists')
    assert get_response.status_code == 200 
    exp_response = 'Pixes, ABBA, Taylor Swift, Nina Simone, Wild Nothing'
    assert get_response.data.decode('utf-8')== exp_response
    
def test_artist_with_no_data(db_connection, web_client):
    db_connection.seed('seeds/artiststore.sql')
    response = web_client.post('/artists')
    assert response.status_code == 400 
    exp_response = "error BAD request, please submit artist_name and genre"
    assert response.data.decode('utf-8') == exp_response
    get_response = web_client.get('/artists')
    assert get_response.status_code == 200 
    exp_response = 'Pixes, ABBA, Taylor Swift, Nina Simone'
    assert get_response.data.decode('utf-8')== exp_response 