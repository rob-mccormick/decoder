from django.db import models


class Codedjob(models.Model):
    job_text = models.TextField()
    submit_time = models.DateTimeField()
    total_words = models.IntegerField(default=1)
    total_masc_words = models.IntegerField(default=0)
    total_fem_words = models.IntegerField(default=0)
    masc_word_proportion = models.DecimalField(max_digits=4,decimal_places=1,default=0)
    fem_word_proportion = models.DecimalField(max_digits=4,decimal_places=1,default=0)
    result = models.CharField(max_length=200,default='')
    masc_words = models.TextField(default='')
    fem_words = models.TextField(default='')

    def summary(self):
        return self.job_text[:100]
