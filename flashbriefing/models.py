from django.db import models

class FeedItem(models.Model):
    uid = models.CharField(max_length=255)
    updateDate = models.DateTimeField(auto_now=True)
    titleText = models.CharField(max_length=255)
    luhn = models.TextField(blank=True, null=True)
    edmonson = models.TextField(blank=True, null=True)
    mainText = models.TextField(blank=True, null=True)
    redirectionUrl = models.URLField()
    def __str__(self):
        return self.titleText
    def save(self, *args, **kwargs):
        if self.luhn:
            self.mainText = self.luhn
        else:
            self.mainText = self.edmonson
        super(FeedItem, self).save(*args, **kwargs)
