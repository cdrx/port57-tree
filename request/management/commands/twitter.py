from __future__ import division

from django.conf import settings
from django.core.management.base import BaseCommand

from TwitterAPI import TwitterAPI

from request.models import ColourRequest
from request.views import colours_from_tweet


class Command(BaseCommand):
    def handle(self, *args, **options):
        twitter = TwitterAPI(settings.CONSUMER_KEY,
                             settings.CONSUMER_SECRET,
                             settings.ACCESS_TOKEN_KEY,
                             settings.ACCESS_TOKEN_SECRET)

        r = twitter.request('statuses/filter', {'track': "port57tree"})
        for tweet in r:
            if 'text' in tweet:
                print tweet
                print tweet['user']['screen_name'], ":", tweet['text']
                colours = colours_from_tweet(tweet['text'])
                for colour in colours:
                    ColourRequest.objects.create(
                        colour=colour,
                        source="Twitter",
                        message=tweet['text'],
                        user=tweet['user']['screen_name']
                    )
