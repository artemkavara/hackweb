from predict.models import MLAlgorithm


class MLRegistry:
    def __init__(self):
        self.endpoints = {}

    def add_algorithm(self, algorithm_name,
                    algorithm_version, algorithm_owner,
                    algorithm_description, algorithm_code, algorithm_object):

        # get algorithm
        database_object, algorithm_created = MLAlgorithm.objects.get_or_create(
                name=algorithm_name,
                description=algorithm_description,
                code=algorithm_code,
                version=algorithm_version,
                owner=algorithm_owner)
       
        # add to registry
        self.endpoints[database_object.id] = algorithm_object