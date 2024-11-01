# index/admin.py

from django.contrib import admin
from .models import PortfolioItem, Contact, Visitor, PersonalDetails

admin.site.register(PortfolioItem)
admin.site.register(Contact)
admin.site.register(Visitor)
admin.site.register(PersonalDetails)