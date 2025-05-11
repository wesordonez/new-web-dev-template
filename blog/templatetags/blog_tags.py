from django import template
from blog.models import BlogIndexPage

register = template.Library()

@register.simple_tag
def get_blog_index_url():
    blog_index = BlogIndexPage.objects.live().first()
    return blog_index.url if blog_index else '#'
