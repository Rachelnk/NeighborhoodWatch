from django  import forms
from content.models import Neighborhood, Business, Profile, Post
from django.contrib.auth.models import User
from cloudinary.forms import CloudinaryFileField

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

class UpdateUserForm(forms.ModelForm):
    first_name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']

class UpdateProfileForm(forms.ModelForm):
    portfolio_pic = forms.ImageField(required=True, widget=forms.FileInput(attrs={'class': 'form-control-file','data-height':300, 'data-max-file-size':"1M"}))
    bio = forms.CharField(required=True, widget=forms.Textarea(attrs={'class': 'form-control mb-4', 'rows': 5, 'placeholder':'Bio'}))
    

    class Meta:
      model = Profile
      exclude = ('user', 'neighborhood')

class AddNeighborhoodForm(forms.ModelForm):
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Title','class': 'form-control mb-4'}))
    description = forms.CharField(required=True, widget=forms.Textarea(attrs={'placeholder': 'Description','class': 'form-control mb-4','rows': 3,}))
    location = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Location','class': 'form-control mb-4'}))
    county = forms.ChoiceField(required=True, widget=forms.Select( attrs={'class': 'form-control mb-4'}), choices=counties)
    health_department = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Health Department','class': 'form-control mb-4'}))
    police_department = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Police Department','class': 'form-control mb-4'}))
    logo = forms.ImageField(required=True, widget=forms.FileInput(attrs={'class': 'form-control-file',}))
    class Meta:
      model = Neighborhood
      fields = ('name','description','location','county','logo','health_department','police_department')
    #   exclude = ('hood_admin',)

class AddBusinessForm(forms.ModelForm):
    title = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control mb-4', 'placeholder':'Business Title'}))
    description = forms.CharField(required=True, widget=forms.Textarea(attrs={'class': 'form-control mb-4', 'rows': 5, 'placeholder':'Description'}))
    category = forms.ChoiceField(choices=business_type, required=True, widget=forms.Select(attrs={'class': 'form-control mb-4', 'placeholder':'Select Business Type'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control mb-4', 'placeholder':'Business Email'}))
    class Meta:
        model = Business
        exclude = ('user', 'neighborhood')


class AddPostForm(forms.ModelForm):
  title = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control mb-4', 'placeholder':'Title'}))
  description = forms.CharField(required=True, widget=forms.Textarea(attrs={'class': 'form-control mb-4', 'rows': 5, 'placeholder':'Description'}))
  category = forms.ChoiceField(choices=post_type, required=True, widget=forms.Select(attrs={'class': 'form-control mb-4', 'placeholder':'Select Post Type'}))
  
  class Meta:
       model = Post
       fields = ('title', 'description', 'category')
       exclude = ('user', 'neighborhood')