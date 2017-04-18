from django.http import HttpResponse, JsonResponse
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
import random

from discounts.models import Deal
from discounts.serializers import DealSerializer

@csrf_exempt
@api_view(['GET','POST'])
@parser_classes((JSONParser,))
def deal_list(request, format=None):
    if request.method == 'GET':
        deals = Deal.objects.all()
        serializer = DealSerializer(deals, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        try:
            dealtype = request.data['result']['parameters']['deal-type'][0]
        except:
            dealtype = None
        try:
            foodtype = request.data['result']['parameters']['food-types'][0]
        except:
            foodtype = None
        try:
            drinktype = request.data['result']['parameters']['drink-types'][0]
        except:
            drinktype = None
        if foodtype:
            deals = Deal.objects.filter(food_type__name=foodtype)
            serializer = DealSerializer(deals, many=True)
            return JsonResponse(random.choice(serializer.data), safe=False)
        elif drinktype:
            deals = Deal.objects.filter(drink_type__name=drinktype)
            serializer = DealSerializer(deals, many=True)
            return JsonResponse(random.choice(serializer.data), safe=False)
        elif dealtype:
            deals = Deal.objects.filter(deal_type__name=dealtype)
            serializer = DealSerializer(deals, many=True)
            return JsonResponse(random.choice(serializer.data), safe=False)
        else:
            return Response({'received data': request.data})
