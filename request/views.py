from django.http import Http404
from jsonview.decorators import json_view

from . models import ColourRequest
from colour.models import Colour

def colours_from_tweet(tweet):
    colours = []
    for c in Colour.objects.all():
        if c.name.lower() in tweet.lower():
            colours.append(c)
    return colours

@json_view
def process_tweet(request):
    tweet = request.GET['tweet']
    user = request.GET['from']

    colours = colours_from_tweet(tweet)
    if not colours:
        raise Http404

    for colour in colours:
        ColourRequest.objects.create(
            colour=colour,
            source="Twitter",
            message=tweet,
            user=user
        )

    return {'success': True, 'colours': [colour.name for colour in colours]}

@json_view
def process_message(request):
    tweet = request.GET['colours']

    colours = colours_from_tweet(tweet)
    if not colours:
        raise Http404

    for colour in colours:
        ColourRequest.objects.create(
            colour=colour,
            source="Studio",
            message=tweet,
            user="Studio"
        )

    return {'success': True, 'colours': [colour.name for colour in colours]}

