from lib.album_repository import AlbumRepository
from lib.album import Album 



#1) Test for construct 
#   create function 
#   create album Var
#   Assert all of relvant contructors id, title, release_year, artist id
def test_for_construct():
    album = Album(1, "Test Title", 2005, 1)
    assert album.id == 1 
    assert album.title == "Test Title"
    assert album.release_year == 2005
    assert album.artist_id == 1
    
#2) Create test for equality 
    #define function 
    #create album1 set to what Album should be
    #create album2 set to what Album should be 
    #assert album1 == album2 
def test_for_equality():
    album1 = Album(1, "Test Title", 2005, 1)
    album2 = Album(1, "Test Title", 2005, 1)
    assert album1 == album2 
    
#3) Create test for formatting 
#   Define function 
#   set album to what it should be
#   assert the result as a str calling calling album and finally what it should be
def test_for_formatting():
    album = Album(1, "Test Title", 2005, 1) 
    assert str(album) == 'Album(1, Test Title, 2005, 1)'
    