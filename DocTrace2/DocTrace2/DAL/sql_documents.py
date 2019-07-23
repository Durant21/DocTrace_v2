import sqlite3
import os
import DocTrace2
from DocTrace2.Domain.Documents import Document

class documents:

    @classmethod
    def get_documents(cls):

        # source:  https://sebastianraschka.com/Articles/2014_sqlite_in_python_tutorial.html

        working_folder = os.path.dirname(DocTrace2.__file__)
        file = os.path.join(working_folder,'db','myDocuments.sqlite')
        conn_string = 'sqlite:///' + file

        # conn = sqlite3.connect('example.db')
        # conn = sqlite3.connect(conn_string)


        conn = sqlite3.connect(file)
        c = conn.cursor()
        c.execute('SELECT * FROM Documents')

        all_rows = c.fetchall()
        all_rows2 = c.description
        print('1):', all_rows)

        lst_documents = []

        for r in all_rows:
            print(r[1])
            aDoc = Document()
            aDoc.doc_id = r[0]
            aDoc.doc_name = r[1]

            lst_documents.append(aDoc)

        conn.close()

        return lst_documents

    @classmethod
    def create_document(cls,task):
        working_folder = os.path.dirname(DocTrace2.__file__)
        file = os.path.join(working_folder,'db','myDocuments.sqlite')
        conn_string = 'sqlite:///' + file

        conn = sqlite3.connect(file)


        sql = '''INSERT INTO Documents(doc_name) VALUES(?);'''
        cur = conn.cursor()
        cur.execute(sql, task)
        return cur.lastrowid

    @classmethod
    def update_document(cls,task):
        working_folder = os.path.dirname(DocTrace2.__file__)
        file = os.path.join(working_folder,'db','myDocuments.sqlite')
        conn_string = 'sqlite:///' + file

        conn = sqlite3.connect(file)


        sql = '''UPDATE Documents SET doc_name = (?) WHERE doc_id = (?);'''
        cur = conn.cursor()
        cur.execute(sql, task)
        return cur.lastrowid
