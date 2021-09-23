from django.contrib import admin

from .models import Comment, Follow, Group, Post


class PostAdmin(admin.ModelAdmin):
    list_display = ("pk", "text", "pub_date", "author")
    search_fields = ("text",)
    list_filter = ("pub_date",)
    empty_value_display = "-пусто-"


admin.site.register(Post, PostAdmin)


class GroupAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "description")
    search_fields = ("title",)
    list_filter = ("description",)
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Group, GroupAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ("post", "author", "text", "created")
    search_fields = ("text",)
    list_filter = ("created",)
    empty_value_display = "-пусто-"


admin.site.register(Comment, CommentAdmin)


class FollowAdmin(admin.ModelAdmin):
    list_display = ("user", "following")
    search_fields = ("following",)
    list_filter = ("following",)
    empty_value_display = "-пусто-"


admin.site.register(Follow, FollowAdmin)
