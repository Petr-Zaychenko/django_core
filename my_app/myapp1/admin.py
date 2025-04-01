from django.contrib import admin
from myapp1.models import Document, User_doc, Cart, Price

## можно так: но тогда никаких кастомизаций!
# admin.site.register(Document, User_doc, Cart, Price)


admin.site.register(Document)
admin.site.register(User_doc)
admin.site.register(Cart)
admin.site.register(Price)
