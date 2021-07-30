from django.db import models
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import truncatechars

from base.enums import TRUNCATE_LENGTH


class Message(models.Model):
    sender = models.ForeignKey(get_user_model(), related_name='messages_sent', on_delete=models.CASCADE)
    receiver = models.ForeignKey(get_user_model(), related_name='messages_obtained', on_delete=models.CASCADE)
    subject = models.CharField(_('message subject'), max_length=100)
    message = models.TextField(_('message content'))
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        ret = f'Message: {self.subject}'
        if len(ret) < TRUNCATE_LENGTH:
            return ret
        return truncatechars(ret, TRUNCATE_LENGTH)
