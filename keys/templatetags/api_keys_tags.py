from django import template
from django.utils.http import urlencode


from keys.models import ApiKey


register = template.Library()


@register.simple_tag(takes_context=True)
def tag_user_api_keys(context, user):
    return ApiKey.objects.filter(user=user).order_by("created_at")
