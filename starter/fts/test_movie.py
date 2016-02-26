from tests import FunctionalTest, root_url
import requests


class TestMovieListPage(FunctionalTest):

    def setUp(self):
        self.url = root_url + 'movie_list'
        get_browser=self.browser.get(self.url)
        
    def test_movie_list_page_response_code(self):
        #test that movie_list page exists and returns the proper response code
        r = requests.get(self.url)
        self.assertEqual(r.status_code, 200)

    def test_movie_list_page_display_all(self):
        #test that movie_list page displays all 200 movies
        movie_list_items = self.browser.find_elements_by_css_selector('li.movie_item')
        self.assertEqual(len(movie_list_items), 200)



        

    