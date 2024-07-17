from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from django.utils.translation import gettext
from django.utils.translation import gettext_lazy as _

from apps.models import Product, Category, User, StudentUser, TeacherUser

# Unregister the default User and Group models
# admin.site.unregister(User)
admin.site.unregister(Group)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'id', 'name',
    search_fields = 'name',


# @admin.register(User)
# class UserUserAdmin(UserAdmin):  # UserAdmin  pay  attention ! Not ModelAdmin
#     pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = 'id', 'name', 'price'
    autocomplete_fields = 'category',


@admin.register(StudentUser)
class StudentUserUserAdmin(UserAdmin):  # UserAdmin  pay  attention ! Not ModelAdmin
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email", 'birth_date', 'image', 'phone')}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )

    def get_queryset(self, request):
        return super().get_queryset(request).filter(type=StudentUser.Type.STUDENT)


@admin.register(TeacherUser)
class TeacherUserUserAdmin(UserAdmin):  # UserAdmin  pay  attention ! Not ModelAdmin
    def get_queryset(self, request):
        return super().get_queryset(request).filter(type=StudentUser.Type.TEACHER)
