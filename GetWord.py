from selenium import webdriver
import sqlite3

browser = webdriver.Firefox()
conn = sqlite3.connect('dictd.db')
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS dict (key text, word text, exp text)')
f = open('links', 'r')
for line in f:
    browser.get(line)
    words = browser.find_elements_by_css_selector('.large-4 li a')
    for word in words:
        item = (word.get_attribute('href')[30:-9], word.text)
        c.execute('INSERT INTO dict (key, word) VALUES (?, ?)', item)
conn.commit()
conn.close()
f.close()
