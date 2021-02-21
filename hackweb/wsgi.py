"""
WSGI config for hackweb project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')
application = get_wsgi_application()

# ML registry
import inspect
from ml.registry import MLRegistry
from ml.predictor.predictor import BookRatePredictor

try:
    registry = MLRegistry() # create ML registry
    # Random Forest classifier
    pred = BookRatePredictor()
    # add to ML registry
    registry.add_algorithm( algorithm_object = pred,
        algorithm_name = "xgboost",
        algorithm_version = "1.0.1",
        algorithm_owner = "from kpi import iasa",
        algorithm_description = "Book rate estimator",
        algorithm_code = inspect.getsource(BookRatePredictor))

except Exception as e:
    print("Exception while loading the algorithms to the registry,", str(e))