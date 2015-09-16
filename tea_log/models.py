from django.db import models
from django.utils import timezone

class Company(models.Model):
    name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name

class Region(models.Model):
    
    '''
    Region_Choice = (
    ('An    ','Anxi        '),
    ('Guang ','Guangdong   '),
    ('Wu    ','WuYiMountain'),
    ('Yun   ','Yunnan      '),
    ('Dar   ','Darjeeling  '),
    ('ASS   ','Assam  '),
    ('Un    ','Unknown')
    )
    '''
    name = models.CharField(max_length=20, unique=True)
    def __str__(self):
        return self.name

class TeaName(models.Model):
    name = models.CharField(max_length=20, unique=True)
    def __str__(self):
        return self.name

class Tea(models.Model):
    name = models.ForeignKey(TeaName)
    company = models.ForeignKey(Company)
    region = models.ForeignKey(Region)
    NATION_CHOICE = (
        ('CH', 'Chinese'  ),
        ('JA', 'Japanese' ),
        ('ID', 'India'    ),
        ('NE', 'Nepalese' ),
        ('CY', 'Cylon'    ),
        ('TW', 'Twiwanese'),
        ('KO', 'Korea')
        )
    
    nation = models.CharField(max_length=10,  choices=NATION_CHOICE,  default='CH')
    
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

    tea = models.CharField(max_length=50, null=True, blank=True)

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
        return "{}/{}/{}".format(self.author.name, self.tea, self.created_date)