from django.contrib import admin
from .models import Member

class MemberAdmin(admin.ModelAdmin):
  list_display = [f.name for f in Member._meta.fields]

admin.site.register(Member, MemberAdmin)

# Register your models here.
