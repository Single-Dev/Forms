from django.db import models


class SubmitMsgToEmail(models.Model):
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=700)
    email = models.EmailField()

    def __str__(self):
        return self.subject