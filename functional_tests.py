from selenium import webdriver
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
        self.fail('Finish the test!')  # this will fail, used as a reminder

        # She is invited to enter a todo item straight away

    # She types "Mow the lawn" into a textbox

    # When she hits enter, the page updates and now lists:
    # "1: Mow the lawn" as an item on the todo list

    # There still exists the textbox inviting Gwen to add
    # another item. She enters "Buy some kombucha" as another
    # item on the list.

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
