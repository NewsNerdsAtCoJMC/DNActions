from rest_framework import serializers
from flashbriefing.models import FeedItem

class FeedItemSerializer(serializers.ModelSerializer):
    uid = serializers.CharField()
    updateDate = serializers.DateTimeField()
    titleText = serializers.CharField()
    mainText = serializers.CharField()
    redirectionUrl = serializers.URLField()
    class Meta:
        model = FeedItem
        fields = ('uid', 'updateDate', 'titleText', 'mainText', 'redirectionUrl')
