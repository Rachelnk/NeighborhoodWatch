from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

counties = [
    ('', ('Choose')), 
    ('Baringo', ('Baringo')),
    ('Bomet', ('Bomet')),
    ('Bungoma ', ('Bungoma ')),
    ('Busia', ('Busia')),
    ('Elgeyo Marakwet', ('Elgeyo Marakwet')),
    ('Embu', ('Embu')),
    ('Garissa', ('Garissa')),
    ('Homa Bay', ('Homa Bay')),
    ('Isiolo', ('Isiolo')),
    ('Kajiado', ('Kajiado')),
    ('Kakamega', ('Kakamega')),
    ('Kericho', ('Kericho')),
    ('Kiambu', ('Kiambu')),
    ('Kilifi', ('Kilifi')),
    ('Kirinyaga', ('Kirinyaga')),
    ('Kisii', ('Kisii')),
    ('Kisumu', ('Kisumu')),
    ('Kitui', ('Kitui')),
    ('Kwale', ('Kwale')),
    ('Laikipia', ('Laikipia')),
    ('Lamu', ('Lamu')),
    ('Machakos', ('Machakos')),
    ('Makueni', ('Makueni')),
    ('Mandera', ('Mandera')),
    ('Meru', ('Meru')),
    ('Migori', ('Migori')),
    ('Marsabit', ('Marsabit')),
    ('Mombasa', ('Mombasa')),
    ('Muranga', ('Muranga')),
    ('Nairobi', ('Nairobi')),
    ('Nakuru', ('Nakuru')),
    ('Nandi', ('Nandi')),
    ('Narok', ('Narok')),
    ('Nyamira', ('Nyamira')),
    ('Nyandarua', ('Nyandarua')),
    ('Nyeri', ('Nyeri')),
    ('Samburu', ('Samburu')),
    ('Siaya', ('Siaya')),
    ('Taita Taveta', ('Taita Taveta')),
    ('Tana River', ('Tana River')),
    ('Tharaka Nithi', ('Tharaka Nithi')),
    ('Trans Nzoia', ('Trans Nzoia')),
    ('Turkana', ('Turkana')),
    ('Uasin Gishu', ('Uasin Gishu')),
    ('Vihiga', ('Vihiga')),
    ('Wajir', ('Wajir')),
    ('West Pokot', ('West Pokot')),
]

business_type = [('cleaning',('cleaning')),
('grocery',('grocery')),
('bakery',('bakery')),
('salon',('salon')),
('barbershop',('barbershop')),
('butchery',('butchery')),
('chemist',('chemist')),
('general_shop',('general_shop')),
('milk_atm',('milk_atm')),
]
post_type = [
    ('1', 'Crimes and Safety'),
    ('2', 'Health Emergency'),
    ('3', 'Recommendations e.g Plumber, mamafua'),
    ('4', 'Power Outages'),
    ('5', 'Lost and Found'),
    ('6', 'Death'),
    ('7', 'Event'),
    ('8', ('water'))
]

# Create your models here.

class Neighborhood(models.Model):
    name = models.TextField(max_length=20, verbose_name='Hood Title', null=True)
    description = models.TextField(max_length=254, blank=True, verbose_name='Description')
    location = models.CharField(max_length=150, verbose_name='Location', null=True, blank=True)
    county = models.CharField(choices=counties, max_length=150, verbose_name='County', null=True, blank=True)
    logo = CloudinaryField('logo')
    admin =  models.ForeignKey(User, on_delete=models.CASCADE, verbose_name= 'Admin', null=True, blank=True)
    health_department = models.CharField(max_length=15, null=True, blank=True, verbose_name='Health Department')
    police_department = models.CharField(max_length=15, null=True, blank=True, verbose_name='Police Department')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Date Created')
    date_updated = models.DateTimeField(auto_now=True, verbose_name='Date Updated')


    def __str__(self):
      return str(self.name)

    def save_hood(self):
      self.save()

    def delete_hood(self):
      self.delete()

    @classmethod
    def find_hood(cls, neighborhood_id):
      return cls.objects.filter(id=neighborhood_id)

    def update_hood(self, id, name, location, county, logo):
        updateHood = Neighborhood.objects.filter(id=id).update(name = name,
                    location = location,
                    county = county,
                    logo = logo)

        return updateHood
    class Meta:
      verbose_name_plural = 'Neighborhoods'





class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='User', null=True)
    profile_pic = CloudinaryField('image')
    bio = models.TextField()
    email = models.EmailField(max_length=100, blank=True)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, null=True ,verbose_name= 'Hood')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Date Created', null= True)
    date_updated = models.DateTimeField(auto_now=True, verbose_name='Date Updated', null= True)

class Post(models.Model):
    title = models.CharField(max_length=500, verbose_name='Title', null=True)
    caption = models.CharField(max_length=2200, verbose_name='Caption', null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Author', null = True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Profile', null =True)
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Date Created', null= True)
    date_updated = models.DateTimeField(auto_now=True, verbose_name='Date Updated', null= True)

    def __str__(self):
      return str(self.title)

    def save_post(self):
      self.save()

    def delete_post(self):
      self.delete()

    @classmethod
    def all_posts(cls):
      return cls.objects.all()
    
    @classmethod
    def searcg_posts(cls, title):
      return cls.objects.filter(title__icontains=title).all()
    class Meta:
      verbose_name_plural = 'Posts'

