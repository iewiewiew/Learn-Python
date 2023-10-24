# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2023/10/24 14:56
@description  ES 基本操作
pip install elasticsearch
"""

from elasticsearch import Elasticsearch


class ElasticsearchClient:
    def __init__(self, host='localhost', port=9200):
        self.host = host
        self.port = port
        self.client = Elasticsearch([{'host': self.host, 'port': self.port}])

    def create_index(self, index_name):
        self.client.indices.create(index=index_name)

    def index_document(self, index_name, document):
        self.client.index(index=index_name, body=document)

    def search_documents(self, index_name, query):
        response = self.client.search(index=index_name, body=query)
        return response['hits']['hits']

    def delete_index(self, index_name):
        self.client.indices.delete(index=index_name)


if __name__ == '__main__':
    # 示例用法
    es = ElasticsearchClient('localhost', 9200)

    index_name = 'my_index'

    # 创建索引
    es.create_index(index_name)

    # 添加文档
    document = {
        'title': 'Example Document',
        'content': 'This is an example document for Elasticsearch.'
    }
    es.index_document(index_name, document)

    # 查询文档
    query = {
        'query': {
            'match': {
                'content': 'example'
            }
        }
    }
    results = es.search_documents(index_name, query)
    for result in results:
        print(result['_source'])

    # 删除索引
    # es.delete_index(index_name)
