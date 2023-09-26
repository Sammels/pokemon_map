from django.db import models  # noqa F401

# your models here
class Pokemon(models.Model):
    """Make Pokemon ID card"""
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media', null=True)

    class Meta:
        verbose_name = 'Покемон'
        verbose_name_plural = 'Покемоны'

    def __str__(self):
        return f"{self.title}"


class PokemonEntity(models.Model):
    """Make Pokemon Entity"""
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, verbose_name="Покемон")
    lat = models.FloatField(verbose_name="Широта")
    lon = models.FloatField(verbose_name="Долгота")
    appeared_at = models.DateTimeField(verbose_name="Время появления", null=True)
    dissapeared_at = models.DateTimeField(verbose_name="Время исчезновения", null=True)
    level = models.IntegerField(verbose_name="Уровень покемона", null=True)
    health = models.IntegerField(verbose_name="Количество Здоровья", null=True)
    strength = models.IntegerField(verbose_name="Сила покемона", null=True)
    defence = models.IntegerField(verbose_name="Уровень защиты", null=True)
    stamina = models.IntegerField(verbose_name="Очки выносливости покемона", null=True)

    class Meta:
        verbose_name = 'Сущность покемона'
        verbose_name_plural = 'Сущности покемонов'

    def __str__(self):
        return f"{self.pokemon.title}"


