from DocTrace2.DAL.sql_documents import documents
from DocTrace2.Domain.Documents import Document
from DocTrace2.DAL.Documents import DAL_Documents
from DocTrace2.viewmodels.create_document_viewodel import CreateDocumentViewModel
from DocTrace2.viewmodels.update_document_viewmodel import UpdateDocumentViewModel

class BLL_Documents:

    @classmethod
    def get_documents(cls):

        my_documents = DAL_Documents.all_documents(limit=25)

        return my_documents

    @classmethod
    def single_document(cls,doc_id):
        doc = DAL_Documents.doc_by_id(doc_id=doc_id)

        return doc

    @classmethod
    def create_document(cls,doc_data):

        # TODO: Validate
        vm = CreateDocumentViewModel(doc_data)
        vm.compute_details()
        if vm.errors:
            return "400 " + vm.error_msg

        try:
            Document = DAL_Documents.add_document(vm.Document)
            # return Response(status=201, json_body=Document.to_dict())
            return "201 " + Document.doc_id
        except Exception as x:
            # return Response(status=400, body='Could not save car.')
            return "400 " + "Could not save document."

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
