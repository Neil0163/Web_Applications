from lib.album_repository import AlbumRepository
from lib.album import Album 

#1) Test drive a get all method
#   Create a function and pass db_connection as the argument 
#   Create an AlbumRepository with db_connection in parameter
#   seed database 
#   call the .all method and ensure it returns relvant data in this case an album with relvent colums
def test_all(db_connection):
    db_connection.seed("seeds/record_store.sql")
    repository = AlbumRepository(db_connection)
    repository.all() == [
        Album(1, 'Wonderwall', 2005, 1)
    ]
    
#Create a test for create method
#create a function and pass db_connection as argument 
#create a repository for AlbumRepoistory db_connection 
# Seed database 
#create album set to album 
#call reposoitroy.create()
#call the assert all method, with what we expect to return 
def test_for_create(db_connection):
    db_connection.seed("seeds/record_store.sql")
    repository = AlbumRepository(db_connection)
    album = Album(None, "Wonderwall", 2005, 1)
    repository.create(album)
    assert repository.all() == [
        Album(1, 'MasterPlan', 2005, 1),
        Album(2, "Wonderwall", 2005, 1)
    ]
    