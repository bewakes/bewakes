from django import template
import markdown

register = template.Library()


@register.filter(name='markdownify')
def markdownify(value):
    return markdown.markdown(value, ['codehilite'])#, safe_mode='escape')
