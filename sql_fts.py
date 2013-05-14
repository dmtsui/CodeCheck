import sqlite3
import pickle

cbc = pickle.load(open('cbc_sql.pkl'))
index = pickle.load(open('index.p'))

codes=[]
indexes = []

conn = sqlite3.connect('cbc_fts.db')
conn.text_factory = str
c = conn.cursor()

c.execute("""DROP TABLE IF EXISTS codes """)
c.execute("""CREATE VIRTUAL TABLE codes USING fts4(section TEXT, name TEXT, code_type TEXT, chapter TEXT, 
								top_section TEXT, content BLOB) """)
c.execute("""DROP TABLE IF EXISTS idx """)
c.execute("""CREATE VIRTUAL TABLE idx USING fts4(name TEXT, content text) """)

for code in cbc.keys():
	section = code
	chapter = cbc[code]['chapter']['number']
	top_section = cbc[code]['section']['number']
	content = cbc[code]['content']
	name = cbc[code]['name']
	code_type = unicode(cbc[code]['type'])
	#print (section, name, code_type, chapter, top_section, content)
	codes.append((section, name, code_type, chapter, top_section, content))

for entry in index.keys():
	index_name = entry
	index_content = unicode(index[entry])
	indexes.append((index_name, index_content))

c.executemany("""INSERT INTO codes VALUES (?,?,?,?,?,?) """, codes)
c.executemany("""INSERT INTO idx VALUES (?,?) """, indexes)
conn.commit()
conn.close()


