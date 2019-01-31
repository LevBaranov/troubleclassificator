#https://habr.com/post/332078/ - по образу статьи калякаем скрипт для набора словаря
import re
import porter


text = 'Необходимо найти последовательность 12 задач'
patern = re.compile(r"[\s\d$+<>№=;:,.]") 
string = text.lower()
words = patern.split(string)
print(words)
for i, word in enumerate(words):
    if(len(word)>0):
        words[i] = porter.Porter().stem(word)
        
dictionary = list(set(words))
print(dictionary)
