from django.contrib import admin
from django.contrib.auth.models import Group
from .models import product_details,categories,product_base,comment

                   


class PostAdmin(admin.ModelAdmin):
    list_display = ('add_product', 'slug', 'timestamp','category')

class baseAdmin(admin.ModelAdmin):
    base_list = ('prod_cate','detail_base','taged')

class commentAdmin(admin.ModelAdmin):
    list_dispay = ('name','email','content','timestamp')
    # list_filter = ('timestamp':timestamp)
    search_fields = ('name','email','content')
    actions = ['approve_comment']

    def approve_comments(self,request,queryset):
        queryset.update(active = True)

#     list_filter = ("status",)
    # search_fields = ['title', 'content']
# admin.site.site_header = "  "
admin.site.site_header = " presentation admin portal "
admin.site.index_title = " welcome to the admin panel "


admin.site.register(product_details,PostAdmin) 
admin.site.register(categories)
admin.site.register(comment,commentAdmin)
admin.site.unregister(Group)
# admin.site.register(product_base,baseAdmin)




