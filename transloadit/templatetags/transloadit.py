import json

from django import template
from django.utils.html import escape
from django.conf import settings

register = template.Library()


@register.simple_tag
def transloadit_params():
    params = {
        'auth': {'key': settings.TRANSLOADIT_AUTH},
        'template_id': settings.TRANSLOADIT_HTML5_VIDEO_TEMPLATE,
    }
    return escape(json.dumps(params))


@register.simple_tag
def transloadit_url():
    return settings.TRANSLOADIT_URL
