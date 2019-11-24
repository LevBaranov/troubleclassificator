#!/usr/bin/env python3.7
#Для формирования словаря будем использовать уже имеющиеся заявка в ES.

import classifactor as clsf 
import logging
import random
import json
from elasticsearch import Elasticsearch, RequestsHttpConnection

def connect_elastic():
	#Подключение к БД
	_es = None
	_es = Elasticsearch(['http://tylo:80/es'])
	if _es.ping():
		print('Connect Established')
	else:
		print('Could not connect!')
	return _es
def search(es_object, index_name, search, size = 1):
	#Процедура поиска
	res = es_object.search(index=index_name, body=search, size=size)
	return res

if __name__ == '__main__':
	logging.basicConfig(level=logging.ERROR)
	es = connect_elastic()
	if es is not None:
		data_dict = {}
		index = 'tickets'
		size = 9999
		search_body = {"query": {"exists":{"field":"category"}}}
		results = search(es, index, json.dumps(search_body), size)
		ids =[]
		for hit in results['hits']['hits']:
			_id = hit['_id']
			ids.append(_id)
		for number in range(20):
			t_id = random.choice(ids)
			ticket = es.get(index = 'tickets', id = t_id)
			category = ticket['_source']['category']
			search_body = {
"query": {
    "bool": {
      "must": [
        {
          "match": {
            "ticket_id": t_id
          }
        },
        {
          "match": {
            "number": 0
          }
        },
        {
          "match": {
            "step_name": "Отправить администраторам активного оборудования"
          }
        }
      ]
    }
  }
}
			step = search(es, 'steps', json.dumps(search_body))
			print(t_id)
			total = step['hits']['total']
			if total == 1:
				info = step['hits']['hits'][0]['_source']['info']
				print(info)
				print(category)
				if data_dict.get(category) is not None:
					data_dict[category].append(info)
				else:
					data_dict[category] = [info]
		print(data_dict)
		my_file = open("data.json", "w")
		my_file.write(json.dumps(data_dict, ensure_ascii=False))
		my_file.close()
