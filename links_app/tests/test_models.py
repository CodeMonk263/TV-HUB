from django.test import TestCase

from links_app.models import LinksModel


class TestLinksModel(TestCase):
    def setUp(self):
        self.links = LinksModel(page_num='1', title="XYZ", href='mixdrop_link')
        self.links.save()

    def test_movie_creation(self):
        self.assertEqual(LinksModel.objects.count(), 1)

    def test_movie_representation(self):
        self.assertEqual(self.links.title, str(self.links))