from django.contrib import admin
from product.models import Product
from apitest.models import Apitest,Apis
from webtest.models import Webcase
# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["productname","productdesc","producter","create_time","id"]#控制展示时候的显示
    def ready(self):
        pass
class ApisAdmin(admin.TabularInline):
    list_display =['apiname','apiurl','apiparamvalue','apimethod','apiresult','apistatus','create_time','id','product']
    model = Apis
    extra = 1

from apptest.models import Appcase
class ApcaseAdmin(admin.TabularInline):
    list_display = ['apcasename', 'aptestresult','create_time','id','product']
    model = Appcase
    extra = 1

class WebcaseAdmin(admin.TabularInline):

    list_display = ['webcasename', 'webtestresult','create_time','id','product']

    model = Webcase

    extra = 1

# class ProductAdmin(admin.ModelAdmin):
#     list_display = ['productname', 'productdesc','create_time','id']
#     inlines = [ApcaseAdmin]


# admin.site.register(Product)#把产品模块注册到Django admin后台并能显示
