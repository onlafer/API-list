from django import template


from new_services.models import NewAPI


register = template.Library()


@register.simple_tag()
def tag_new_apis():
    return NewAPI.objects.all()


@register.simple_tag(takes_context=True)
def tag_user_apis(context, user):
    return NewAPI.objects.filter(user=user)
