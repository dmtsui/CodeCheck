from bs4 import BeautifulSoup
import re
import pickle

re_chp = re.compile(r'^c[0-9].*')
re_sec = re.compile(r's.*')
re_apx = re.compile(r'[A-Z]')

chp_dict = {}
sec_dict = {}


f = open('cbc_part1(no_figure).html').read()

soup = BeautifulSoup(f)

for each in soup.find_all('a',{'name': re_chp}):
	tmp = re.split(' ',each.next_sibling.contents[0],2)
	chp_dict[tmp[1]] = {'name':tmp[2], 'sections':{}, 'figures':{},'tables':{}}
	each.next_sibling.decompose()
	each.decompose()
for each in soup.find_all('a',{'name':re_sec}):
	tmp = re.split(' ',each.next_sibling.contents[0],2)
	sec_dict[tmp[1]] = tmp[2]
	each.next_sibling.decompose()
	each.decompose()

#print sec_dict.keys()



for each in chp_dict.keys():
	if each[-1] not in ['A','B','C','D','E','F']:
		for m in sec_dict.keys():
			if m[-1] not in ['A','B','C','D','E','F']:
				if m[:2] == each:
					chp_dict[each]['sections'][m] = {'name':sec_dict[m], 'sections':{},'figures':{},'tables':{}}
				else:
					if len(each) < 2 and m[0] == each:
						chp_dict[each]['sections'][m] = {'name':sec_dict[m], 'sections':{},'figures':{},'tables':{}}


	else:
		for m in sec_dict.keys():
			if m[-1] in each[-1]:
				if m[:2] == each[:2]:
					chp_dict[each]['sections'][m] = {'name':sec_dict[m], 'sections':{},'figures':{},'tables':{}}
			# else:
			# 	if m[0] not in ['1','2','3']:
			# 		chp_dict[m] = {'name': sec_dict[m], 'sections': {}}

out = open('cbc_part1 (sub_sections_only).html','w')
out.write(str(soup))

output = open('top_sections2.pkl','w')
pickle.dump(chp_dict,output)
output.close()	

# for each in chp_dict.keys():
# 	print each , chp_dict[each]['sections']
