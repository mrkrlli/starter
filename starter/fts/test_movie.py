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

    def test_movie_list_page_click_detail_link(self):
    	#test that clicking a movie detail link will take you to the appropriate movie detail link page
		
		#this will click the first movie item, which should be Deadpool
    	movie_items = self.browser.find_elements_by_css_selector('li.movie_item a')
    	movie_items[0].click()

    	self.assertEqual(self.browser.current_url, root_url + 'movie_details/771390242')


class TestMovieListPagestMovieDetailsPage(FunctionalTest):

    def setUp(self):
        self.url = root_url + 'movie_details/771390242' #deadpool movie id
        get_browser=self.browser.get(self.url)


    def test_movie_details_page_response_code(self):
        #test that movie_list page exists and returns the proper response code
        r = requests.get(self.url)
        self.assertEqual(r.status_code, 200)

    def test_movie_details_page_information(self):
    	#test that this page shows the details for the deadpool movie
    	movie_title = self.browser.find_element_by_css_selector('h3.movie_title')
    	self.assertEqual(movie_title.text, "Deadpool")

    	#test that actors and characters are displayed
    	members = self.browser.find_elements_by_css_selector('li.movie_members')
    	self.assertEqual(len(members), 5)





        

    