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
def search(es_object, index_name, search, size):
	#Процедура поиска
	res = es_object.search(index=index_name, body=search, size=size)
	return res

"""
if __name__ == '__main__':
	logging.basicConfig(level=logging.ERROR)
	es = connect_elastic()
	if es is not None:
		index = 'steps'
		size = 9999
		search_body = {'query': { 'match': { 'step_name': { 'query': 'Отправить администраторам активного оборудования'}}}}
		results = search(es, index, json.dumps(search_body), size)
		diction = []
		for hit in results['hits']['hits']:
			source = hit['_source']
			info = source['info']
			print(info)
			diction.extend(clsf.get_dict(info))
		#res = result[_source]
	diction = clsf.sort_dict(diction)
	print(diction)
"""
if __name__ == '__main__':
	logging.basicConfig(level=logging.ERROR)
	es = connect_elastic()
	if es is not None:
		index = 'tickets'
		size = 9999
		search_body = {"query": {"exists":{"field":"category"}}}
		results = search(es, index, json.dumps(search_body), size)
		ids =[]
		for hit in results['hits']['hits']:
			_id = hit['_id']
			ids.append(_id)
		random.choice(ids)
