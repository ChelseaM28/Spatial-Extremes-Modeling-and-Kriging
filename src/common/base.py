# Filename : base.py
# Author : Chelsea Momoh
# Date : 2026-08-03
# Version : 1.0
# Description : This script contains different scripts common to the kriging and tail extremes processes.
# * - * - * - * - * - * - * - * - * - * - * - * - * - * - * -


# Preporcessing's data object should be a filtered dataframe including only the chosen earthquake.
class Preprocessing:
    def __init__(self, filtered_data_object):
        self.dataframe = filtered_data_object

    def detect_outliers(self):
        pass

    def pairwise_distance_computation(self):
        pass


class Plotting:
    def __init__(self, passed_data):
        self.passed_data = passed_data

    def plot_passed_data(self):
        # some function using the passed data. Will be used for ALL graphs, not just semivoriogram.
        # if this adds unnecessary complexity, I will not use this.
        pass
