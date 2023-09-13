from django.contrib import admin
from .models import Tag
from .models import Tematic
from .models import Product
# Register your models here.
admin.site.register(Tag)
admin.site.register(Tematic)
admin.site.register(Product)