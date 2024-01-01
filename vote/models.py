from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Voting(models.Model):
    name = models.CharField(max_length=20,blank=True,null=True)
    image = models.ImageField(upload_to='image')
    desc = models.TextField(blank=None)
    count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
    
class Voters(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    voted_for = models.ForeignKey(Voting, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.user.username} - Voted for: {self.voted_for.name}"
    