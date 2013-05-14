from bs4 import BeautifulSoup
import re


re_section = re.compile( '[A-Z]?[0-9]+[A-Z]?(?:\.[0-9]+)*' )
re_page = re.compile("p[0-9]+")

# soup.a with r'p[0-9]+'
#

def get_section(string):
        all_split = string.split()
        sections = []
        
        for each in all_split:
                if re_section.match(each):
                        sections.append(each)
        for section in sections:
                all_split.remove(section)
        return " ".join(all_split), sections

f = open("cbc_part2(clean_up).html").read()

out = open("cbc_part2(clean_up)2.html",'w')


#soup the text
soup = BeautifulSoup(f)

for each in soup.find_all('p',attrs={'class':'b'}):
    each.contents[0].wrap(soup.new_tag('b'))

# Sectionm, Tables, Figures
out.write(str(soup))

print 'done'
