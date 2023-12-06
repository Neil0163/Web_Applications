# Tests for your routes go here

def test_for_get_add_name(web_client):
    response = web_client.get('/names?add=Eddie')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Julia,Alice,Karim,Eddie'