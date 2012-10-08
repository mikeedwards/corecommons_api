from django.contrib import admin
from core.models import Standard, Component, GradeLevel, Language

class StandardAdmin(admin.ModelAdmin):
    pass

class ComponentAdmin(admin.ModelAdmin):
    pass

class GradeLevelAdmin(admin.ModelAdmin):
    pass

class LanguageAdmin(admin.ModelAdmin):
    pass

admin.site.register(Standard, StandardAdmin)
admin.site.register(Component, ComponentAdmin)
admin.site.register(GradeLevel, GradeLevelAdmin)
admin.site.register(Language, LanguageAdmin)