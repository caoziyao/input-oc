# coding: utf-8




class BulkWriteOperation(object):

    def __init__(self, builder, selector, is_upsert=False):
        self.builder = builder
        self.selector = selector
        self.is_upsert = is_upsert



class BulkOperationBuilder(object):


    def __init__(self, collection, ordered=False):
        self.collection = collection
        self.ordered = ordered
        self.results = []
        self.executors = []
        self.done = False
        self._isert_returns_nModified = True
        self._update_return_nModified = True


    def find(self, selector):
        return BulkWriteOperation(self, selector)