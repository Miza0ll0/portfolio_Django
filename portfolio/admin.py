from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import About, Project

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # Empêche d'ajouter plus d'une instance
        return not About.objects.exists()

admin.site.register(Project)