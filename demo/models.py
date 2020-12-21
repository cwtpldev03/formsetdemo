from django.db import models

# Create your models here.
class PressureFormat(models.Model):
	name = models.ForeignKey('Certificate', on_delete=models.CASCADE, related_name='certificates')
	cal_p = models.FloatField()
	m1 = models.FloatField()
	m2 = models.FloatField()
	m3 = models.FloatField()
	mvmi = models.FloatField()
	deviation = models.FloatField()
	repeat_ability = models.FloatField()
	hysteresis = models.FloatField()
	expand_uncertainity = models.FloatField()

	def __str__(self):
		return str(self.name)


class Certificate(models.Model):
	name = models.CharField(max_length=256)

	def __str__(self):
		return self.name
