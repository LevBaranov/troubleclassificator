#https://habr.com/post/332078/ - по образу статьи калякаем скрипт для набора словаря
import re
import porter

def get_dict(string):
	patern = re.compile(r"[\s\d$+<>№=;:,.()/#\[\]]")
	latin = 'a-z' 
	string = string.lower()
	words = patern.split(string)
	#print(words)
	for i, word in enumerate(words):
		#print(word)
		if(len(word)>2 and not re.match(r'[a-z]', word)):
			words[i] = porter.Porter().stem(word)
	dictionary = list(set(words))
	return dictionary
def sort_dict(l):
    n = []
    for i in l:
        if i not in n:
            n.append(i)
    return n

#get_dict('дключен через конечный к БМ uybh 123')

