from django.db import models

class Client(models.Model):

    fullname = models.CharField('Full name', max_length=50)
    phone_number = models.CharField('Phone number', max_length=13)

    def __str__(self):
        return f'{self.fullname}'
    
class Sponsor(models.Model):

    name = models.CharField('Sponsor', max_length=50)
    image = models.ImageField('Image')

    def __str__(self):
        return f'{self.name}'

class Blog(models.Model):

    image = models.ImageField('Blog image')
    name = models.CharField('Title', max_length=256)
    text = models.TextField('Text')
    data = models.DateTimeField('Created')

    def __str__(self):
        return f'{self.name}'