from rest_framework import mixins
from rest_framework import generics
from rest_framework.response import Response
from .models import Trip
from .serializers import TripSerializer
from rest_framework.permissions import IsAuthenticated
from api.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework import status


# Create your views here.

class TripList(mixins.ListModelMixin,
               mixins.CreateModelMixin,
               generics.GenericAPIView):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    serializer_class = TripSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def get_queryset(self):
        """
        This view should return a list of all the trips
        for the currently authenticated user.
        """
        user = self.request.user
        return Trip.objects.filter(owner=user)


class TripDetail(mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin,
                 generics.GenericAPIView):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    queryset = Trip.objects.all()
    serializer_class = TripSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


