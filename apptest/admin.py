from django.contrib import admin

# Register your models here.
from django.contrib import admin
from apptest.models import Appcase,Appcasestep

class ApcasetepAdmin(admin.TabularInline):
    list_display=['apptestep','apptestobjname','appfindmethod','appevlemnt','appoptmethod','appassertdat','apptestresult','create_time','id','appcase']
    model = Appcasestep
    extra=1
class ApcaseAdmin(admin.ModelAdmin):
    list_display = ['appcasename', 'apptestresult','create_time','id']
    inlines = [ApcasetepAdmin]
admin.site.register(Appcase,ApcaseAdmin)
