from django.db import models


from django.urls import reverse


CATEGORY_CHOICES = (
    ('TS', 'Футболки'),
    ('SS', 'Кофты'),
    ('HT', 'Головные уборы'),
    ('RG', 'Рашгарды'),
    ('CR', 'Шевроны'),
    ('FL', 'Флаги'),
    ('EQ', 'Снаряжение с разделением на СМБ и ИСБ'),
)


class Product(models.Model):
    title = models.CharField(
        'Название товара',
        max_length=200
    )
    description = models.TextField(
        'Описание товара'
    )
    price = models.FloatField(
        'Цена товара'
    )
    category = models.CharField(
        'Категория',
        choices=CATEGORY_CHOICES,
        max_length=2
    )
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True
    )
    image = models.ImageField(
        'Картинка',
        upload_to='product/',
        blank=True
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('shop_detail', kwargs={'shop_pk': self.pk})

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Cart(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )
    quantity = models.PositiveIntegerField(
        default=1
    )

    @property
    def total_cost(self):
        return self.quantity * self.product.price


class News(models.Model):
    title = models.CharField(
        'Название новости',
        max_length=200
    )
    description = models.TextField(
        'Описание новости'
    )
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True
    )
    image = models.ImageField(
        'Картинка',
        upload_to='product/',
        blank=True
    )

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('new_detail', kwargs={'new_pk': self.pk})

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
