from django.contrib import admin

from .forms import UserForm, TeamForm, NewsForm, ProjectForm
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
        (None, {'fields': ('name', 'creator', 'users', 'description', 'avatar', 'is_open')}),
        # ('Personal info', {'fields': ('last_name', 'first_name', 'middle_name', 'birth_date',)}),
    )
    list_display_links = ('name', )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'creator', 'users', 'description', 'avatar', 'is_open')}
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


class ProjectAdmin(admin.ModelAdmin):
    form = ProjectForm
    list_display = ('project_name', 'creator', 'start_date', 'dead_line')
    fieldsets = (
        (None, {'fields': ('project_name', 'creator', 'project_description', 'teams', 'requests', 'start_date',
                           'dead_line', 'is_open')}),
        # ('Personal info', {'fields': ('last_name', 'first_name', 'middle_name', 'birth_date',)}),
    )
    list_display_links = ('project_name', 'creator', 'start_date', 'dead_line')
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('project_name', 'creator', 'project_description', 'teams', 'requests', 'start_date',
                       'dead_line', 'is_open')}
         ),
    )
    search_fields = ('project_name', 'creator', 'start_date')
    ordering = ('start_date', 'project_name')
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Project, ProjectAdmin)
