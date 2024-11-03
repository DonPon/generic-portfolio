# index/admin.py

from django.contrib import admin
from .models import PortfolioItem, Contact, Visitor, PersonalDetails, Skill

admin.site.register(PortfolioItem)
admin.site.register(Contact)
admin.site.register(Visitor)
admin.site.register(PersonalDetails)
admin.site.register(Skill)