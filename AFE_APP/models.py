from django.db import models

class AFE_REQUEST(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    subsidiaries = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    types = models.CharField(max_length=100)
    # operation = models.CharField(max_length=100)
    environment = models.CharField(max_length=100)
    assets = models.CharField(max_length=100)
    start_date = models.CharField(max_length=100)
    ops_duration = models.CharField(max_length=100)
    perenco_share = models.CharField(max_length=100)
    # end_of_license = models.CharField(max_length=100)
    create_leader = models.CharField(max_length=100)
    member = models.CharField(max_length=100)

    def __str__(self):
        return self.name
