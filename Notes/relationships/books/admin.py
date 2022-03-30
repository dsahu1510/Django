from django.contrib import admin
# from .models import Publication, Article

# # Register your models here.
# admin.site.register(Publication)
# admin.site.register(Article)

from .models import Place, Restaurant, Waiter
admin.site.register(Place)
admin.site.register(Restaurant)
admin.site.register(Waiter)
