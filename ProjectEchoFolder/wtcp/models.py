from django.db import models

# Create your models here.


class nativeLanguage(models.Model):
    nativeLanguage= models.CharField(max_length=200, help_text ='Enter a language (ex: English or Spanish)')

    def __str__(self):
        """String for representing the Model object."""
        return self.name


from django.urls import reverse

class Student(models.Model):
    """Model for representing a student (but not specific students)"""
    #Foriegn key will be used since students can only have one name but can qualify for many programs/languages etc
    name = model.ForiegnKey.CharField(max_length=350)

    #One to Many since students can only have one native language but many students can speak the same languages
    nativeLanguage = models.OneToManyField(nativeLanguage, help_text = 'Enter your native language')

    def __str__(self):
        """String for representing the Model object."""
        return self.name

    def get_absolute_url(self):
        """Returns the url to access a detail record for this student."""
        return reverse('student-detail', args=[str(self.id)])
