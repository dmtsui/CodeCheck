import sqlite3
import pickle

cbc = pickle.load(open('cbc_sql.pkl'))

codes=[]

conn = sqlite3.connect('cbc.db')
conn.text_factory = str
c = conn.cursor()

c.execute("""DROP TABLE IF EXISTS codes """)
c.execute("""CREATE TABLE codes (section TEXT, name TEXT, code_type TEXT, chapter TEXT, 
								top_section TEXT, content BLOB) """)

for code in cbc.keys():
	section = code
	chapter = cbc[code]['chapter']['number']
	top_section = cbc[code]['section']['number']
	content = cbc[code]['content']
	name = cbc[code]['name']
	code_type = unicode(cbc[code]['type'])
	#print (section, name, code_type, chapter, top_section, content)
	codes.append((section, name, code_type, chapter, top_section, content))

c.executemany("""INSERT INTO codes VALUES (?,?,?,?,?,?) """, codes)
conn.commit()
conn.close()


