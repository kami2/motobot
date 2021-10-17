from django.shortcuts import render
from .models import DataBikes
from rest_framework import viewsets
from rest_framework import permissions
from apimoto.serializers import DataBikesSerializer
# Create your views here.


class DataBikesViewSet(viewsets.ModelViewSet):
    serializer_class = DataBikesSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = DataBikes.objects.all()
        model = self.request.query_params.get('model')
        if model is not None:
            queryset = queryset.filter(model=model)
        return queryset

