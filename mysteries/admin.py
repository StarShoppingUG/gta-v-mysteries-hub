from django.contrib import admin
from .models import Theory, CheatCode, Developer

    
# Register models
admin.site.register(Developer)
admin.site.register(CheatCode)
admin.site.register(Theory)