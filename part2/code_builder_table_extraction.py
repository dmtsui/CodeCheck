from bs4 import BeautifulSoup
import re
import pickle


f = open("cbc_part2(clean_up).html").read()
soup = BeautifulSoup(f)

table_dict = {}


for each in soup.find_all('table'):
	if each.caption:
		if each.caption.b:
			if each.caption.b.contents[0].string and each.caption.b.contents[0].string != ' ':
				if re.match(r'^TABLE.*', each.caption.b.contents[0].string):
					tmp = re.split(" "," ".join(map(unicode,each.caption.b.contents)),2)
					if len(tmp) == 2 or tmp[2] == '':
						table_dict[tmp[1]] = {'name':'','content': unicode(each)}
					else:
						table_dict[tmp[1]] = {'name':tmp[2],'content': unicode(each)}
					each.decompose()

out = open('cbc_part2(no_table).html','w')
out.write(str(soup))

output = open('table.pkl','w')
pickle.dump(table_dict,output)
output.close()

#					print range(len(each.caption.b.contents))
#					for i in range(len(each.caption.b.contents)):
#						if not isinstance(i, unicode):
#							print unicode(each.caption.b.contents[i])
#							each.caption.b.contents[i] = unicode(each.caption.b.contents[i])
#					print each.caption.b.contents
