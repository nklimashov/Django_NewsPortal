from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import m2m_changed
from django.dispatch import receiver

from .models import Post


@receiver(m2m_changed, sender=Post)
def post_created(instance, created, **kwargs):
    if kwargs['action'] != 'post_add':
        return

    emails = User.objects.filter(
        subscriptions__category__in=instance.category_type
    ).values_list('email', flat=True)

    subject = f'Появился новый пост от {instance.post_author}'

    text_content = (
        f'Категория: {instance.category_type}\n'
        f'Тема: {instance.title}\n\n'
        f'Ссылка на пост: http://127.0.0.1:8000{instance.get_absolute_url()}'
    )
    html_content = (
        f'Категория: {instance.category_type}<br>'
        f'Тема: {instance.title}<br><br>'
        f'<a href="http://127.0.0.1{instance.get_absolute_url()}">'
        f'Ссылка на пост</a>'
    )
    for email in emails:
        msg = EmailMultiAlternatives(subject, text_content, None, [email])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
