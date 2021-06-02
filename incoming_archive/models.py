from django.db import models
from django.conf import settings


class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now =True)

    class Meta:
        abstract = True
        ordering = ('-created', )


class Institute(TimeStampedModel):
    name = models.CharField(max_length=200)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Mail(TimeStampedModel):
    registration_number = models.IntegerField()
    reference_number = models.IntegerField()
    source = models.ForeignKey(Institute, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    pdf_copy = models.FileField(upload_to='incoming/pdf-copies', blank=True, null=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


