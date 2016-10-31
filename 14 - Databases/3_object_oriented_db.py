class Database:
    def __init__(self, file_name, table_name):
        self._properties = dict()
        self._properties['file_name'] = file_name
        self._properties['table_name'] = table_name

    @property
    def file_name(self):
        return self._properties.get('file_name', None)

    @file_name.setter
    def file_name(self, name):
        self._properties['file_name'] = name

    @file_name.deleter
    def file_name(self):
        del self._properties['file_name']

    @property
    def table_name(self):
        return self._properties.get('table_name', None)

    @table_name.setter
    def table_name(self, name):
        self._properties['table_name'] = name

    @table_name.deleter
    def table_name(self):
        del self._properties['table_name']
