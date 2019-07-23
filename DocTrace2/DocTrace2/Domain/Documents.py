import uuid
import sqlalchemy
import datetime

from DocTrace2.data.sqlalchemy_base import SqlAlchemyBase

class Document(SqlAlchemyBase):
    __tablename__ = 'Document'

    doc_id = sqlalchemy.Column(sqlalchemy.String,primary_key=True,
                               default=lambda: str(uuid.uuid4()))
    doc_name = sqlalchemy.Column(sqlalchemy.String)

    def to_dict(self):
        return {
            'doc_id': self.doc_id,
            'doc_name': self.doc_name,
        }
