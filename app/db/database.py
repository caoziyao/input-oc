# coding: utf-8


class Database(object):

    def __init__(self, client):
        self._client = client


    @property
    def client(self):
        return self._client






