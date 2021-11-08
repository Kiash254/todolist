from django.db import models

# Create your models here.
from django.utils import timezone
class Category(models.Model): 
    name = models.CharField(max_length=100) 
    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")
    def __str__(self):
        return self.name 
class TodoList(models.Model):
    title = models.CharField(max_length=250) 
    content = models.TextField(blank=True) # a text field 
    created = models.DateField(default=timezone.now().strftime("%Y-%m-%d")) # a date
    due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d")) # a date
    # 
    on_delete=models.DO_NOTHING,
    class Meta:
        ordering = ["-created"] #ordering by the created field
    def __str__(self):
        return self.title #name to be shown when called