from django.db import models
from django.core.validators import RegexValidator

class GetInTouch(models.Model):
    name        = models.CharField(max_length=255,null=True,blank=False)
    phone       = models.CharField(validators=[RegexValidator(
                    regex=r'^998[0-9]{2}[0-9]{7}$',
                    message="Faqat o'zbek raqamlarigina tasdiqlanadi"
                    )], max_length=17)
    message    = models.TextField(blank=False)
    published   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name