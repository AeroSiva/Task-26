'''
    Using Page Object mmodel (POM), Explicit wait, Expected Conditions, pytest kindly do the following task as mentioned below:-

    1. Go tohttps://www.imdb.com/search/name/
    2. Fill the data given in the input Boxes, select Boxes and Drop Down mwenu on the webpage and do a search.
    3. Do not use sleep() method fo the task.
'''

from main import IMDB
import pytest

@pytest.fixture
def imdb_search_instance():
    imdb = IMDB()
    imdb.access_URL()
    yield imdb                     # The yield statement provides the IMDB instance to the test function.
    imdb.driver.quit()

# Test 1 to check whether after selecting required options the page load and searched as per selection
    """
    Assertion is made by checking whether the title of the page is changed as per the requirement.
    """
def test_searched(imdb_search_instance):
    expected_title = 'with Quotes, Male, Include adult names (Sorted by Popularity Ascending)' # Title 
    actual_title = imdb_search_instance.fill_datas()
    assert actual_title == expected_title,f"Expected result: {expected_title}, but got: {actual_title}" 