#https://habr.com/post/332078/ - по образу статьи калякаем скрипт для набора словаря
import re
import porter

def get_dict(strings):
	text = 'Необходимо найти последовательность 12 задач'
	patern = re.compile(r"[\s\d$+<>№=;:,.]") 
	string = strings.lower()
	words = patern.split(string)
	#print(words)
	for i, word in enumerate(words):
    		if(len(word)>0):
        		words[i] = porter.Porter().stem(word)
        
	dictionary = list(set(words))
	return dictionary

result = create_string(' подключен через БМ18 EoIP 855_Telros конечный 10.188.112.174 Шел')

