from django.db import models

# Create your models here.
class Sruser(models.Model):
    username = models.CharField(max_length=64)
    useremail = models.EmailField(max_length=128)
    password = models.CharField(max_length=64)
    registered_dttm = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'sunrin_sruser'
        verbose_name = '선린 사용자'
        verbose_name_plural = '선린 사용자'