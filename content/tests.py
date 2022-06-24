from django.test import TestCase
from content.models import Neighborhood, Post, Profile, Business
from django.contrib.auth.models import User
# Create your tests here.
user = User.objects.get(id=1)
profile = Profile.objects.get(id=1)

class TestNeighborhood(TestCase):
    def setUp(self):
        self.new_neigborhood=Neighborhood(name = "Hood", location="Ngong", county='Nairobi', logo="default.jpg", hood_admin=user)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_neigborhood,Neighborhood))

    def test_save_image(self):
        new_hood=self.new_neigborhood
        new_hood.save_hood()
        posts=Neighborhood.get_hoods()
        self.assertTrue(len(posts)>0)


    def update_image(self):
        new_hood=self.save_hood()
        new_hood.update_hood()
        posts=Neighborhood.get_hoods()
        self.assertTrue(len(posts)==0)

    # def test_delete_image(self):
    #     new_hood=self.new_neigborhood
    #     new_hood.delete_hood()
    #     posts=Neighborhood.get_hoods()
    #     self.assertTrue(len(posts)==0)

class TestBusiness(TestCase):
    def setUp(self):
        self.new_business=Business(title = "Biz", description="Ngong", email='ray@gmail.com', neighborhood="default.jpg", owner=profile)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_business,Business))

    def test_save_image(self):
        new_biz=self.new_business
        new_biz.save_business()
        posts=Business.get_businesses()
        self.assertTrue(len(posts)>0)

    def update_image(self):
        new_biz=self.new_business
        new_biz.update_busness()
        posts=Business.get_businesses()
        self.assertTrue(len(posts)==0)
        

    def test_delete_image(self):
        new_biz=self.new_business
        new_biz.delete_business()
        posts=Business.get_businesses()
        self.assertTrue(len(posts)==0)

