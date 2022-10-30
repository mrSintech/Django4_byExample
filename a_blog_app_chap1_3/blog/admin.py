from django.contrib import admin
from .models import Post

# if admin.site.register used django will take care of everything
# but, by using @admin.register() we can customize the admin site


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # with list_display we can specify which fields we want to show in
    # objects list
    list_display = ('title', 'slug', 'author', 'publish', 'status')

    # list_filter allow us to specify filter over fields
    list_filter = ('status', 'created', 'publish', 'author')

    # search_fields give us feature to search throgh selected fields
    search_fields = ('title', 'body')

    # prepopulated_fields automaticaly prepopulates the slug field with the input of the
    # title field
    prepopulated_fields = {"slug": ('title',)}

    # with raw_id_fields the author field is now displayed with a lookup
    # widget, which can be much better than a drop-down select input when
    # you have thousands of users. This is achieved with the
    # raw_id_fields attribute, the field show id of related obj
    raw_id_fields = ('author',)

    # date_hirearchy add navigation links to navigate through a date hierarchy
    date_hierarchy = 'publish'

    # with ordering We have specified the default sorting criteria
    ordering = ("status", 'publish')
