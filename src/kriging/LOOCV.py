# Filename: LOOCV.py
# Author : Chelsea Momoh
# Date : 2026-08-06
# Version : 1.0
# Description : This script contains classes and methods for 
#               implementing Leave-One-Out-Cross-Validation.
# * - * - * - * - * - * - * - * - * - * - * - * - * - * - * -

from kriging import OrdinaryKriging

class LOOCV:
    def __init__(self, some_kriging_data, some_original_data):
        self.some_original_data = some_original_data
        pass

    def cross_validation(self):
        OrdinaryKriging.punctual_kriging(self.some_original_data)
        # Will need to perform punctual kriging here.
        pass
