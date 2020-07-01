from .serializers import *
from .models import *
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
import time
from django.http import Http404

import sys
sys.path.insert(0, '../')
from vids_collector import vids_collector as vid

class ShowSerializerViewSet(viewsets.ModelViewSet):
    # mapping serializer into the action
    serializer_class = ShowSerializer
    queryset = ShowsModel.objects.all()

    @action(detail=False, methods=['get'])
    def get_shows(self, request, pk=None):
        if request.method == 'GET':
            ShowsModel.objects.all().delete()
            titles, hrefs, thumbnails_src = vid.get_shows("https://wtv.unblockit.id/")

            for show in zip(titles, hrefs, thumbnails_src):
                ShowsModel.objects.create(title=show[0][1:], href=show[1], thumbnail_src=show[2])

            data = ShowsModel.objects.first()

            serializer = ShowSerializer(data=data.__dict__)

            if serializer.is_valid():
                return Response("Success", status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'])
    def search_shows(self, request, pk=None):
        if request.method == 'POST':
            search_term = request.data["search"]
            ShowsModel.objects.all().delete()
            titles, hrefs = vid.search_shows("https://wtv.unblockit.id/searchresults.php?s=", search_term)
            for show in zip(titles, hrefs):
                ShowsModel.objects.create(title=show[0], href=show[1])
            data = ShowsModel.objects.first()
            serializer = ShowSerializer(data=data.__dict__)
            if serializer.is_valid():
                return Response("Success", status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SeasonSerializerViewSet(viewsets.ModelViewSet):
    serializer_class = SeasonSerializer
    queryset = SeasonModel.objects.all()

    @action(detail=False, methods=['post'])
    def get_seasons(self, request, pk=None):
        if request.method == 'POST':
            hrefs = vid.get_seasons(request.data["href"])
            count = len(hrefs)
            try:
                if count > 1:
                    href = hrefs[0]
                else:
                    href = hrefs
                data = get_object_or_404(SeasonModel, href=href)
            except Http404:
                SeasonModel.objects.all().delete()
                for href in hrefs:
                    SeasonModel.objects.create(title=request.data["title"], season=str(count), href=href)
                    count = count-1
                data = SeasonModel.objects.first()

            serializer = SeasonSerializer(data=data.__dict__)
            if serializer.is_valid():
                return Response("Success", status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EpisodeSerializerViewSet(viewsets.ModelViewSet):
    serializer_class = EpisodeSerializer
    queryset = EpisodesModel.objects.all()

    @action(detail=False, methods=['post'])
    def get_episodes(self, request, pk=None):
        if request.method == 'POST':
            hrefs = vid.get_eps(request.data["href"])
            count = len(hrefs)
            try:
                if count > 1:
                    href = hrefs[0]
                else:
                    href = hrefs
                data = get_object_or_404(EpisodesModel, href=href)
            except Http404:
                EpisodesModel.objects.all().delete()
                for href in hrefs:
                    EpisodesModel.objects.create(title=request.data["title"], episode=str(count), href=href, season=request.data["season"])
                    count = count-1
                data = EpisodesModel.objects.first()

            serializer = EpisodeSerializer(data=data.__dict__)
            if serializer.is_valid():
                return Response("Success", status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @action(detail=True, methods=['get'])
    def watch_episode(self, request, pk=None):
        if request.method == 'GET':
            video = get_object_or_404(EpisodesModel, pk=self.kwargs['pk'])
            video.href = vid.get_link(video.href)
            video.save()

            serializer = EpisodeSerializer(data=video.__dict__)
            if serializer.is_valid():
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
