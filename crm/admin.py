from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import Membership

admin.site.unregister(User)
admin.site.unregister(Group)

# Customizing admin titles
admin.site.site_header = "DjAdmin"
admin.site.index_title = "Admin"
admin.site.site_title = "DjAdmin"

admin.site.register(Membership)