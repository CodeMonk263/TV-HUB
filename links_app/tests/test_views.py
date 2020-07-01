from django.shortcuts import reverse

from rest_framework.test import APITestCase

from links_app.models import LinksModel


class TestNoteApi(APITestCase):
    def setUp(self):
        # create movie
        self.links = LinksModel(page_num='1',title="XYZ", href='mixdrop_link')
        self.links.save()

    def test_link_creation(self):
        response = self.client.post(reverse('get_links'), {
            'page_num': '8'
        })

        # assert new movie was added
        self.assertEqual(LinksModel.objects.count(), 2)

        # assert a created status code was returned
        self.assertEqual(201, response.status_code)

    def test_getting_links(self):
        response = self.client.get(reverse('get_links'), format="json")
        self.assertEqual(len(response.data), 1)

    def test_updating_movie(self):
        response = self.client.put(reverse('get_links', kwargs={'pk': 1}), {
            'page_num': '8',
            'title': 'updated_title',
            'href': 'updated_href'
        }, format="json")

        # check info returned has the update
        self.assertEqual('updated_title', response.data['title'])

    def test_deleting_movie(self):
        response = self.client.delete(reverse('get_links', kwargs={'pk': 1}))

        self.assertEqual(204, response.status_code)