from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response
from rest_framework.views import APIView
from api.serializers import BranchesSerializer
from api.models import branches
from django.http import Http404

class BranchView(APIView):
    def get(self, request,q=None,limit=0,offset=0):
        queryset = branches.objects.filter(branch__icontains=q).order_by('ifsc')[offset:offset:limit]
        if queryset:
            serializer = BranchesSerializer(queryset, many=True)
            return Response(Response(serializer.data))
        raise Http404("No matches for the given query")

class SearchView(APIView):
    def get(self, request,q=None,limit=0,offset=0):
        queryset = (branches.objects.filter(branch__icontains=q) |
                    branches.objects.filter(ifsc__icontains=q) |
                    branches.objects.filter(bank_id__icontains=q) |
                    branches.objects.filter(city__icontains=q) |
                    branches.objects.filter(state__icontains=q) |
                    branches.objects.filter(address__icontains=q) |
                    branches.objects.filter(district__icontains=q)).order_by('ifsc')[offset:offset:limit]
        if queryset:
            serializer = BranchesSerializer(queryset, many=True)
            return Response(Response(serializer.data))
        raise Http404("No matches for the given query")