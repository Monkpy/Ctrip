import pymongo


class Mongodb(object):

    def __init__(self):
        self.host = ''
        self.mongodb = 'Ctrip'  # 库
        self.mongo_table = 'hotel'  # 集合
        self.client = pymongo.MongoClient(host=self.host, port=27017)  # 建立连接

        self.db = self.client[self.mongodb]  # 操作库
        self.tb = self.db[self.mongo_table]  # 操作集合

    def save_mongo(self, hk):
        self.tb.insert_one(hk)
        '''
        db.集合名.update(criteria, objNew, upsert, mult) 
        criteria: 需要被更新的条件表达式 
        objNew: 更新表达式 
        upsert: 如目标记录不存在，是否插入新文档。 
        multi: 是否更新多个文档。
        '''


if __name__ == '__main__':
    mongodb = Mongodb()

