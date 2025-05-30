from django.contrib import admin
from .models import Profile, Post

# Customize how Profile appears in the admin
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at')
    search_fields = ('user__username', 'user__email')

# Customize how Post appears in the admin (if you're using a Post model)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    search_fields = ('title', 'author__username')
    list_filter = ('created_at',)

# Register your models with admin
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Post, PostAdmin)
