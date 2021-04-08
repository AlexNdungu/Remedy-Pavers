from django.db import models
from django.urls import reverse

#Products Model

class Products(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    image_product = models.ImageField(blank=True, null=True, upload_to = 'products/')

    def __str__(self):
        return self.name


#Upload Model

class Upload(models.Model):
    id_upload = models.AutoField(primary_key=True)
    prod_name = models.ForeignKey('Products', on_delete = models.CASCADE)
    image_upload = models.ImageField(blank=True, null=True, upload_to = 'images/')
    description = models.TextField(blank=True, null=True)
    upload_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.prod_name)

    class Meta:
        ordering = ['-upload_time']    

    @property
    def image_url(self):
        if self.image_upload and hasattr(self.image_upload, 'url'):
            return self.image_upload.url    

    def get_absolute_url(self):
        return reverse ('Remedy1:upload',args=[self.id,])       

#Testimonial place
class Testimonials(models.Model):
    my_name = models.CharField(primary_key=True ,max_length=100)
    message = models.TextField(blank=True, null=True)
    message_time = models.DateTimeField(auto_now_add=True)        

    def __str__(self):
        return self.my_name    