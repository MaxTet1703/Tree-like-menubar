from django.db import models
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.

class Menu(models.Model):

    """ Модель, описывающая меню как объект """
    
    name = models.TextField("Имя меню", null=False)
    slug = models.SlugField("Url меню", null=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super(Menu, self).save(*args, **kwargs)


class MenuItem(models.Model):
    """ Модель, описывающая разделы меню """

    title = models.TextField("Название раздела")
    slug = models.SlugField("Url раздела", null=False)
    parent = models.ForeignKey(to="MenuItem", null=True, blank=True, on_delete=models.CASCADE, related_name="children", verbose_name="Родитель")
    menu = models.ForeignKey(to=Menu, on_delete=models.CASCADE, related_name="item", verbose_name="Меню")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        subslug = slugify(self.title)
        if self.parent: self.slug = f"{self.parent.slug}_{subslug}"
        else: self.slug = f"{self.menu.slug}_{subslug}"
        return super(MenuItem, self).save(*args, **kwargs)

    @property
    def get_absolute_url(self):
        return reverse("menu", kwargs={"url": self.slug})


