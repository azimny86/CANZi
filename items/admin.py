from django.contrib import admin
from .models import Items, Comments
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Items)
class ItemsAdmin(SummernoteModelAdmin):

    summernote_fields = ('description')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']


@admin.register(Comments)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ['name', 'email', 'body']
    actions = ['approved_comments']

    def approved_comments(self, request, queryset):
        queryset.updated(approved=True)