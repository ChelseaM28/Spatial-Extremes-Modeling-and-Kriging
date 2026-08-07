# Filename: covariance_models.py
# Author : Chelsea Momoh
# Date : 2026-08-06
# Version : 1.0
# Description : This script contains classes and methods for 
#               fitting a covariance model to the semivariogram via WLS.
# * - * - * - * - * - * - * - * - * - * - * - * - * - * - * -

class FitCovarianceModelsToSemivariogram():
    def __init__(self, semivariogram_data):
        self.semivariogram = semivariogram_data

    def fit_cov_models(self):
        # I don't think I need a separate class for each type of model.
        pass

    def choose_cov_model(self):
        # Will need RSS (residual sum of sqrs) for each in order to choose (according to Webster & Oliver)
        pass
