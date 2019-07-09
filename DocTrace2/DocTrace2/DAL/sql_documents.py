import sqlite3
import os
import DocTrace2

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
        print('1):', all_rows)

        conn.close()

        return all_rows


    @classmethod
    def create_document(cls,task):
        working_folder = os.path.dirname(DocTrace2.__file__)
        file = os.path.join(working_folder,'db','myDocuments.sqlite')
        conn_string = 'sqlite:///' + file

        conn = sqlite3.connect(file)


        sql = ''' INSERT INTO Documents(doc_name)
                   VALUES(?) '''
        cur = conn.cursor()
        cur.execute(sql, task)
        return cur.lastrowid


