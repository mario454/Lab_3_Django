from django.db import models
from django.db.models import Count, Q
# Create your models here.

class Track(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100, null=False, unique=True)

    @classmethod
    def getalltracks(cls):
        return cls.objects.all()

    @classmethod
    def getalltracks_N_numtr(cls):
        return cls.objects.annotate(numberoftr=Count('trainee', filter=Q(trainee__status=True))).order_by('id')
    
    @classmethod
    def gettrackbyid(cls, id):
        return cls.objects.get(id=id)