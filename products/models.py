import os

from django.template.defaultfilters import slugify


from django.db import models
from django.core.urlresolvers import reverse



class Category(models.Model):
    name=models.CharField(max_length=200,db_index=True)
    slug=models.SlugField(max_length=200,db_index=True,unique=True)

    class Meta:
        ordering=('name',)
        verbose_name='category'
        verbose_name_plural='categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])

class Product(models.Model):
    TIPOS = (
        ('libros', 'Libros'),
        ('audios', 'Audios'),
        ('ideos', 'Videos')
    )
    category=models.ForeignKey(Category,related_name='products')
    name=models.CharField(max_length=200,db_index=True)
    slug=models.SlugField(max_length=200,db_index=True)
    image=models.ImageField(upload_to='products/%Y/%m/%d',blank=True)
    description=models.TextField(blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.PositiveIntegerField()
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    type=models.CharField(max_length=140, choices=TIPOS)

    class Meta:
        ordering=('name',)
        index_together=(('id','slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail',
            args=[self.id,self.slug])


class Document(models.Model):
    title = models.CharField(max_length=140)
    file = models.FileField()

    def __str__(self):
        return self.title

    @property
    def pretty_name(self):
        return "{0}.{1}".format(slugify(self.title),
                                get_extension(self.file.name))



def get_extension(filename):
    return os.path.splitext(filename)[1]