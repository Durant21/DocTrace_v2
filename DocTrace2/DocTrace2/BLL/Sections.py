from DocTrace2.DAL.sql_sections import Sections


class BLL_Sections:

    @classmethod
    def get_sections(cls):

        my_section = Sections.get_sections()

        return my_section

    @classmethod
    def create_section(cls):
        # ( section_id, doc_text, date_in)

        doc_text = 'abc'
        date_in = '2015-01-01'
        task = (doc_text,date_in)
        doc_id = 1
        new_section_id = Sections.create_section(task)

        return new_section_id