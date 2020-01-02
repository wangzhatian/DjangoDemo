from django.contrib import admin
from product.models import Product
from apitest.models import Apistep,Apitest,Apis

class Apistepadmin(admin.TabularInline):
    list_display=["apiname","apiurl","apiparamvalue","apimethod","apiresult","apistatus","create_time","id","apitest"]
    model = Apistep
    extra = 1
class ApitestAdmin(admin.ModelAdmin):
    list_display=["apitestname","apitestdesc","apitester","apitestresult","create_time","id"]
    inlines = [Apistepadmin]
class ApisAdmin(admin.TabularInline):
    list_display=['apiname','apiurl','apiparamvalue','apimethod','apiresult','apistatus','create_time','id','product']

admin.site.register(Apitest,ApitestAdmin)
admin.site.register(Apis)
# Register your models here.
