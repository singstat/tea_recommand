from django.contrib import admin
from .models import Entry, Tea, Company, TeaName



    
class TeaInline(admin.TabularInline): 
    model = Tea
    extra = 1 

class TeanameAdmin(admin.ModelAdmin):
    fields = ['name']
    inlines = [TeaInline]

class CompanyAdmin(admin.ModelAdmin):
    fields = ['name']
    
class TeaAdmin(admin.ModelAdmin):
    list_display = ('company','name', 'nation', 'region', 'color', 'status')
    #list_filter = (
    #        ('name', admin.RelatedOnlyFieldListFilter),
    #    )
    #inlines = [TeanameInline]

admin.site.register(TeaName, TeanameAdmin)

admin.site.register(Entry)
admin.site.register(Company)
admin.site.register(Tea, TeaAdmin)