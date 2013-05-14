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

f = open("cbc_part2.html").read()

out = open("cbc_part2(clean_up).html",'w')

ulist = ['&#931;', '&#60;', '&#958;', '&#8211;', '&#167;',
         '&#62;', '&#916;', '&#175;', '&#177;', '&#8242;',
         '&#961;', '&#38;', '&#184;', '&#8224;', '&#964;',
         '&#190;', '&#945;', '&#216;', '&#920;', '&#932;',
         '&#935;', '&#934;', '&#821;', '&#8249;', '&#949;',
         '&#963;', '&#248;', '&#8805;', '&#8727;', '&#188;',
         '&#178;', '&#8200;', '&#969;', '&#8243;', '&#8212;',
         '&#229;', '&#913;', '&#8221;', '&#34;', '&#176;',
         '&#215;', '&#39;', '&#956;', '&#966;', '&#952;',
         '&#8722;', '&#8220;', '&#181;', '&#160;', '&#957;',
         '&#35;', '&#960;', '&#946;', '&#183;', '&#402;',
         '&#8260;', '&#937;', '&#948;', '&#8217;', '&#8804;',
         '&#189;', '&#8730;']

#replace unicode characters with s
for u in ulist:
    f.replace(u,' ')

print 'unicode extracted'

#soup the text
soup = BeautifulSoup(f)

print 'soup'
#remove all divs in the soup
for a in soup.find_all('div'):
    a.unwrap()
print 'div unwrapped'
#remove all links to pages
for b in soup.find_all('a',attrs={'name':re_page}):
    b.decompose()

#remove blockquote
for c in soup.find_all('blockquote'):
    c.unwrap()
print 'blockquote done'

#remove span
for d in soup.find_all('span'):
    d.extract()
print 'span done'

#remove i
for e in soup.find_all('i'):
        e.unwrap()

for f in soup.find_all('br'):
        f.extract()


for each in soup.find_all('p',attrs={'class':'b'}):
        if each.string is None:
                each.extract()
        else:
                each.contents[0].wrap(soup.new_tag('b'))

# Sectionm, Tables, Figures
out.write(str(soup))

print 'done'
