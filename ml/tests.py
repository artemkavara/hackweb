from django.test import TestCase

from ml.predictor.predictor import BookRatePredictor
import inspect
from ml.registry import MLRegistry

class MLTests(TestCase):
    def test_rf_algorithm(self):
        input_data = {
            "book_pages":67,
            "book_review_count":1000,
            "book_rating_count":251,
            "book_genre": "genre_(Biography)",
            "book_format": 'format_(soft_cover)',
            "authors_number":2,
            "title_len":5,
        }
        my_alg = BookRatePredictor()
        response = my_alg.compute_prediction(input_data)
        self.assertEqual('OK', response['status'])
    
    def test_registry(self):
        registry = MLRegistry()
        self.assertEqual(len(registry.endpoints), 0)
        algorithm_object = BookRatePredictor()
        algorithm_name = "xgboost"
        algorithm_version = "1.0.1"
        algorithm_owner = "from kpi import iasa"
        algorithm_description = "Book rate estimator"
        algorithm_code = inspect.getsource(BookRatePredictor)
        # add to registry
        registry.add_algorithm(algorithm_name,
                    algorithm_version, algorithm_owner,
                    algorithm_description, algorithm_code, algorithm_object)
        # there should be one endpoint available
        self.assertEqual(len(registry.endpoints), 1)