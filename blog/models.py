from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from ckeditor.fields import RichTextField

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    topic = models.CharField(max_length=200, blank=True, null=True)
    title = models.CharField(max_length=200)
    text = models.TextField(blank=True, null=True)
    content = RichTextField(blank=True, null=True)
    created_date = models.DateTimeField(
        default = timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)
