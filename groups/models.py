from django.db import models
from django.utils.text import slugify
from django.urls import reverse
import misaka
from django.contrib.auth import get_user_model
User = get_user_model()

from django import template
register = template.Library()

# Create your models here.

class Group(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(allow_unicode=True, unique=True)
    description = models.TextField(blank=True, default='')
    description_html = models.TextField(editable=False, default='', blank=True)
    members = models.ManyToManyField(User, through='GroupMember')

    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        self.description = misaka.html(self.description)
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('group:single',kwargs={'slug': self.slug})

    class Meta:
        ordering = ['name']

class GroupMember(models.Model):
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, related_name='memberships', null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='user_groups', null=True)

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ('group', 'user')