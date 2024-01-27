from django.contrib import admin
from .models import Member


class MemberAdmin(admin.ModelAdmin):
    """class for showing the member sql in admin site in the folloing order"""
    list_display = ("firstname", "lastname", "joined_date")
  
admin.site.register(Member, MemberAdmin)


class ProdactAdmin(admin.ModelAdmin):
    """class for showing the prodact sql in admin site in the folloing order"""
    list_display = ("name", "price")
  