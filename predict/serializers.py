from rest_framework import serializers
from predict.models import MLAlgorithm
from predict.models import MLRequest


class MLAlgorithmSerializer(serializers.ModelSerializer):

    class Meta:
        model = MLAlgorithm
        read_only_fields = ("id", "name", "description", "code",
                            "version", "owner")
        fields = read_only_fields

class MLRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = MLRequest
        read_only_fields = (
            "id",
            "input_data",
            "full_response",
            "response",
            "parent_mlalgorithm",
        )
        fields =  (
            "id",
            "input_data",
            "full_response",
            "response",
            "feedback",
            "parent_mlalgorithm",
        )