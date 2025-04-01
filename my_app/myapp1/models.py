import os.path

from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.utils.translation import gettext_lazy as _


class Document(models.Model):
    file_path = models.FileField(upload_to='images/')
    size = models.IntegerField()

    def __str__(self):
        return f' file_path: {self.file_path}, size: {self.size}'

    def delete(self, *args, **kwargs):
        if os.path.isfile(self.file_path.path):
            os.remove(self.file_path.path)
        super().delete(*args, **kwargs)

    class Meta:
        db_table = 'docs'


class User_doc(models.Model):
    username = models.CharField(max_length=35)
    docs = models.ForeignKey(Document, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'username: {self.username},  docs_id: {self.docs}'

    class Meta:
        db_table = "users_to_docs"


class Price(models.Model):
    file_type = models.TextField()
    price = models.DecimalField(max_digits=20, decimal_places=3)

    def __str__(self):
        return f'file_type: {self.file_type}, price: {self.price}'

    class Meta:
        db_table = "price"


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    docs = models.ForeignKey(Document, on_delete=models.SET_NULL, null=True)
    order_price = models.DecimalField(max_digits=10, decimal_places=3)
    payment = models.BooleanField(default=False)

    def __str__(self):
        return f'user_id: {self.user},  docs_id: {self.docs},  order_price: {self.order_price},  payment: {self.payment}'

    class Meta:
        db_table = "cart"


