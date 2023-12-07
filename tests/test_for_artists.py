from lib.artists import Artists

def test_for_constructs_artist():
    artists = Artists(1, 'Test Name', 'Test Genre')
    assert artists.id == 1 
    assert artists.artist_name == 'Test Name'
    assert artists.genre == 'Test Genre'
    
def test_for_equality():
    artist_1 = Artists(1, 'Test Name', 'Test Genre') 
    artist_2 = Artists(1, 'Test Name', 'Test Genre')
    assert artist_1 == artist_2
    
def test_for_formatting():
    artists = Artists(1,'Test Name', 'Test Genre') 
    assert str(artists) == "Artists(1, Test Name, Test Genre)"