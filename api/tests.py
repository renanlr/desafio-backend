from django.contrib.auth import authenticate, get_user_model
from rest_framework.authtoken.models import Token
from django.test import TestCase
from rest_framework.test import APIRequestFactory
from rest_framework.test import force_authenticate
from rest_framework import status
from . import views
from api.models import Trip
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient, APITestCase


# Create your tests here.


class TripTestCase(APITestCase):

    @classmethod
    def setUpClass(cls):
        super(TripTestCase, cls).setUpClass()
        cls.client = APIClient()

    @classmethod
    def setUpTestData(cls):
        cls.alice = get_user_model().objects.create(username='Alice', password='123456')
        cls.bob = get_user_model().objects.create(username='Bob', password='Smith')
        Trip.objects.create(owner=cls.alice, start_date='2020-03-27T00:35:00Z', end_date='2020-03-27T00:35:00Z')
        Trip.objects.create(owner=cls.bob, start_date='2020-03-27T00:35:00Z', end_date='2020-03-27T00:35:00Z')

    def setUp(self):
        token = Token.objects.create(user=self.alice)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    def test_should_return_status_401_when_unauthorized(self):
        # setup
        # Erase credentials
        self.client.credentials()
        # execute
        response = self.client.get('/trips/')
        # verify
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_should_list_all_trips(self):
        # execute
        response = self.client.get('/trips/')
        # verify
        assert response.status_code == status.HTTP_200_OK
        assert response.data.get('count') == 1

    def test_should_classify_trip(self):
        # setup
        trip = Trip.objects.create(owner=self.alice, start_date='2020-03-27T00:35:00Z', end_date='2020-03-27T00:35:00Z')
        # execute
        response = self.client.put('/trips/' + str(trip.id)+'/', {"classification": 1, "rating": 5})
        # verify
        assert response.status_code == status.HTTP_200_OK
        assert response.data.get('classification') == 1
        assert response.data.get('rating') == 5

    def test_should_create_trip(self):
        # setup
        trip = Trip.objects.create(owner=self.alice, start_date='2020-03-27T00:35:00Z',
                                   end_date='2020-03-27T00:35:00Z')
        # execute
        response = self.client.post('/trips/', {"start_date":"2020-03-27T00:35:00Z",
                                                "end_date":"2020-03-27T00:35:00Z",
                                                "classification": 1, "rating": 5})
        # verify
        assert response.status_code == status.HTTP_200_OK
        assert response.data.get('count') == 2

    def test_return_400_when_trip_unexistent(self):
        # setup
        trip = Trip.objects.create(owner=self.alice, start_date='2020-03-27T00:35:00Z', end_date='2020-03-27T00:35:00Z')
        # execute
        response = self.client.put('/trips/' + str(trip.id)+'/', {"classification": 1, "rating": 5})
        # verify
        assert response.status_code == status.HTTP_200_OK
        assert response.data.get('classification') == 1
        assert response.data.get('rating') == 5

