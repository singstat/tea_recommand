from django.db import models
from django.utils import timezone

class Company(models.Model):
    name = models.CharField(max_length=100, unique=True, default='')
    def __str__(self):
        return self.name


class TeaName(models.Model):
    name = models.CharField(max_length=20, unique=True, default='')
    def __str__(self):
        return self.name

class Tea(models.Model):
    name = models.ForeignKey(TeaName)
    company = models.ForeignKey(Company)
    
    NATION_CHOICE = (
        ('CH', 'Chinese'  ),
        ('JA', 'Japanese' ),
        ('ID', 'India'    ),
        ('NE', 'Nepalese' ),
        ('CY', 'Cylon'    ),
        ('TW', 'Twiwanese'),
        ('KO', 'Korea'),
        ('Un    ','Unknown')
        )
    
    nation = models.CharField(max_length=10,  choices=NATION_CHOICE,  default='CH')
    
    REGION_CHOICE = (
    ('An    ','Anxi        '),
    ('Guang ','Guangdong   '),
    ('Wu    ','WuYiMountain'),
    ('Yun   ','Yunnan      '),
    ('Dar   ','Darjeeling  '),
    ('ASS   ','Assam  '),
    ('Un    ','Unknown')
    )

    region = models.CharField(max_length=20, choices=REGION_CHOICE,unique=True, default='Un')
    
    COLOR_CHOICE = (
            ('GR    ', 'Green'),
            ('BL    ', 'Black'),
            ('WH    ', 'White'),
            ('OO    ', 'Oolong'),
            ('PU-ERH', 'Pu-erh'),
            ('PURPLE', 'Purple'),
            ('BLENED', 'Blened')
        )
        
    color = models.CharField(max_length=10,  choices=COLOR_CHOICE,  default='OO')
    
    STATUS_CHOICE = (
        ('le', 'Leaf'),
        ('tg', 'Tea bag'),
        )
    
    status = models.CharField(max_length=10,  choices=STATUS_CHOICE,  default='le')
    
    def __str__(self):
        return "{}/{}/{}".format(self.name, self.company, self.status)
    


class Entry(models.Model):
    author  = models.ForeignKey('auth.User')

    tea_info = models.ForeignKey(Tea, null=True)

    comment = models.TextField(null=True, blank=True)
    
    #Personal_Grade_Choice = (
    #    ('L', 'Like'),
    #    ('D', 'Dislike'),
    #    )
    #
    #Grade = models.CharField(max_length=10, choices=Personal_Grade_Choice,  default='L')
    
    Personal_Grade_Choice = (
        (True, 'Like'),
        (False, 'Dislike'),
        )
    like = models.BooleanField(choices=Personal_Grade_Choice,  default=True)
    
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}/{}/{}".format(self.author.username, self.tea_info, self.created_date)