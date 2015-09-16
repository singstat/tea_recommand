from django.contrib import admin
from .models import Entry
from .models import Tea

from .models import Company

from .models import TeaName

admin.site.register(TeaName)
admin.site.register(Company)

admin.site.register(Tea)
admin.site.register(Entry)
# Register your models here.
