from django.shortcuts import render, redirect, reverse
from django.conf import settings

from apiproject.mixins import Directions


def route(request):
    """
    Basic view for routing
    """
    context = { "google_api_key": settings.GOOGLE_API_KEY, "base_country": settings.BASE_COUNTRY}
    return render(request, 'main/route.html', context)


def map(request):
    """
    Basic view for displaying a map
    """
    lat_a = request.GET.get("lat_a", None)
    long_a = request.GET.get("long_a", None)
    lat_b = request.GET.get("lat_b", None)
    long_b = request.GET.get("long_b", None)
    lat_c = request.GET.get("lat_c", None)
    long_c = request.GET.get("long_c", None)
    lat_d = request.GET.get("lat_d", None)
    long_d = request.GET.get("long_d", None)

    # only call API if all 4 addresses are added
    if lat_a and lat_b and lat_c and lat_d:
        directions = Directions(
            lat_a= lat_a,
            long_a=long_a,
            lat_b = lat_b,
            long_b=long_b,
            lat_c= lat_c,
            long_c=long_c,
            lat_d = lat_d,
            long_d=long_d
            )
    else:
        return redirect(reverse('main:route'))

    context = {
        "google_api_key": settings.GOOGLE_API_KEY,
        "base_country": settings.BASE_COUNTRY,
        "lat_a": lat_a,
        "long_a": long_a,
        "lat_b": lat_b,
        "long_b": long_b,
        "lat_c": lat_c,
        "long_c": long_c,
        "lat_d": lat_d,
        "long_d": long_d,
        "origin": f'{lat_a}, {long_a}',
        "destination": f'{lat_b}, {long_b}',
        "directions": directions,
    }

    return render(request, 'main/map.html', context)