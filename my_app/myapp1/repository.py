from django.core.exceptions import ObjectDoesNotExist
from .models import Document, User_doc
from .my_funk import trans_b_in_kb
from django.contrib.auth.models import User

class DocumentRepository:
    @classmethod
    def create_document(cls, upload_file, user_email):
        document = Document.objects.create(
            file_path=upload_file,
            size=trans_b_in_kb(upload_file.size)
        )

        User_doc.objects.create(
            username=user_email,
            docs=document
        )
        return document

    @classmethod
    def delete_document(cls, doc_id):
        try:
            document = Document.objects.get(id=doc_id)
            User_doc.objects.filter(docs=document).delete()
            document.delete()
            return True
        except ObjectDoesNotExist:
            return False

    @classmethod
    def get_document_by_id(cls, doc_id):
        try:
            return Document.objects.get(id=doc_id)
        except ObjectDoesNotExist:
            return None


class UserRepository:
    @classmethod
    def get_user_by_email(cls, email):
        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            return None

    @classmethod
    def create_user(cls, email, password):
        return User.objects.create_user(
            username=email,
            email=email,
            password=password
        )