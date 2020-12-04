from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Gwen goes to check out the app's homepage
        self.browser.get('http://localhost:8000')

        # She notices page title and header mention todo lists
        self.assertIn('TODO', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1') # provided by selenium
        self.assertIn('TODO', header_text)
        
        # She is invited to enter a todo item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual( # assert value of placeholder text for element
            inputbox.get_attribute('placeholder'),
            'Enter a TODO item'
        )

        # She types "Mow the lawn" into a textbox
        inputbox.send_keys('Mow the lawn') # selenium's way of typing

        # When she hits enter, the page updates and now lists:
        # "1: Mow the lawn" as an item on the todo list
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1) # make sure browser has finished loading

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_name('tr')
        self.assertTrue(
            any(row.text == '1: Mow the lawn') for row in rows
        )

        # There still exists the textbox inviting Gwen to add
        # another item. She enters "Buy some kombucha" as another
        # item on the list.
        self.fail('finish the test!')

        # The page updates again, now shows two items on her list

        # Gwen wonders if the site will remember her list. Then
        # she sees the site has generated a unique URL for her
        # and there is some explanatory text to that effect.

        # She visits that URL - her todo list is still there

        # Satisfied, she closes the browser()


if __name__ == '__main__':
    unittest.main(
        warnings='ignore'
    )  # automatically finds test classes and methods in the file and runs them
