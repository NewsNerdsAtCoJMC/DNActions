from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, parser_classes

from flashbriefing.models import FeedItem
from flashbriefing.serializers import FeedItemSerializer

import datetime

@csrf_exempt
@api_view(['GET'])
def flash_briefing(request, format=None):
    if request.method == 'GET':
        items = FeedItem.objects.all()
        serializer = FeedItemSerializer(items, many=False)
        return JsonResponse(serializer.data, safe=False)
