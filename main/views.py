from django.http import HttpResponsePermanentRedirect
from django.urls import reverse


def main_redirect(request):
    uri = reverse('category:list_filter', args=('all', ))
    return HttpResponsePermanentRedirect(uri)
