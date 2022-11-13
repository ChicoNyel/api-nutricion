from django.db import models


class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        abstract = True
        managed = True


class Food(TimeStampMixin):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=1000, blank=True, null=True)
    calories = models.CharField(max_length=1000, blank=True, null=True)
    equivalence = models.CharField(max_length=1000, blank=True, null=True)
    measure = models.CharField(max_length=1000, blank=True, null=True)
    letter = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        db_table = 'food'

    def __str__(self):
        return self.name


class User(TimeStampMixin):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=1000, blank=True, null=True)
    email = models.EmailField(max_length=1000, blank=True, null=True)
    username = models.CharField(max_length=1000, blank=True, null=True)
    password = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        db_table = 'user'

    def __str__(self):
        return self.username
