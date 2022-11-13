from django.test import TestCase

# Create your tests here.
from .models import Contact



class TestContactModel(TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.data1 ={
            "name": "John",
            "email": "john",
            "subject":"problem var",
            "message": "problem var!!!!!!!",
                } 
        Contact.objects.create(**cls.data1)
    
    def test_created_data(self):
        contact = Contact.objects.first()
        self.assertEqual(contact.name, self.data1['name'])
        
        
    @classmethod
    def tearDownClass(cls):
        Contact.objects.first().delete()
        del cls.data1