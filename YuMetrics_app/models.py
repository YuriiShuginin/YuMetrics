from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """User information"""

    country = models.CharField("Country", max_length=30)
    mistakes = models.ManyToManyField('Metric', verbose_name='Mistakes', through='Mistake', related_name='MistakenUsers')
    
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name', 'country']

    def __str__(self):
        return self.username


class Metric(models.Model):
    """Metric information"""

    class Meta:
        verbose_name = "Metric"
        verbose_name_plural = "Metrics"

    name = models.CharField("Metric name", max_length=20, unique=True, blank=False)
    transcript = models.CharField("Metric name transcript", max_length=50)
    definition = models.CharField("Metric definition", unique=True, max_length=255, blank=False)

    def __str__(self):
        if self.transcript:
            return f"{self.name} ({self.transcript}) – {self.definition}"
        return f"{self.name} – {self.definition}"


class Mistake(models.Model):
    """User's mistake data"""

    class Meta:
        verbose_name = "Mistake"
        verbose_name_plural = "Mistakes"
        unique_together = ["metric", "user"]

    metric = models.ForeignKey(Metric, on_delete=models.CASCADE, related_name="metric_mistakes")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_mistakes")
    date = models.DateTimeField("Mistake date", auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} – {self.metric.name}"


class Result(models.Model):
    """User's quiz result"""

    class Meta:
        verbose_name = "Result"
        verbose_name_plural = "Results"

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="results")
    score = models.IntegerField("Score", blank=False)
    date = models.DateTimeField("Result date", auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}: {self.score}"
