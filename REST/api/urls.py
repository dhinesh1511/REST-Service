# -*- coding: utf-8 -*-
"""
Created on Sat May 28 12:18:31 2022

"""

from django.urls import include, path



from api.views import BranchView,SearchView

urlpatterns = [
   path('branch?<str:q>&<int:limit>&<int:offset>', BranchView.as_view()),
   path('search?<str:q>&<int:limit>&<int:offset>', SearchView.as_view()),
]