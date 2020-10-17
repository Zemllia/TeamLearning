from django.contrib import admin

from .forms import UserForm, TeamForm, NewsForm
from .models import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class UserAdmin(BaseUserAdmin):
    form = UserForm
    list_display = ('username', 'email')
    fieldsets = (
        (None, {'fields': ('email', 'username', 'last_name',
                           'first_name', 'avatar', 'professionalism_coefficient')}),
        # ('Personal info', {'fields': ('last_name', 'first_name', 'middle_name', 'birth_date',)}),
    )
    list_display_links = ('username', 'email')
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'last_name',
                                'first_name', 'avatar', 'professionalism_coefficient')}
         ),
    )
    search_fields = ('username',)
    ordering = ('username',)
    filter_horizontal = ()


class TeamAdmin(admin.ModelAdmin):
    form = TeamForm
    list_display = ('name', )
    fieldsets = (
        (None, {'fields': ('name', 'users', 'description', 'avatar')}),
        # ('Personal info', {'fields': ('last_name', 'first_name', 'middle_name', 'birth_date',)}),
    )
    list_display_links = ('name', )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'users', 'description', 'avatar')}
         ),
    )
    search_fields = ('name',)
    ordering = ('name',)
    filter_horizontal = ()


class NewsAdmin(admin.ModelAdmin):
    form = NewsForm
    list_display = ('post_header', 'author')
    fieldsets = (
        (None, {'fields': ('author', 'post_header', 'post_text', 'post_image', 'date')}),
        # ('Personal info', {'fields': ('last_name', 'first_name', 'middle_name', 'birth_date',)}),
    )
    list_display_links = ('post_header', 'author')
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('author', 'post_header', 'post_text', 'post_image', 'date')}
         ),
    )
    search_fields = ('post_header', 'author')
    ordering = ('post_header',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(News, NewsAdmin)
