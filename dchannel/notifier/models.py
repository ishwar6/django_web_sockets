from django.db import models

# Create your models here.

class Channel(models.Model):
    user        = models.ForeignKey(User, null=True, blank=True)
    links     = models.ManyToManyField(Courses, blank=True)
    subtotal    = models.DecimalField(default=0.00, max_digits=8, decimal_places=2)
    total       = models.DecimalField(default=0.00, max_digits=8, decimal_places=2)
    updated     = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    objects = CartManager()

    def __str__(self):
        return str(self.id)

    @property
    def is_digital(self):
        qs = self.courses.all()
        new_qs=  qs.filter(is_digital = False)
        if new_qs.exists(): 
            return False
        return True

 
