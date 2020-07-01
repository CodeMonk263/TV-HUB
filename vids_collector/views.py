import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_react.settings')

import django
from django.shortcuts import render
django.setup()

from .models import Link
import sys
sys.path.insert(0, '../')
from vids_collector import vids_collector as vid

from .serializers import LinkSerializer
from rest_framework import generics

def populate(page_num):
    titles, hrefs = vid.get_vids("https://xmoviesforyou.video/page/" + str(page_num))
    for video in zip(titles,hrefs):
        title = video[0]
        href = video[1]
        title, href = Link.objects.get_or_create(title=title,href=href)

class LinkListCreate(generics.ListCreateAPIView):
    populate(1)
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    
