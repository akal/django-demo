from django.db import models

# Create your models here.

class Question(models.Model):
    text = models.CharField(max_length=100)

    def __str__(self):
        return 'Question: %s' % self.text


class ContactRequest(models.Model):
    title = models.CharField(max_length=4,
                             choices=(('MR', 'Mr'), 
                                      ('MRS', 'Mrs'),
                                      ('MS', 'Ms'),
                                      ('REV', 'Rev'),
                                      ('DR', 'Dr')))
    name = models.CharField(max_length=100)
    email = models.EmailField()
    question = models.ForeignKey(Question)
    answer = models.CharField(max_length=100)

    def __str__(self):
        return 'ContactRequest: %s' % self.name
    
