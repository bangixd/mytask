from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField()
    image = models.ImageField(upload_to='category')

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product:category_filter', args=[self.slug,])


class Product(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField()
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False)
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to='product')
    describe = models.TextField()

    def __str__(self):
        return f'{self.name} from {self.category}'

    def get_absolute_url(self):
        return reverse('product:detail', args=[self.slug])


