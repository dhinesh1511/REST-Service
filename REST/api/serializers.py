# -*- coding: utf-8 -*-
"""
Created on Sat May 28 11:54:03 2022

"""

from rest_framework import serializers

from api.models import branches

class BranchesSerializer(serializers.ModelSerializer):
    class Meta:
        model = branches
        fields = ('ifsc','bank_id','branch','address','city','district','state')