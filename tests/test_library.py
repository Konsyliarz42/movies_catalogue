from . import app, pytest

@pytest.mark.parametrize(
    'list_type, results', (
        ('popular', '4'), ('popular', '12'), ('popular', '20'),
        ('now_playing', '4'), ('now_playing', '12'), ('now_playing', '20'),
        ('top_rated', '4'), ('top_rated', '12'), ('top_rated', '20'),
        ('upcoming', '4'), ('upcoming', '12'), ('upcoming', '20')
))
def test_homepage(list_type, results):
    with app.test_client() as client:
        response = client.get(f"/?list_type={list_type}&results={results}")
        assert response.status_code == 200