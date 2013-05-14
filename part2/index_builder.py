import urllib2
import re
import sqlite3
from bs4 import BeautifulSoup
import pickle

re_section = re.compile( '[A-Z]?[0-9]+[A-Z]?(?:\.[0-9]+)*' )

def get_section(string):
        all_split = string.split()
        sections = []
        
        for each in all_split:
                if re_section.match(each):
                        sections.append(each)
        for section in sections:
                all_split.remove(section)
        return " ".join(all_split), sections


f = open("code_index.html").read()

content = BeautifulSoup(f)

p = content.find_all('p')

current = ""

index = {}

for each in p:
        if each.get('class')[0] == "index1":
                temp = each.get_text()
                name, sections = get_section(temp)
                current = name
                index[current] = {current:sections}

        elif each.get('class')[0] == "index2":
                temp = each.get_text()
                name, sections = get_section(temp)
                index[current][name] = sections
        else:
                pass

pickle.dump(index, open("index.p","wb"))
print "done"

