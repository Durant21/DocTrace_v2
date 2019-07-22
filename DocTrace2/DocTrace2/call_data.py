# from DocTrace2.BLL.Groups import BLL_Groups
from DocTrace2.BLL.Documents import BLL_Documents
from DocTrace2.Domain.Document import Document
from DocTrace2.data.db_factory import DbSessionFactory

# def test_call_groups():
#    r = BLL_Groups.get_groups()
#    return r
#
# def test_call_documents():
#    r = BLL_Documents.get_documents()
#    return r
#
# def test_doc():
#    # doc = Document('','')
#    # doc.__init__('','')
#    doc = Document()
#    doc.add_name('a doc')
#    print(doc.doc_name)
#    return doc
#
# def test_create_doc(doc_name):
#     r = BLL_Documents.create_document(doc_name=doc_name)
#     print(r)
#
def test_update_doc(doc_name):
    doc_data = {"doc_id": "1001","doc_name": "changed name"}
    r = BLL_Documents.update_document(doc_id='1001',doc_data=doc_data)
    print(r)


def main():
    DbSessionFactory.global_init('myDocuments.sqlite')
    # (test_call_groups())
    # test_call_documents()
    # (test_doc())
    # test_create_doc('abc')
    test_update_doc('abc')

if __name__ == "__main__":
    main()


