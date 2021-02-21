# backend/server/apps/endpoints/urls.py file
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from predict.views import MLAlgorithmViewSet
from predict.views import MLRequestViewSet
from predict.views import PredictView

router = DefaultRouter(trailing_slash=False)
router.register(r"mlalgorithms", MLAlgorithmViewSet, basename="mlalgorithms")
router.register(r"mlrequests", MLRequestViewSet, basename="mlrequests")

urlpatterns = [
    url(r"^api/v1/", include(router.urls)),
]


urlpatterns = [
    url(r"^api/v1/", include(router.urls)),
    # add predict url
    url(
        r"^api/v1/(?P<algorithm_name>.+)/estim$", PredictView.as_view(), name="estim"
    ),
]