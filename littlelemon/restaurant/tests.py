from django.test import TestCase
from restaurant.models import MenuItem
from rest_framework.test import APIClient
from django.contrib.auth.models import User
import json

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(name="IceCream", price=80)
        self.assertEqual(str(item), "IceCream : 80")

class MenuViewTest(TestCase):
  def setUp(self):
      self.user = User.objects.create_user(username='testuser', password='testpass')

      # Create a few test instances of the Menu model
      self.item1 = MenuItem.objects.create(name="IceCream", price=80)
      self.item2 = MenuItem.objects.create(name="Cake", price=90)
      self.client = APIClient()

      # Obtain a token
      response = self.client.post('/auth/token/login/', {'username': 'testuser', 'password': 'testpass'})
      self.token = response.data['auth_token']

  def test_get_all(self):
      # Retrieve all the Menu objects
      response = self.client.get('/restaurant/menu/', format='json', HTTP_AUTHORIZATION='Token ' + self.token)

      # Check status code
      self.assertEqual(response.status_code, 200)

      # Deserialize the response content
      data = json.loads(response.content)

      # Check if the serialized data equals the response
      self.assertEqual(data['results'][0]['name'], self.item1.name)
      self.assertEqual(float(data['results'][0]['price']), float(self.item1.price))
      self.assertEqual(data['results'][1]['name'], self.item2.name)
      self.assertEqual(float(data['results'][1]['price']), float(self.item2.price))