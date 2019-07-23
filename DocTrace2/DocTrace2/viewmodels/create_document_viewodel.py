from DocTrace2.Domain.Documents import Document

from DocTrace2.viewmodels.base_viewmodel import ViewModelBase

class CreateDocumentViewModel(ViewModelBase):
    def __init__(self, data_dict):
        super().__init__()
        self.data_dict = data_dict
        self.Document = None

    def compute_details(self):
        doc_id = self.data_dict.get('doc_id')
        doc_name = self.data_dict.get('doc_name')

        if not doc_name:
            self.errors.append("doc name is a required field.")

        if not self.errors:
            doc = Document(
                doc_id=doc_id,
                doc_name=doc_name
            )
            self.Document = doc


