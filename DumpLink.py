from selenium import webdriver

browser = webdriver.Firefox()

browser.get('http://websters.yourdictionary.com/')
links = browser.find_elements_by_css_selector('.slider_link')
f = open('links', 'w')
for link in links:
    f.write(link.get_attribute('href') + '\n')
f.close()
