from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .repository import DocumentRepository, UserRepository
from .models import Document

class AuthService:
    @staticmethod
    def login_user(request, username, password):
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user=user)
            return True
        return False

    @staticmethod
    def register_user(request, email, password, password2):
        if password != password2:
            messages.error(request, 'Пароли не совпадают!')
            return None

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Пользователь с таким email уже существует!')
            return None

        try:
            user = User.objects.create_user(
                username=email,
                email=email,
                password=password
            )
            messages.success(request, 'Регистрация прошла успешно!')
            return user
        except Exception as e:
            messages.error(request, f'Ошибка при регистрации: {str(e)}')
            return None

class FileService:
    @staticmethod
    def get_all_files():
        return Document.objects.all()

    @staticmethod
    def add_file(upload_file, request):
        DocumentRepository.create_document(upload_file, request.user.email)

    @staticmethod
    def delete_file(file_id):
        return DocumentRepository.delete_document(file_id)