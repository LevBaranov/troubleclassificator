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
def get_token(word):
	patern = re.compile(r"[\s\d$+<>№=;:,.()/#\[\]]")
	latin = 'a-z'
	word = patern.split(word.lower())
	token = porter.Porter().stem(word)
	return token
#get_dict('дключен через конечный к БМ uybh 123')
#token = get_token('Не работает ПД, по EQM привязки нет, по адресу УК нет, клиент со своей стороны оборудование проверил, клиент уточнил МАСи которые должны видить в канале 00-25-45-87-b0-89. Телефон: (89065438200).')
#print(token)
