import sys
import csv
import os
import random

from dateutil.parser import parse

from DocTrace2.data.db_factory import DbSessionFactory
from DocTrace2.Domain.Document import Document

class DAL_Documents:
    __document_data = {}

    @classmethod
    def all_documents(cls,limit=None):
        session = DbSessionFactory.create_session()
        query = session.query(Document)

        if limit:
            documents = query[:limit]
        else:
            documents = query.all()

        session.close()

        return documents


    @classmethod
    def doc_by_id(cls, doc_id):
        session = DbSessionFactory.create_session()
        document = session.query(Document).filter(Document.doc_id == doc_id).first()
        session.close()

        return document

    @classmethod
    def add_document(cls, doc):
        try:
            session = DbSessionFactory.create_session()

            db_doc = Document()
            db_doc.doc_id = doc.doc_id
            db_doc.doc_name = doc.doc_name

            session.add(db_doc)
            session.commit()

            return db_doc

        except Exception as e:
            print (e)

    @classmethod
    def update_document(cls, doc_data):
        session = DbSessionFactory.create_session()

        db_doc = session.query(Document).filter(Document.doc_id == doc_data.doc_id).first()
        db_doc.doc_name = doc_data.doc_name

        session.commit()

        return db_doc


    @classmethod
    def delete_document(cls, doc_id):
        session = DbSessionFactory.create_session()
        db_doc = session.query(Document).filter(Document.doc_id == doc_id).first()

        if not db_doc:
            return

        session.delete(doc_id)
        session.commit()


