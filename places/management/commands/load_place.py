from places.models import Place
from django.core.management import BaseCommand
import requests
import os
from io import BytesIO


def get_response(url) -> object:
    response = requests.get(url)
    response.raise_for_status()
    return response


def save_place(place_properties) -> object:
    """ Save place in Db and return it as object."""

    place, _ = Place.objects.update_or_create(
        title=place_properties['title'],
        lon=place_properties['coordinates']['lng'],
        lat=place_properties['coordinates']['lat'],
        defaults={
            'short_description': place_properties['description_short'],
            'long_description': place_properties['description_long']}
        )
    place.save()
    return place


class Command(BaseCommand):
    help = 'Add locations from external web'

    def add_arguments(self, parser):
        """Url parametr of command."""
        parser.add_argument(
            'json_url', type=str, help='Url adress of json file')

    def handle(self, *args, **kwargs):
        """Save place object and related image objects.

        Fetch json data and save place and related images to the
        database. Information about json format located in README file.
        """
        url = kwargs['json_url']
        response = get_response(url).json()
        place = save_place(response)
        urls = response['imgs']
        for num, url in enumerate(urls, 0):
            response = get_response(url).content
            image = BytesIO(response)
            filename = os.path.basename(url)
            image_object = place.images.get_or_create(
                place=place.title,
                image_order=num)[0]
            image_object.save()
            image_object.image.save(filename, image, save=True)
