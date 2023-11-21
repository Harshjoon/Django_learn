from django.contrib import admin
from .models        import Profile
from form.models    import BugReport

# Register your models here.
admin.site.register(Profile)
admin.site.register(BugReport)

