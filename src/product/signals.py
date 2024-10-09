from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.postgres.search import SearchVector
from .models import Product


@receiver(post_save, sender=Product)
def create_search_vector(sender, instance, created, **kwargs):
    # if instance.active:
    #     Product.objects.filter(id=instance.id).update(search_vector=SearchVector('name', 'description'))

    if created:
        Product.objects.filter(id=instance.id).update(search_vector=SearchVector('name', 'description'))

