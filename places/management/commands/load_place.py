from places.models import Place
from django.core.management import BaseCommand
import requests
import os
from io import BytesIO


def get_response(url):
    response = requests.get(url)
    response.raise_for_status()
    return response


def save_place(place_properties):
    place = Place.objects.get_or_create(
        title=place_properties['title'],
        description_short=place_properties['description_short'],
        description_long=place_properties['description_long'],
        lon=place_properties['coordinates']['lng'],
        lat=place_properties['coordinates']['lat'],
    )[0]
    place.save()
    return place


class Command(BaseCommand):
    help = 'Add locations from external web'

    def add_arguments(self, parser):
        parser.add_argument('json_url', type=str, help='Url adress of json file')

    def handle(self, *args, **kwargs):
        url = kwargs['json_url']
        response = get_response(url).json()
        place = save_place(response)
        urls = response['imgs']
        for num, url in enumerate(urls, 0):
            response = get_response(url).content
            image = BytesIO(response)
            filename = os.path.basename(url)
            image_object = place.images.get_or_create(
                title=place.title,
                image_order=num)[0]
            image_object.save()
            image_object.image.save(filename, image, save=True)








