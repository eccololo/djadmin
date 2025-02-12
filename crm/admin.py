from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.urls import resolve
from .models import Membership

# admin.site.unregister(User)
# admin.site.unregister(Group)

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

    actions = ("set_membership_to_active", )

    def set_membership_to_active(self, request, queryset):

        queryset.update(membership_active=True)

        self.message_user(request, "Membership(s) activated.")

    set_membership_to_active.short_description = "Mark selected items as membership active"

    def has_add_permission(self, request):
        return True
    
    def has_change_permission(self, request, obj=None):
        return True
    
    def has_delete_permission(self, request, obj=None):

        if any("Are you sure you want to delete this object?" in m.message for m in messages.get_messages(request)):
            
            return True

        if obj is not None and request.POST.get("action") == "delete_selected":

            messages.add_message(request, messages.ERROR, (
                "Are you sure you want to delete this object?"
            ))

        elif obj is not None and resolve(request.path_info).url_name == "crm_membership_delete":
            
            messages.add_message(request, messages.ERROR, (
                "Are you sure you want to delete this object?"
            ))

        return True

admin.site.register(Membership, MembershipAdmin)