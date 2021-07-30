from django.contrib import admin

from .models import Message


class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'sender', 'receiver', 'subject', 'message', 'date_created')
    list_display_links = ('id', )
    list_select_related = ('sender', 'receiver')
    search_fields = ('sender_email', 'receiver_email', 'subject',)


admin.site.register(Message, MessageAdmin)
