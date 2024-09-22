from django.db import models
from django.core.validators import RegexValidator

class GetInTouch(models.Model):
    name = models.CharField(max_length=255,null=True,blank=False)
    phone = models.CharField(validators=[RegexValidator(
            regex=r'^998[0-9]{2}[0-9]{7}$',
            message="Faqat o'zbek raqamlarigina tasdiqlanadi"
            )], max_length=17)
    message = models.TextField(blank=False)
    published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Project(models.Model):
    STATUS_CHOICES = (
        (True, 'Active'),
        (False, 'Inactive'),
    )
    
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/projects')
    link = models.URLField()
    position = models.IntegerField()
    status = models.BooleanField(choices=STATUS_CHOICES, default=True)
    
    class Meta:
        ordering = ['position']

    def __str__(self):
        return self.name
