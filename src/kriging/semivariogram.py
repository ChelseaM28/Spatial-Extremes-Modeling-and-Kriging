# Filename: semivariogram.py
# Author : Chelsea Momoh
# Date : 2026-08-03
# Version : 1.0
# Description : This script contains classes and methods for 
#               computing and plotting the empirical semivariogram.
# * - * - * - * - * - * - * - * - * - * - * - * - * - * - * -

# Not all of these methods will be performed, as the scope of the project will need to be limited.
class SourcesOfUnreliability:
    def __init__(self, data_object):
        self.data_object = data_object

    def sample_size(self):
        pass
        
    def lag_interval_and_bin_width(self):
        pass

    def marginal_distribution(self):
        pass

    def outliers(self):
        #NOTE: This is already a function in the preprocessing class. 
        #Later, I will decide whether to skip this or just reference the class in this method
        pass

    def anisotropy(self):
        pass

    def trend(self):
        pass


class EmpiricalSemivariogram:
    def __init__(self, data_object):
        self.data_object = data_object

    def compute_empirical_semivariogram(self):
        pass


class PlotEmpiricalSemivariogram:
    def __init__(self, data_object):
        self.data_object = data_object
        self.passed_to_plotting_class = None

    def plot_empirical_semivariogram(self):
        #self.passed_to_plotting_class = some operation
        Plotting(self.passed_to_plotting_class).plot_passed_data()
        print("Empirical Semivariogram plotted. Check output folder > graphics for the graph.")
        pass
