import re
import pickle

#load tables, figures, chapters, and sections from pickled files
tables = pickle.load(open('table.pkl'))
figures = pickle.load(open('figure.pkl'))
chapters = pickle.load(open('top_sections2.pkl'))
sections = pickle.load(open('sub_sections.pkl'))


#build the lists to loop through and combine all
#the separate dicitionaries into chapters dictionary

t_keys = tables.keys()
f_keys = figures.keys()
c_keys = chapters.keys()
s_keys = sections.keys()


for chp in c_keys:
	for top_section in chapters[chp]['sections'].keys():
		for table in t_keys:
			if re.search(top_section, table):
				chapters[chp]['sections'][top_section]['tables'][table] = tables[table]
		for figure in f_keys:
			if re.search(top_section, figure):
				chapters[chp]['sections'][top_section]['figures'][figure] = figures[figure]
		for section in s_keys:
			if re.search(top_section, section):
				chapters[chp]['sections'][top_section]['sections'][section] = sections[section]

output = open('part2.pkl','w')
pickle.dump(chapters,output)
output.close()	


		
		


