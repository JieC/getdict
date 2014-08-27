import sqlite3

conn = sqlite3.connect('dictd.db')
c = conn.cursor()
f = open('dict.txt', 'w')

for i in c.execute('SELECT * FROM dict WHERE exp IS NOT NULL'):
    f.write(i[0].encode('utf8') + '\n')
    f.write(i[1].encode('utf8') + '\n')
    f.write(i[2].encode('utf8') + '\n')
    f.write('</>\n')

f.close()
conn.close()
