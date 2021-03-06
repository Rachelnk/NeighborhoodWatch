# Generated by Django 4.0.5 on 2022-06-18 09:52

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Neighborhood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=20, null=True, verbose_name='Hood Title')),
                ('description', models.TextField(blank=True, max_length=254, verbose_name='Description')),
                ('location', models.CharField(blank=True, max_length=150, null=True, verbose_name='Location')),
                ('county', models.CharField(blank=True, choices=[('', 'Choose'), ('Baringo', 'Baringo'), ('Bomet', 'Bomet'), ('Bungoma ', 'Bungoma '), ('Busia', 'Busia'), ('Elgeyo Marakwet', 'Elgeyo Marakwet'), ('Embu', 'Embu'), ('Garissa', 'Garissa'), ('Homa Bay', 'Homa Bay'), ('Isiolo', 'Isiolo'), ('Kajiado', 'Kajiado'), ('Kakamega', 'Kakamega'), ('Kericho', 'Kericho'), ('Kiambu', 'Kiambu'), ('Kilifi', 'Kilifi'), ('Kirinyaga', 'Kirinyaga'), ('Kisii', 'Kisii'), ('Kisumu', 'Kisumu'), ('Kitui', 'Kitui'), ('Kwale', 'Kwale'), ('Laikipia', 'Laikipia'), ('Lamu', 'Lamu'), ('Machakos', 'Machakos'), ('Makueni', 'Makueni'), ('Mandera', 'Mandera'), ('Meru', 'Meru'), ('Migori', 'Migori'), ('Marsabit', 'Marsabit'), ('Mombasa', 'Mombasa'), ('Muranga', 'Muranga'), ('Nairobi', 'Nairobi'), ('Nakuru', 'Nakuru'), ('Nandi', 'Nandi'), ('Narok', 'Narok'), ('Nyamira', 'Nyamira'), ('Nyandarua', 'Nyandarua'), ('Nyeri', 'Nyeri'), ('Samburu', 'Samburu'), ('Siaya', 'Siaya'), ('Taita Taveta', 'Taita Taveta'), ('Tana River', 'Tana River'), ('Tharaka Nithi', 'Tharaka Nithi'), ('Trans Nzoia', 'Trans Nzoia'), ('Turkana', 'Turkana'), ('Uasin Gishu', 'Uasin Gishu'), ('Vihiga', 'Vihiga'), ('Wajir', 'Wajir'), ('West Pokot', 'West Pokot')], max_length=150, null=True, verbose_name='County')),
                ('logo', cloudinary.models.CloudinaryField(max_length=255, verbose_name='logo')),
                ('health_department', models.CharField(blank=True, max_length=15, null=True, verbose_name='Health Department')),
                ('police_department', models.CharField(blank=True, max_length=15, null=True, verbose_name='Police Department')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Date Updated')),
                ('admin', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Admin')),
            ],
            options={
                'verbose_name_plural': 'Neighborhoods',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('bio', models.TextField()),
                ('email', models.EmailField(blank=True, max_length=100)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date Created')),
                ('date_updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Date Updated')),
                ('neighborhood', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='content.neighborhood', verbose_name='Hood')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name_plural': 'Profles',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, null=True, verbose_name='Title')),
                ('caption', models.CharField(max_length=2200, null=True, verbose_name='Caption')),
                ('category', models.CharField(choices=[('1', 'Crimes and Safety'), ('2', 'Health Emergency'), ('3', 'Recommendations e.g Plumber, mamafua'), ('4', 'Power Outages'), ('5', 'Lost and Found'), ('6', 'Death'), ('7', 'Event'), ('8', 'water')], max_length=150, null=True, verbose_name='Post Category')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date Created')),
                ('date_updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Date Updated')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Author')),
                ('neighborhood', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='content.neighborhood', verbose_name='Hood')),
                ('profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='content.profile', verbose_name='Profile')),
            ],
            options={
                'ordering': ['date_created'],
            },
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=20, null=True, verbose_name='Business Title')),
                ('description', models.CharField(max_length=150, null=True, verbose_name='Business Descritption')),
                ('logo', cloudinary.models.CloudinaryField(max_length=255, verbose_name='Business Logo/Image')),
                ('email', models.EmailField(max_length=254, null=True, verbose_name='Business Email')),
                ('business_type', models.CharField(choices=[('cleaning', 'cleaning'), ('grocery', 'grocery'), ('bakery', 'bakery'), ('salon', 'salon'), ('barbershop', 'barbershop'), ('butchery', 'butchery'), ('chemist', 'chemist'), ('general_shop', 'general_shop'), ('milk_atm', 'milk_atm')], max_length=50, null=True, verbose_name='Business Type')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Date Updated')),
                ('neighborhood', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='content.neighborhood', verbose_name='Hood')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Business owner')),
            ],
            options={
                'verbose_name_plural': 'Businesses',
            },
        ),
    ]
