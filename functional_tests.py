from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.pass_flag = False
        self.browser = webdriver.Firefox()

    def tearDown(self):
        if self.pass_flag == True:
            pass
        else:
            self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Gwen goes to check out the app's homepage
        self.browser.get('http://localhost:8000')

        # She notices page title and header mention todo lists
        self.assertIn('TODO', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1')
        self.assertIn('TODO', header_text.text)

        # She is invited to enter a todo item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(  # assert value of placeholder text for element
            inputbox.get_attribute('placeholder'), 'Enter a TODO item')

        # She types "Mow the lawn" into a textbox
        inputbox.send_keys('Mow the lawn')  # selenium's way of typing

        # When she hits enter, the page updates and now lists:
        # "1: Mow the lawn" as an item on the todo list
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)  # make sure browser has finished loading

        # self.pass_flag = True
        self.check_for_row_in_list_table('1: Mow the lawn')

        # There still exists the textbox inviting Gwen to add
        # another item. She enters "Buy some kombucha" as another
        # item on the list.
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy some kombucha')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        
        # The page updates again, now shows two items on her list
        self.check_for_row_in_list_table('1: Mow the lawn')
        self.check_for_row_in_list_table('2: Buy some kombucha')

        self.fail('finish the test!')


        # Gwen wonders if the site will remember her list. Then
        # she sees the site has generated a unique URL for her
        # and there is some explanatory text to that effect.

        # She visits that URL - her todo list is still there

        # Satisfied, she closes the browser()


if __name__ == '__main__':
    unittest.main(
        warnings='ignore'
    )  # automatically finds test classes and methods in the file and runs them
