from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from places.models import Place


def get_json():
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
                    "detailsUrl":
                        "https://raw.githubusercontent.com/devmanorg/where-to-go-frontend/master/places/moscow_legends.json"
                }
            }
        )
    return geo_json


def index(request):
    geo_json = get_json()
    data = {'geo_json': geo_json}
    return render(request, 'index.html', context=data)


def place_view(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    return HttpResponse(f'{place.title}')
