from django.db import models
import uuid

class Msg(models.Model):
    user = models.CharField(max_length=15)
    message = models.TextField()
    password = models.CharField(max_length=20)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return str(self.id)