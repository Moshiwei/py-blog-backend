from django.db import models

# Create your models here.
class Blogs(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, null=False)
    author = models.CharField(max_length=100)
    content = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'blogs'
        ordering = ['-created_at']
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'