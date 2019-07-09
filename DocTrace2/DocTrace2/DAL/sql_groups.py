import sqlite3
import os
import DocTrace2

class Groups:

    @classmethod
    def get_groups(cls):

        # source:  https://sebastianraschka.com/Articles/2014_sqlite_in_python_tutorial.html

        working_folder = os.path.dirname(DocTrace2.__file__)
        file = os.path.join(working_folder,'db','myDocuments.sqlite')
        conn_string = 'sqlite:///' + file

        conn = sqlite3.connect(file)
        c = conn.cursor()
        c.execute('SELECT * FROM Groups')

        all_rows = c.fetchall()
        print('1):', all_rows)

        conn.close()

        return all_rows


    @classmethod
    def get_group(cls,group_id):

        # source:  https://sebastianraschka.com/Articles/2014_sqlite_in_python_tutorial.html

        working_folder = os.path.dirname(DocTrace2.__file__)
        file = os.path.join(working_folder,'db','myDocuments.sqlite')
        conn_string = 'sqlite:///' + file

        conn = sqlite3.connect(file)
        c = conn.cursor()
        c.execute('SELECT * FROM Groups where Group_id = {}'.format(group_id))

        all_rows = c.fetchall()
        print('1):', all_rows)

        conn.close()

        return all_rows


    @classmethod
    def create_group(cls,task):
        working_folder = os.path.dirname(doctrace.__file__)
        file = os.path.join(working_folder,'db','myDocuments.sqlite')
        conn_string = 'sqlite:///' + file

        conn = sqlite3.connect(file)


        sql = ''' INSERT INTO Groups(group_name,doc_id,section_id)
                   VALUES(?,?,?) '''
        cur = conn.cursor()
        cur.execute(sql, task)
        return cur.lastrowid


