from bs4 import BeautifulSoup
import re
import pickle

#K109.1

re_section = re.compile( '[A-Z]?[0-9]+[A-Z]?(?:\.[0-9]+)*' )

f = open('cbc_part1(sub_sections_only).html').read()

soup = BeautifulSoup(f)

sub_sections = {}
current_section = None

#gets rid of the empty p tags
empty_tags = soup.findAll(lambda tag: tag.name == 'p' and not tag.contents and (tag.string is None or not tag.string.strip()))
[empty_tag.extract() for empty_tag in empty_tags]

for each in soup.body.find_all('ol', recursive = False):
	each.wrap(soup.new_tag("p"))

for each in soup.body.find_all('p', recursive = False):
	if each.b and len(each.b) > 0:
		tmp = re.split(' ', each.b.contents[0], 1)
		if  re_section.match(tmp[0]):
			current_section = tmp[0]
			print current_section
			if len(tmp) ==2:
				sub_sections[current_section] ={'name':tmp[1], 'content': str(each)}
			else:
				sub_sections[current_section] ={'name':'', 'content': str(each)}
		else:
			print current_section
			sub_sections[current_section]['content'] += str(each)

	else:
		print current_section
		sub_sections[current_section]['content'] += str(each)

output = open('sub_sections.pkl','w')
pickle.dump(sub_sections,output)
output.close()	




