from django_elasticsearch_dsl_drf.serializers import DocumentSerializer

from .documents import *


class FNIDocumentSerializer(DocumentSerializer):
    class Meta:
        document = FNIDocument
        fields = (
            'id',
            'food_name',
            'food_group',
            'food_amount',
            'calorie',
            'carbs',
            'protein',
            'fat',
            'sugar',
            'salt',
            'cholesterol',
            'saturated_fatty_acid',
            'trans_fat'
        )
