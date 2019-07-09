from DocTrace2.DAL.sql_documents import documents


class BLL_Documents:

    @classmethod
    def get_documents(cls):

        my_documents = documents.get_documents()

        return my_documents

    @classmethod
    def create_document(cls):
        # ( doc_name)

        doc_name = 'a doc name'
        task = (doc_name)
        new_document_id = documents.create_document(task)

        return new_document_id