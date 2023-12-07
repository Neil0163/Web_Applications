from lib.artists_repository import ArtistRepository
from lib.artists import Artists

def test_all(db_connection):
    repository = ArtistRepository(db_connection)
    db_connection.seed('seeds/artiststore.sql')
    assert repository.all() == [
        Artists(1, 'Pixes', 'Indie'), 
        Artists(2, 'ABBA', 'Pop'),
        Artists(3, 'Taylor Swift', 'Pop'), 
        Artists(4, 'Nina Simone', 'Jazz')
        ]
def test_create_method(db_connection):
        repository = ArtistRepository(db_connection)
        db_connection.seed('seeds/artiststore.sql')
        artists = Artists(None, 'TestName', 'TestGenre')
        repository.create(artists)
        assert repository.all() == [
        Artists(1, 'Pixes', 'Indie'), 
        Artists(2, 'ABBA', 'Pop'),
        Artists(3, 'Taylor Swift', 'Pop'), 
        Artists(4, 'Nina Simone', 'Jazz'),
        Artists(5, 'TestName', 'TestGenre')
        ]