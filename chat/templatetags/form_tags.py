from django import template

register = template.Library()

@register.filter(name='add_class')
def add_class(value, arg):
    """
    Adds a CSS class to the existing class of a form field widget.
    """
    css_classes = value.field.widget.attrs.get('class', '')
    updated_classes = f"{css_classes} {arg}".strip()
    return value.as_widget(attrs={'class': updated_classes})
