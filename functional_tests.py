from selenium import webdriver

# Gwen goes to check out the app's homepage 
browser = webdriver.Firefox()
browser.get('http://localhost:8000')

# She notices page title and header mention todo lists
assert 'TODO' in browser.title

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
browser.quit()