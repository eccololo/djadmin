from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import Membership

admin.site.unregister(User)
admin.site.unregister(Group)

# Customizing admin titles
admin.site.site_header = "DjAdmin"
admin.site.index_title = "Admin"
admin.site.site_title = "DjAdmin"

class MembershipAdmin(admin.ModelAdmin):

    fields = [
        ("name", "membership_plan"), 
        "membership_active", 
        # "unique_code"
    ]

    list_display = ["name", "membership_plan", "membership_active", "unique_code"]

    list_filter = ["membership_plan"]

    search_fields = ["name"]

    list_display_links = ["name"]

    # list_editable = ["membership_plan", "unique_code"]

admin.site.register(Membership, MembershipAdmin)