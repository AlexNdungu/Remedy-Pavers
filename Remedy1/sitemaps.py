from django.contrib.sitemaps import Sitemap
from .models import Upload

class UploadSitemap(Sitemap):
    def items(self):
        return Upload.objects.all()