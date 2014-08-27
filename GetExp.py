from selenium import webdriver
import sqlite3

# profile = webdriver.FirefoxProfile('profile')
# browser = webdriver.Firefox(profile)

options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=e:/Users/Jie/Desktop/GetDict")
browser = webdriver.Chrome('e:/Users/Jie/Desktop/GetDict/chromedriver', 0, options)

conn = sqlite3.connect('dictd.db')
c = conn.cursor()
c.execute('SELECT * FROM dict WHERE exp IS NULL LIMIT 7000 OFFSET 14000')

for i in c.fetchmany(7000):
    w = i[0]
    url = 'http://www.yourdictionary.com/' + w
    browser.get(url)
    try:
        e = browser.execute_script("""
            var w = document.querySelector('.hdr-partner-websters');
            if (w === null) {
                h = document.querySelectorAll('h2');
                for (var j = 0; j < h.length; j++) {
                    if (h[j].textContent.indexOf('Webster') !== -1) {
                        w = h[j];
                        break;
                    }
                }
            }
            var d = w.nextElementSibling;
            var list = [];
            for (var e=d.nextElementSibling,i=0; e.nodeName === 'DIV';e = e.nextElementSibling,i++){
                list[i] = e;
            }
            return list;
            """)
    except:
        continue
    exp = u''
    for d in e:
        exp = exp + d.get_attribute('innerHTML')
    t = (exp, w)
    c.execute('UPDATE dict SET exp = ? WHERE key = ?', t)
    conn.commit()
conn.close()
