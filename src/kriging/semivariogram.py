# Filename: semivariogram.py
# Author : Chelsea Momoh
# Date : 2026-08-03
# Version : 1.0
# Description : This script contains classes and methods for 
#               computing and plotting the empirical semivariogram.
# * - * - * - * - * - * - * - * - * - * - * - * - * - * - * -

from common.base import Plotting, Preprocessing
import numpy as np

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
    def __init__(self, filtered_data_object): 
        self.data_object = filtered_data_object  # Filtered to chosen earhquake only + outliers removed.
        self.locations = []
        self.location_pairs = []  # Will likely be location pair coordinates... I think.
        self.location_pair_distances = Preprocessing.pairwise_distance_computation(self.data_object)
        # I am using peak ground acceleration as my parameter of interest with the 
        # assumption that professionals in industry would find this metric more useful.
        # It is "a natural simple design parameter since it can be related 
        # to a force and for simple design" - USGS Earthquake Hazards 201
        self.PGA_true = {} 
        self.PGA_predicted = {}
        self.log_PGA_trues = []
        
        self.residuals_sum = []
        self.semivariogram = []  # This is the experimental variogram referenced in literature.
        self.station_variance = {}

    def construct_GMM(self):
        # Model construction belongs here.
        # self.PGA_predicted for each station is updated --> given by GMM models
        # self.station_variance for each station is updated --> given by GMM models
        # These may end up being rearranged into tuples of pairs OR a dictionary

        # Now I need a residual for each station pair.
        for station_1, station_2 in self.location_pairs:
            self.residuals_sum.append(
                ((self.log_PGA_true[station_1]-np.log(self.PGA_predicted[station_1]))/self.station_variance[station_1]), 
                ((self.log_PGA_true[station_2]-np.log(self.PGA_predicted[station_2]))/self.station_variance[station_2])
                )
        return self.residuals_sum  # Should now be a list of tuples in the same order as location pairs.

    def compute_empirical_semivariogram(self): 
        # I need to check when this one is supposed to be used.
        self.semivariogram = 0.5*(1/len(self.station_pairs))*sum(self.residuals_sum)**2
        return self.semivariogram

    def spherical_empirical_semivariogram(self):
        pass
    
    def exponential_empirical_semivariogram(self):
        pass

    def power_empirical_semivariogram(self):
        pass


class PlotEmpiricalSemivariogram:  # I will figure this out later.
    def __init__(self, data_object):
        self.data_object = data_object
        self.passed_to_plotting_class = None

    def plot_empirical_semivariogram(self):
        #self.passed_to_plotting_class = some operation
        Plotting(self.passed_to_plotting_class).plot_passed_data()
        print("Empirical Semivariogram plotted. Check output folder > graphics for the graph.")
        pass
