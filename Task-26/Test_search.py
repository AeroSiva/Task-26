from main import IMDB
import pytest

@pytest.fixture
def imdb_search_instance(request):
    imdb = IMDB()
    imdb.access_URL()
    yield imdb
    imdb.driver.quit()

def test_searched(imdb_search_instance):
    result = imdb_search_instance.fill_datas()
    assert result == 'with Quotes, Male, Include adult names (Sorted by Popularity Ascending)'