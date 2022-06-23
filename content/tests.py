from django.test import TestCase
from content.models import Neighborhood, Post, Profile, Business
from django.contrib.auth.models import User
# Create your tests here.
user = User.objects.get(id=1)
profile = Profile.objects.get(id=1)

class TestNeighborhood(TestCase):
    def setUp(self):
        self.new_neigbourhood=Neighborhood(title = "Hood", location="Ngong", county='Nairobi', Neighborhood_logo="default.jpg", hood_admin=user)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_neigbourhood,Neighborhood))
