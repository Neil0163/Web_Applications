from lib.artists import Artist

def test_for_construct():
    artist = Artist(1, 'TestName', 'TestGenre')
    assert artist.id == 1
    assert artist.artist_name == 'TestName'
    assert artist.genre == 'TestGenre'
    
def test_for_eq():
    artist_1 = Artist(1, 'TestName', 'TestGenre')
    artist_2 = Artist(1, 'TestName', 'TestGenre')
    assert artist_1 == artist_2
    
def test_for_formatting():
    artist = Artist(1, 'TestName', 'TestGenre')
    assert str(artist) == "Artist(1, TestName, TestGenre)"