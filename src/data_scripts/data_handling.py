# Filename : data_load.py
# Author : Chelsea Momoh
# Date : 2026-08-03
# Version : 1.0
# Description : This script contains the data class for loading and cleaning data.
# * - * - * - * - * - * - * - * - * - * - * - * - * - * - * -



class DataHandler:
    def __init__(self, filepath):
        self.filepath = filepath
        self.dataframe = pd.read_csv(filepath)
        self.mini_dataframe = self.dataframe.head(10)
        self.filtered = None
        self.output_path = "/workspaces/Spatial-Geostatistics-Analysis/data/raw/processed"

   def clean_data(self, dataframe):
        # Figure how to handle missing data and data types. No outlier detection in this step.
        #self.dataframe = drop na
        #other cleaning steps added here
        return self.dataframe
   
   def test_clean_data(self):
        self.tested_cleaned_data = self.clean_data(self.mini_dataframe)
        #This will print, in terminal, about 10 rows of the dataframe after a test cleaning process.
        print(f"Cleaned First Ten Rows of Your Dataset.\noriginal dataset is unmodified:\n{self.tested_cleaned_data.head(10)}")
    
    def save_cleaned_to_json(self):
        self.dataframe.to_json(self.output_path + "/cleaned_data.json", orient='records', lines=True)
    
    def filter_to_earthquake(self):
    # This function will find the earthquake with the most stations reporting data.
    # It will return the earthquake ID and the number of stations reporting data.
    self.dataframe = #some operation to choose earthquake. Can be in one line if it's simple
    self.filtered = self.dataframe
    return self.filtered

    def save_filtered_to_json(self):
        self.filtered.to_json(self.output_path + "/filtered_data.json", orient='records', lines=True)

    def clean_filter_and_save(self):   
        self.dataframe = self.clean_data(self.dataframe)
        self.filtered = self.filter_to_earthquake()
        self.save_filtered_to_json()
        return self.filtered
        

