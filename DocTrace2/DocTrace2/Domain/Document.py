class Document:
    def __init__(self):
        self.doc_id = 0
        self.doc_name = ''

    def add_name(self, name):
        self.doc_name = name

    def add_id(self, id):
        self.doc_id = id

    def to_dict(self):
        return {
            'doc_id': self.doc_id,
            'doc_name': self.doc_name,
        }
