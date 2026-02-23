from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

class Article(models.Model):
    # The headline of the news
    title = models.CharField(max_length=200)
    
    # Optional: A cover image for the homepage preview cards
    thumbnail = models.ImageField(upload_to='thumbnails/', blank=True, null=True)
    
    # The Rich Text Editor field for the main news body
    content = CKEditor5Field('Content', config_name='default')
    
    # Timestamps to track when news was published or edited
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # This ensures the newest articles show up first by default
        ordering = ['-created_at']

    def __str__(self):
        return self.title