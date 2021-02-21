from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import mixins


from predict.models import MLAlgorithm
from predict.serializers import MLAlgorithmSerializer


from predict.models import MLRequest
from predict.serializers import MLRequestSerializer

class MLAlgorithmViewSet(
    mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    serializer_class = MLAlgorithmSerializer
    queryset = MLAlgorithm.objects.all()


def deactivate_other_statuses(instance):
    old_statuses = MLAlgorithmStatus.objects.filter(parent_mlalgorithm = instance.parent_mlalgorithm,
                                                        created_at__lt=instance.created_at,
                                                        active=True)
    for i in range(len(old_statuses)):
        old_statuses[i].active = False
    MLAlgorithmStatus.objects.bulk_update(old_statuses, ["active"])


class MLRequestViewSet(
    mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet,
    mixins.UpdateModelMixin
):
    serializer_class = MLRequestSerializer
    queryset = MLRequest.objects.all()

import json
from numpy.random import rand
from rest_framework import views, status
from rest_framework.response import Response
from ml.registry import MLRegistry
from hackweb.wsgi import registry
'''
... the rest of the backend/server/apps/endpoints/views.py file ...
'''

class PredictView(views.APIView):
    def post(self, request, algorithm_name, format=None):

        algs = MLAlgorithm.objects.all()
        print(algs)
        algorithm_object = registry.endpoints[algs[1].id]
        prediction = algorithm_object.compute_prediction(request.data)


        estim = prediction["estimated_rate"] if "estimated_rate" in prediction else "error"
        ml_request = MLRequest(
            input_data=json.dumps(request.data),
            full_response=prediction,
            response=str(estim),
            feedback="",
            parent_mlalgorithm=algs[1],
        )
        ml_request.save()

        prediction["request_id"] = ml_request.id

        return Response(prediction)