from lib.artists_repository import ArtistRepository
from lib.artists import Artist
def test_all(db_connection):
    db_connection.seed('seeds/artiststore.sql')
    repository = ArtistRepository(db_connection)
    assert repository.all()==[
        Artist(1, 'Pixes', 'Indie'),
        Artist(2, 'ABBA', 'Pop'),
        Artist(3, 'Taylor Swift', 'Pop'),
        Artist(4, 'Nina Simone', 'Jazz')
    ]
    

def test_for_create(db_connection):
    repository =ArtistRepository(db_connection)
    db_connection.seed('seeds/artiststore.sql')
    artist = Artist(None, 'TestName', 'TestGenre')
    repository.create(artist)
    assert repository.all() == [
        Artist(1, 'Pixes', 'Indie'),
        Artist(2, 'ABBA', 'Pop'),
        Artist(3, 'Taylor Swift', 'Pop'),
        Artist(4, 'Nina Simone', 'Jazz'),
        Artist(5, 'TestName', 'TestGenre')
        ]