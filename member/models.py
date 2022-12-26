from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
# Create your models here.


class Member(MPTTModel):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    email = models.EmailField(blank=True, unique=True)
    birth_date = models.DateField()
    contact = models.CharField(max_length=100, blank=True)
    parent = TreeForeignKey(
        'self', on_delete=models.CASCADE, related_name="child_member", blank=True, null=True)

    class MPTTMeta:
        parent_attr = 'parent'
