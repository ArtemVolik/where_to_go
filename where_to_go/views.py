"""Main page of application."""

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from places.models import Place
from django.urls import reverse


def get_places_json(request):
    """Make geo_json with places data from DB."""
    geo_json = {
        "type": "FeatureCollection",
        "features": []
    }
    places = Place.objects.all()
    for place in places:
        geo_json['features'].append(
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [place.lon, place.lat]
                },
                "properties": {
                    "title": place.short_title,
                    "placeId": place.id,
                    "detailsUrl":
                        reverse('place_properties', args=(place.id,))
                }
            }
        )
    return geo_json


def index(request):
    """Render the main page."""
    geo_json = get_places_json(request)
    locations = {'geo_json': geo_json}
    return render(request, 'index.html', context=locations)


def place_properties(request, place_id):
    """Return Place properties in Json.

    Using for 'places/<int:place_id>/' page
    """
    place = get_object_or_404(Place, id=place_id)
    place_properties = {
        "title": place.title,
        "imgs": [image.image.url for image in place.images.all()],
        "description_short": place.short_description,
        "long_description": place.long_description,
        "coordinates": {
            "lat": place.lat,
            "long": place.lon
        }
    }
    return JsonResponse(
        place_properties, safe=False,
        json_dumps_params={'ensure_ascii': False, 'indent': 4})
