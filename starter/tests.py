import unittest
import os
import sys
from selenium import webdriver


#default URL routing
root_url =  'http://127.0.0.1:8000/' 



class FunctionalTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(2)


    @classmethod    
    def tearDownClass(self):
        self.browser.close()


        
def run_functional_tests(pattern=None):
    print 'running tests'
    if pattern is None:
        tests = unittest.defaultTestLoader.discover('fts')
    else:
        pattern_with_globs = '*%s*' % (pattern,)
        tests = unittest.defaultTestLoader.discover('fts', pattern=pattern_with_globs)

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(tests)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        
        run_functional_tests()
    else:
        
        run_functional_tests(pattern=sys.argv[1])
