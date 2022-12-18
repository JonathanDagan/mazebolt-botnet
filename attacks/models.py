from django.db import models

# Create your models here.

class Attack(models.Model):
    class AttackStatus(models.TextChoices):
        NEW = 'NEW', 'New'
        RUNNING = 'RUNNING', 'Running'
        DONE = 'DONE', 'Done'

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=10, choices=AttackStatus.choices, default=AttackStatus.NEW)
    startTimestamp = models.DateTimeField(auto_now_add=True)
    command = models.CharField(max_length=500)

class Client(models.Model):
    class ClientStatus(models.TextChoices):
        FREE = 'FREE', 'Free'
        RUNNING = 'RUNNING', 'Running'
        DONE = 'DONE', 'Done'

    id = models.AutoField(primary_key=True)
    address = models.CharField(max_length=100)
    status = models.CharField(max_length=10, choices=ClientStatus.choices, default=ClientStatus.FREE)
    attack = models.ForeignKey(Attack, on_delete=models.CASCADE, null=True)