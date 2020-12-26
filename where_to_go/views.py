from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from places.models import Place, Image
from django.urls import reverse


def get_json(request):
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
                    "title": place.short_title(),
                    "placeId": place.id,
                    "detailsUrl": reverse('place_properties', args=(place.id,))
                }
            }
        )
    return geo_json


def index(request):
    geo_json = get_json(request)
    data = {'geo_json': geo_json}
    return render(request, 'index.html', context=data)


def place_properties(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    place_properties = {
        "title": place.title,
        "imgs": [image.image.url for image in place.images.all()],
        "description_short": place.description_short,
        "description_long": place.description_long.replace("\\", ''),
        "coordinates": {
            "lat": place.lat,
            "long": place.lon
        }
    }
    return JsonResponse(place_properties, safe=False, json_dumps_params={'ensure_ascii': False, 'indent': 4})
