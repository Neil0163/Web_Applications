from lib.artists import Artists

class ArtistRepository:
    def __init__(self, connection):
        self._connection = connection
    def all(self):
        rows = self._connection.execute('SELECT * FROM artists;')
        return[
            Artists(row['id'], row['artist_name'], row['genre'])
            for row in rows
        ]
        
    def create(self, artists):
        self._connection.execute(
            "INSERT INTO artists (artist_name, genre) VALUES (%s, %s)", 
            [artists.artist_name, artists.genre]
        )
        return None