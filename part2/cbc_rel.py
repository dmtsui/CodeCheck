from bs4 import BeautifulSoup
import urllib2
import re
import sqlite3


con = sqlite3.connect('cbc.db')
c = con.cursor()
c.execute('''DROP TABLE IF EXISTS code_rel ''')
c.execute('''CREATE TABLE IF NOT EXISTS code_rel(code TEXT NOT NULL, rel TEXT NOT NULL) ''')

t = c.execute('''SELECT name, children FROM cbc_code ''')

all_values =[]

for row in t:
    if str(row[1]) != '[]' and str(row[0]) != 'None' :
        for each in row[1][1:-1].split(', '):
            all_values.append((str(row[0]),str(each[1:-1])))
#            c.execute('''INSERT INTO code_rel(code,rel) values(?,?)''',values)
#            con.commit()
#print all_values
c.executemany('INSERT INTO code_rel VALUES (?,?)', all_values)
con.commit()
            
    

#for row in c.execute('''SELECT name, children FROM cbc_code '''):
#    name = row[0]
#    if cmp('[]',str(row[1]) ):
#        print name
#        for each in str(row[1][1:-1]).split(', '):
#            values = (str(row[0]),each)
#            c.execute('''INSERT INTO code_rel(code,rel) values(?,?)''',values)
# WHERE name='3101F.4' OR name='3101F.5' con.commit()
print "done"
