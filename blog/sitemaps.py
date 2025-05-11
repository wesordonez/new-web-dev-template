from django.contrib.sitemaps import Sitemap
from .models import BlogPage

class BlogSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return BlogPage.objects.live()

    def lastmod(self, obj):
        # Use the latest revision or first published date
        return obj.latest_revision_created_at or obj.first_published_at

    def location(self, obj):
        return obj.url
