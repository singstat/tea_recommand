from django.db import models
from django.utils import timezone


class Log_structure(models.Model):
    author  = models.ForeignKey('auth.User')
    Company = models.CharField(max_length=200)
    
    Tea_Color_Choices = (
            ('GR    ', 'Green'),
            ('BL    ', 'Black'),
            ('WH    ', 'White'),
            ('OO    ', 'Oolong'),
            ('PU-ERH', 'Pu-erh'),
            ('PURPLE', 'Purple'),
            ('BLENED', 'Blened')
        )
        
    Color = models.CharField(max_length=10,  choices=Tea_Color_Choices,  default='OO')
    
    Nation_Choices = (
    ('CH', 'Chinese'),
    ('JA', 'Japanese'),
    ('ID', 'India'),
    ('NE', 'Nepalese'),
    ('CY', 'Cylon'),
    ('TW', 'Twiwanese')
    )
    
    Nation = models.CharField(max_length=10,  choices=Nation_Choices,  default='CH')
    
    Region_Choice = (
    ('An    ','Anxi        '),
    ('Guang ','Guangdong   '),
    ('Wu    ','WuYiMountain'),
    ('Yun   ','Yunnan      '),
    ('Dar   ','Darjeeling  '),
    ('ASS   ','Assam  '),
    ('Un    ','Unknown')
    )
    
    Region = models.CharField(max_length=10,  choices=Region_Choice,  default='Un')
    
    name = models.CharField(max_length=50)
    
    Status_Choice = (
    ('le', 'Leaf'),
    ('tg', 'Tea bag'),
    )
    
    Status = models.CharField(max_length=10,  choices=Status_Choice,  default='le')
    
    text = models.TextField()
    
    Personal_Grade_Choice = (
    ('L', 'Like'),
    ('D', 'Dislike'),
    )
    
    Grade = models.CharField(max_length=10, choices=Personal_Grade_Choice,  default='L')
    
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name
