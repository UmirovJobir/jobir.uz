from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.conf import settings

from .models import GetInTouch

import telebot
from telebot.util import quick_markup

bot = telebot.TeleBot(settings.TELEGRAMBOT.get('token'))

def return_markup(id):
    return quick_markup({
        f"Contact: #{id}": {'url': f'https://jobir.uz/admin/app/getintouch/{id}/change/'},
    }, row_width=1)


@receiver(post_save, sender=GetInTouch) 
def create_contact(sender, instance, created, **kwargs):
    if created:
        message = f"""
📩 Yangi murojaat❗️\n
👤 Mijoz:  {instance.name}
📞 Raqam: <code>+{instance.phone}</code>
📄 Xabar:  <code>{instance.message}</code>
"""
        bot.send_message(chat_id=settings.TELEGRAMBOT.get('chat_id'),
                        text=message,
                        reply_markup= return_markup(id=instance.pk),
                        parse_mode="HTML")