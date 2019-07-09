import sqlite3
import os
import DocTrace2

class Sections:

    @classmethod
    def get_sections(cls):

        # source:  https://sebastianraschka.com/Articles/2014_sqlite_in_python_tutorial.html

        working_folder = os.path.dirname(DocTrace2.__file__)
        file = os.path.join(working_folder,'db','myDocuments.sqlite')
        conn_string = 'sqlite:///' + file

        # conn = sqlite3.connect('example.db')
        # conn = sqlite3.connect(conn_string)


        conn = sqlite3.connect(file)
        c = conn.cursor()
        c.execute('SELECT * FROM sections')

        all_rows = c.fetchall()
        print('1):', all_rows)

        conn.close()

        return all_rows

    @classmethod
    def get_section(cls,section_id):

        # source:  https://sebastianraschka.com/Articles/2014_sqlite_in_python_tutorial.html

        working_folder = os.path.dirname(DocTrace2.__file__)
        file = os.path.join(working_folder,'db','myDocuments.sqlite')
        conn_string = 'sqlite:///' + file

        # conn = sqlite3.connect('example.db')
        # conn = sqlite3.connect(conn_string)


        conn = sqlite3.connect(file)
        c = conn.cursor()
        c.execute('SELECT * FROM sections where section_id = {}'.format(section_id))
        all_rows = c.fetchall()
        print('1):', all_rows)

        conn.close()

        return all_rows

    @classmethod
    def create_section(cls,task):
        working_folder = os.path.dirname(DocTrace2.__file__)
        file = os.path.join(working_folder,'db','myDocuments.sqlite')
        conn_string = 'sqlite:///' + file

        conn = sqlite3.connect(file)


        sql = ''' INSERT INTO Sections(doc_text, date_in)
                   VALUES(?,?) '''
        cur = conn.cursor()
        cur.execute(sql, task)
        return cur.lastrowid


