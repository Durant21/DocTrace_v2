from DocTrace2.BLL.Groups import BLL_Groups
from DocTrace2.BLL.Documents import BLL_Documents
from DocTrace2.Domain.Document import Document

def test_call_groups():
   r = BLL_Groups.get_groups()
   return r

def test_call_documents():
   r = BLL_Documents.get_documents()
   return r

def test_doc():
   # doc = Document('','')
   # doc.__init__('','')
   doc = Document()
   doc.add_name('a doc')
   print(doc.doc_name)
   return doc


def main():
    (test_call_groups())
    test_call_documents()
    (test_doc())

if __name__ == "__main__":
    main()


