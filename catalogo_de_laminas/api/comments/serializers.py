import logging
import datetime

from rest_framework import serializers

from catalogo_de_laminas.wised import models as wised_models

logger = logging.getLogger(__name__)


class WpCommentsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = wised_models.Wp2Popularpostsdata
        fields = (
            'postid',
            'day',
            'last_viewed',
            'pageviews',
        )

    def validate(self, data):
        data['day'] = datetime.datetime.now()
        return data
