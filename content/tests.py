from django.test import TestCase
from content.models import Neighborhood, Post, Profile, Business
from django.contrib.auth.models import User
# Create your tests here.
user = User.objects.get(id=1)
profile = Profile.objects.get(id=1)

class TestNeighborhood(TestCase):
    def setUp(self):
        self.new_neigborhood=Neighborhood(title = "Hood", location="Ngong", county='Nairobi', Neighborhood_logo="default.jpg", hood_admin=user)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_neigborhood,Neighborhood))

    def test_save_image(self):
        new_hood=self.new_neigborhood
        new_hood.create_neigborhood()
        posts=Neighborhood.get_neighborhoods()
        self.assertTrue(len(posts)>0)


    def update_image(self):
        new_hood=self.new_neigbourhood
        new_hood.update_neighbourhood()
        posts=Neighborhood.get_neighbourhoods()
        self.assertTrue(len(posts)==0)

    def test_delete_image(self):
        new_hood=self.new_neigborhood
        new_hood.delete_neigborhood()
        posts=Neighborhood.get_neighborhoods()
        self.assertTrue(len(posts)==0)

class TestBusiness(TestCase):
    def setUp(self):
        self.new_business=Business(name = "Biz", description="Ngong", email='ray@gmail.com', neighbourhood="default.jpg", owner=profile)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_business,Business))

    def test_save_image(self):
        new_biz=self.new_business
        new_biz.create_business()
        posts=Business.get_businesses()
        self.assertTrue(len(posts)>0)

    def update_image(self):
        new_biz=self.new_business
        new_biz.update_business()
        posts=Business.get_businesses()
        self.assertTrue(len(posts)==0)

    def test_delete_image(self):
        new_biz=self.new_business
        new_biz.delete_business()
        posts=Business.get_businesses()
        self.assertTrue(len(posts)==0)

