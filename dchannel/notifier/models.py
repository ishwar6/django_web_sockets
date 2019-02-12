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

 

class Cart(models.Model):
    user        = models.ForeignKey(User, null=True, blank=True)
    courses     = models.ManyToManyField(Courses, blank=True)
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

 



def m2m_changed_cart_receiver(sender, instance, action, *args, **kwargs):
    if action == 'post_add' or action == 'post_remove' or action == 'post_clear':
        courses = instance.courses.all()
        total = Decimal(0.00)
        for x in courses:
            total = Decimal(total) + Decimal(x.price)
        if instance.subtotal != total:
            instance.subtotal = total
            instance.save()

m2m_changed.connect(m2m_changed_cart_receiver, sender=Cart.courses.through)




def pre_save_cart_receiver(sender, instance, *args, **kwargs):
    if instance.subtotal > 0:
        instance.total = Decimal(instance.subtotal) * Decimal(1.08) # 8% tax
    else:
        instance.total = 0.00

pre_save.connect(pre_save_cart_receiver, sender=Cart)

