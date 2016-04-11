from django.db import models

class BioDrug(models.Model):
    name = models.CharField(max_length=100)
    inputer = models.ForeignKey('auth.User', null=True, blank=True)

    create_time = models.DateTimeField(auto_now_add=True, editable=False, null=True)
    update_time = models.DateTimeField(auto_now=True, editable=False, null=True)

    def __unicode__(self):
        return self.name