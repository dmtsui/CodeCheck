from bs4 import BeautifulSoup
import re
import pickle


table_dict ={}

f = open('cbc_part2(no_table).html').read()

soup = BeautifulSoup(f)

for each in soup.find_all('img'):
	if each.parent.name not in ['li','ol']  and each.parent.parent.name not in ['li','ol']:
		if re.match(r'^FIGURE.*', each['alt']):
			tmp = re.split(' ',unicode(each['alt']),2)
			if tmp[1] not in table_dict:
				if len(tmp) != 2:
					table_dict[unicode(tmp[1])] = {'name':(tmp[2]), 'content': unicode(each['src'])}
				else:
					table_dict[unicode(tmp[1])] = {'name':u'', 'content': unicode(each['src'])}
			else:
				if len(tmp) != 2:
					table_dict[unicode(tmp[1])][str(len(table_dict[tmp[1]])+1)] = {'name':tmp[2], 'content': unicode(each['src'])}
				else:
					table_dict[unicode(tmp[1])][str(len(table_dict[tmp[1]])+1)] = {'name':u'', 'content': unicode(each['src'])}	
			each.parent.decompose()

out = open('cbc_part2(no_figure).html','w')
out.write(str(soup))

output = open('figure.pkl','w')
pickle.dump(table_dict,output)
output.close()			
				 
