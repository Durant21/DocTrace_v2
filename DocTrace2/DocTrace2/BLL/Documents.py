from DocTrace2.DAL.sql_documents import documents
from DocTrace2.Domain.Document import Document
from DocTrace2.DAL.Documents import DAL_Documents
from DocTrace2.viewmodels.create_document_viewodel import CreateDocumentViewModel
from DocTrace2.viewmodels.update_document_viewmodel import UpdateDocumentViewModel

class BLL_Documents:
#
#     @classmethod
#     def get_documents(cls):
#
#         my_documents = documents.get_documents()
#
#         return my_documents
#
#     @classmethod
#     def create_document(cls,doc_name):
#         # ( doc_name)
#
#         # doc_name = 'a doc name'
#         task = [doc_name]
#         new_document_id = documents.create_document(task)
#
#         return new_document_id
#
#     @classmethod
#     def update_document_sql(cls,doc_name):
#         # ( doc_name)
#
#         # doc_name = 'a doc name'
#         task = [doc_name,3]
#         new_document_id = documents.update_document(task)
#
#         return new_document_id

    @classmethod
    def update_document(cls,doc_id,doc_data): # (int,json_body)

        # get the document object by doc_id
        doc = DAL_Documents.doc_by_id(doc_id)

        if not doc:
            msg = "404 The document with id '{}' was not found.".format(doc_id)
            return msg

        # Validate
        vm = UpdateDocumentViewModel(doc_data,doc_id)
        vm.compute_details()
        if vm.errors:
            return "400 " + vm.error_msg
        try:
            DAL_Documents.update_document(vm.Document)
            return "204 Document updated successfully."
        except:
            return "400 Could not update document."
