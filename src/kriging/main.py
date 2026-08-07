# Filename: semivariogram.py
# Author : Chelsea Momoh
# Date : 2026-08-03
# Version : 1.0
# Description : This script will run each step of the kriging process.
# * - * - * - * - * - * - * - * - * - * - * - * - * - * - * -

from data_scripts.data_handling import DataHandler
from common.base import Preprocessing
from semivariogram import EmpiricalSemivariogram
from kriging import OrdinaryKriging

class Main:
    def __init__(self, filepath):
        self.filepath = filepath
        self.datahandler = DataHandler(self.filepath)
        self.filtered_data_object = self.datahandler.clean_filter_and_save()
        self.kriger = None  
        pass

    def main(self):
        location_pairs = None  # Need to decide how to pair stations
        GMM_predictions = self.filtered_data_object.construct_GMM()
        self.preprocessor = Preprocessing(self.filtered_data_object, location_pairs, GMM_predictions)
        self.semivari = EmpiricalSemivariogram(self.filtered_data_object)
        self.kriger = OrdinaryKriging(self.semivari.choose_covariance_model)
        # semivariogram global-esque variables
        # semivariogram sources of unreliability will be handled within the variogram script.
        
        # station_ids = filtered_data_object['station_ids']
        # location_pair_distances_dict = preprocessor.pairwise_distance_computation()
        block = self.kriger.block_kriging
        return block

    def LOOCV(self):
        pass
        
