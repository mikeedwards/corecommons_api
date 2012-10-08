from django.db import models

# Create your models here.
class Language(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    code = models.CharField(max_length=6)

    def __unicode__(self):
        return self.code

class GradeLevel(models.Model):
    name = models.CharField(max_length=6)

    def __unicode__(self):
        return self.name

class LearningStandardItem(models.Model):
    language = models.ForeignKey("Language")
    ref_id = models.CharField(max_length=100, unique=True)
    document_ref_id = models.CharField(max_length=100)
    parent_ref_id = models.CharField(max_length=100, blank=True, null=True)
    parent = models.ForeignKey("LearningStandardItem", blank=True, null=True)
    ref_URI = models.URLField()
    grade_levels = models.ManyToManyField(GradeLevel)
    code = models.CharField(max_length=100)
    statement = models.TextField()

    def __unicode__(self):
        return self.code

class Standard(LearningStandardItem):
    pass

class Component(LearningStandardItem):
    pass