from django.template import Library
from core.forms import ContactForm

register = Library()

@register.simple_tag
def get_contact():
    return ContactForm