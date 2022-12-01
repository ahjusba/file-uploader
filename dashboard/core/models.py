from django.db import models

class Member(models.Model):
  username = models.CharField(max_length=150)
  organization = models.CharField(max_length=150)

  def __str__(self):
    return self.name

class File(models.Model):
  filename = models.CharField(max_length=150)
  uploader = models.ForeignKey(Member, on_delete=models.CASCADE)
  upload_time = models.DateTimeField()
  downloads = models.IntegerField(default=0)

  def __str__(self):
    return self.name