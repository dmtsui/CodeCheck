from bs4 import BeautifulSoup
import urllib2
import re
import sqlite3

con = sqlite3.connect('cbc.db')
c = con.cursor()
c.execute('''DROP TABLE cbc_code ''')
c.execute('''CREATE TABLE IF NOT EXISTS cbc_code(id Integer PRIMARY KEY, name TEXT NOT NULL, description TEXT, link TEXT NOT NULL,
            content BLOB NOT NULL, children Text) ''')

lvl1 = []
lvl2 = []
lvl3 = []

href_match = re.compile('^javascript\:Next\(\'(?:\./)?st_ca_st_b200v10[^\.]*\.htm\'\)\;')
re_section = re.compile( '[A-Z]?[0-9]+(?:\.[0-9]+)*' )


def get_section(string):
    for each in string.split():
        if re_section.match(each):
               
            return each
            

def get_content(html):
    content = urllib2.urlopen(html)
    soup = BeautifulSoup(content)
    soup = soup.find(id="icc_body")
    title_desc = BeautifulSoup(str(soup.b)).get_text()
    children = []
    links = soup.find_all('a')

    title = get_section(title_desc)

    
    if len(links) > 0:
        for link in links:
            a = link.get_text()
            a = get_section(a)
            children.append(str(a))
            
    
    return unicode(soup), unicode(title), unicode(children), unicode(title_desc)

def all_links(html, tag_id):
    links = []
    content = urllib2.urlopen(html)

    soup = BeautifulSoup(content)
    toc = BeautifulSoup(str(soup.find(id=tag_id)))
    if toc:
        for link in toc.find_all('a'):
            h = link.get('href')
            if href_match.match(h):
                h = "http://publicecodes.cyberregs.com/st/ca/st/b200v10/"+h[17:-3]
                toc_i, title, children, description = get_content(h)          
                values =(title,description, h, toc_i, children,)
                if BeautifulSoup(toc_i).get_text() != u'\n':
                    c.execute('''INSERT INTO cbc_code(name,description, link, content, children) values(?,?,?,?,?)''',values)
                    links.append(values[2])
        con.commit()
        return links
        


lvl1 = all_links("http://publicecodes.cyberregs.com/st/ca/st/b200v10/index.htm", "icc_main_toc_contents")
for link in lvl1:
    lvl2 += all_links(link, "icc_main_toc_contents")

for link in lvl2:
    lvl3 += all_links(link, "icc_section_toc_contents")

print"done"
