from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class Breed(models.Model):
    BREED_CHOICES = [
        ('persian', 'Персидская'),
        ('maine_coon', 'Мейн-кун'),
        ('siberian', 'Сибирская'),
        ('british_shorthair', 'Британская короткошерстная'),
        ('ragdoll', 'Рэгдолл'),
        ('other', 'Другая'),
    ]

    name = models.CharField(max_length=100, unique=True, choices=BREED_CHOICES)

    def __str__(self):
        return self.name

class Kitten(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=20, null=False)
    age = models.PositiveIntegerField(null=False, help_text="Укажите возраст котенка в месяцах.")
    description = models.TextField(blank=True)
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE, related_name='kittens')  # Ссылка на модель Breed
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='kittens')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class KittenRating(models.Model):
    kitten = models.ForeignKey(Kitten, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])  # Оценка от 1 до 5
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('kitten', 'user')  # Каждый пользователь может оценивать котенка только один раз

    def __str__(self):
        return f"Rating {self.rating} for {self.kitten} by {self.user}"
