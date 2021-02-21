import xgboost as xgb

import pandas as pd
import numpy as np

class BookRatePredictor:
    def __init__(self):
        path_to_artifacts = ""
        self.model= xgb.XGBRegressor()
        self.model.load_model(path_to_artifacts + "did_our_best.model")
        

    def preprocessing(self, input_data):
        # JSON to pandas DataFrame
        input_data = pd.DataFrame(input_data, index=[0])

        # fill missing values
        top_genres = ['genre_(Biography)', 'genre_(Childrens)',
       'genre_(Classics)', 'genre_(Contemporary)', 'genre_(Cultural)',
       'genre_(European Literature)', 'genre_(Fantasy)', 'genre_(Fiction)',
       'genre_(Historical)', 'genre_(Historical Fiction)', 'genre_(History)',
       'genre_(Literature)', 'genre_(Mystery)', 'genre_(Nonfiction)',
       'genre_(Paranormal)', 'genre_(Religion)', 'genre_(Romance)',
       'genre_(Science Fiction)', 'genre_(Sequential Art)', 'genre_(Thriller)',
       'genre_(Young Adult)', 'genre_(nan)', 'genre_(Other)',]
        top_formats = ['format_(soft_cover)', 'format_(hard_cover)', 'format_(ebook)',
       'format_(audio)', 'format_(other)',]
        for genre in top_genres:
            input_data.loc[:,genre] = np.zeros((len(input_data)))
        for form in top_formats:
            input_data.loc[:,form] = np.zeros((len(input_data)))
        
        for i in range(len(input_data)):
            genres_list = input_data.iloc[i]['book_genre'].split('|')
            for genre in genres_list:
                if genre in top_genres:
                    input_data.at[i, genre] = 1
            format_list = input_data.iloc[i]['book_format'].split('|')
            for form in format_list:
                if form in top_formats:
                    input_data.at[i, form] = 1 
      
        input_data = input_data.drop(columns = ['book_genre', 'book_format'])
        return input_data

    def estim(self, input_data):
        return self.model.predict(input_data)

    def postprocessing(self, input_data):
        return {"estimated_rate": input_data, "status": "OK"}

    def compute_prediction(self, input_data):
        try:
            input_data = self.preprocessing(input_data)
            estimation = self.estim(input_data)  # only one sample
            estimation = self.postprocessing(estimation)
            
        except Exception as e:
            return {"status": "Error", "label": str(e)}

        return estimation