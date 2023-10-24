# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2023/12/4 10:41
@description  向量数据库

连接并写入向量数据：https://cloud.tencent.com/document/product/1709/95102
"""


def create_database(url, key):
    """
    创建数据库
    通过 VectorDBClient() 创建一个向量数据库的客户端对象，并通过 create_database()  创建数据库 db-test。
    """

    import tcvectordb
    from tcvectordb.model.enum import FieldType, IndexType, MetricType, ReadConsistency

    client = tcvectordb.VectorDBClient(url=url, username='root', key=key,
                                       read_consistency=ReadConsistency.EVENTUAL_CONSISTENCY, timeout=30)
    db = client.create_database(database_name='db-test')
    print(db.database_name)


def create_collection(url, key):
    """
    创建集合
    设置索引参数，通过接口 create_collection() 创建一个名为 book-vector 的集合，用于写入 3 维向量数据。
    """
    import tcvectordb
    from tcvectordb.model.enum import FieldType, IndexType, MetricType, EmbeddingModel
    from tcvectordb.model.index import Index, VectorIndex, FilterIndex, HNSWParams
    from tcvectordb.model.enum import FieldType, IndexType, MetricType, ReadConsistency

    client = tcvectordb.VectorDBClient(url=url, username='root', key=key,
                                       read_consistency=ReadConsistency.EVENTUAL_CONSISTENCY, timeout=30)

    db = client.database('db-test')
    # -- index config
    # 第一步，设计索引（不是设计 Collection 的结构）
    # 1. 【重要的事】向量对应的文本字段不要建立索引，会浪费较大的内存，并且没有任何作用。
    # 2. 【必须的索引】：主键id、向量字段 vector 这两个字段目前是固定且必须的，参考下面的例子。
    # 3. 【其他索引】：检索时需作为条件查询的字段，比如要按书籍的作者进行过滤，这个时候 author 字段就需要建立索引，
    #     否则无法在查询的时候对 author 字段进行过滤，不需要过滤的字段无需加索引，会浪费内存；
    # 4.  向量数据库支持动态 Schema，写入数据时可以写入任何字段，无需提前定义，类似 MongoDB.
    # 5.  例子中创建一个书籍片段的索引，例如书籍片段的信息包括 {id, vector, bookName, author，},
    #     id 为主键需要全局唯一，vector 字段需要建立向量索引，假如我们在查询的时候要查询指定书名称的内容，这个时候需要对 bookName 建立索引，其他字段没有条件查询的需要，无需建立索引。
    index = Index(
        FilterIndex(name='id', field_type=FieldType.String, index_type=IndexType.PRIMARY_KEY),
        FilterIndex(name='author', field_type=FieldType.String, index_type=IndexType.FILTER),
        FilterIndex(name='bookName', field_type=FieldType.String, index_type=IndexType.FILTER),
        VectorIndex(name='vector', dimension=3, index_type=IndexType.HNSW,
                    metric_type=MetricType.COSINE, params=HNSWParams(m=16, efconstruction=200))
    )
    # create a collection
    # 第二步，创建 Collection
    coll = db.create_collection(
        name='book-vector',
        shard=1,
        replicas=0,
        description='this is a collection of test embedding',
        index=index
    )
    print(vars(coll))


def upsert_data(url, key):
    """
    插入数据
    通过接口 upsert() 为集合 book-vector 写入向量数据。其中，参数 id 为写入的文档 ID，参数 vector 为写入的向量数据， build_index 配置是否在写入数据时创建索引。
    """
    import tcvectordb
    from tcvectordb.model.collection import UpdateQuery
    from tcvectordb.model.document import Document, SearchParams, Filter
    from tcvectordb.model.enum import FieldType, IndexType, MetricType, ReadConsistency
    from tcvectordb.model.index import Index, VectorIndex, FilterIndex, HNSWParams

    # create a database client object
    client = tcvectordb.VectorDBClient(url=url, username='root', key=key,
                                       read_consistency=ReadConsistency.EVENTUAL_CONSISTENCY, timeout=30)
    # 指定写入数据的数据库与集合
    db = client.database('db-test')
    coll = db.collection('book-vector')

    # 写入数据，可能存在一定延迟
    # 1. 支持动态 Schema，除了 id、vector 字段必须写入，可以写入其他任意字段；
    # 2. upsert 会执行覆盖写，若文档id已存在，则新数据会直接覆盖原有数据(删除原有数据，再插入新数据)
    # 3. 参数 build_index 为 True，指写入数据同时重新创建索引。
    res = coll.upsert(
        documents=[
            Document(id='1', vector=[
                0.2123, 0.23, 0.213], author='罗贯中', bookName='三国演义', page=21),
            Document(id='2', vector=[
                0.2123, 0.22, 0.213], author='吴承恩', bookName='西游记', page=22),
            Document(id='3', vector=[
                0.2123, 0.21, 0.213], author='曹雪芹', bookName='红楼梦', page=23)
        ],
        build_index=True
    )
    print(res)


def query_data(url,key):
    """
    检索数据
    精确查询是基于标量字段进行精确查找的检索方式。向量数据库支持根据 Document Id 进行精确查询。
    """
    import tcvectordb
    from tcvectordb.model.enum import FieldType, IndexType, MetricType, ReadConsistency
    from tcvectordb.model.index import Index, VectorIndex, FilterIndex, HNSWParams
    from tcvectordb.model.document import Document, Filter, SearchParams

    # create a database client object
    client = tcvectordb.VectorDBClient(url=url, username='root',key=key,
                                       read_consistency=ReadConsistency.EVENTUAL_CONSISTENCY, timeout=30)

    db = client.database('db-test')
    coll = db.collection('book-vector')

    # 1. query 用于查询数据
    # 2. 可以通过传入主键 id 列表或 filter 实现过滤数据的目的
    # 3. 如果没有主键 id 列表和 filter 则必须传入 limit 和 offset，类似 scan 的数据扫描功能
    # 4. 如果仅需要部分 field 的数据，可以指定 output_fields 用于指定返回数据包含哪些 field，不指定默认全部返回

    filter_param = Filter(Filter.In("bookName", ["三国演义", "西游记"]))
    # query
    doc_list = coll.query(document_ids=['0001', '0002', '0003'], retrieve_vector=True, filter=filter_param, limit=3,
                          offset=0, output_fields=['bookName', 'author'])

    for doc in doc_list:
        print(doc)


if __name__ == '__main__':
    # @todo：合并前删除
    url = 'http://lb-o9mp6ani-ybuviqwhknaz7tgj.clb.ap-guangzhou.tencentclb.com:10000'
    key = 's5tsNRrCX9EJyNFiiSbUWnBt80QCsZdwLLapk4wd'

    # create_database(url=url, key=key)
    # create_collection(url=url, key=key)
    # upsert_data(url=url, key=key)
    query_data(url=url, key=key)
