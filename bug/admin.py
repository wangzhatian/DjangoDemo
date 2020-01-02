from django.contrib import admin

# Register your models here.
from django.contrib import admin
from bug.models import Bug
class BugAdmin(admin.ModelAdmin):
    list_display = ['bugname ', 'bugdetail ', ' bugstatus', ' buglevel', ' bugcreater', ' bugassign',
                    'create_time','id']
admin.site.register(Bug) # 把 Bug 管理模块注册到 Django admin 后台并能显示
