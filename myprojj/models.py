from django.db import models
from django.contrib.auth.models import User

class PasswordCheck(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    password = models.CharField(max_length=100)
    strength_score = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"PasswordCheck by {self.user.username} at {self.created_at}"
    