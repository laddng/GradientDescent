# Nick Ladd - CSC 391 Machine Learning
# Date: 09/25/16
# Dr. Cho
#
# Input: A csv file that contains a dataset on different
# wines that we would like to analyze for linear regressions.
#
# Output: A table that consists of the iteration, cost
# function of that iteration, and the RMSE of that iteration.
#
# Constraints: I have been assigned one variable to analyze,
# and I will do so with a univariate linear regression. Only
# basic libraries can be used.
#

# Import Python libraries
import csv;
import numpy;
import math;

# Main function
def main():

  # Variables
  filename = "winequality-red.csv";
  default_step_size = 1;
  dataset = [];
  variable_to_analyze = 1;

  # Function calls
  dataset = import_dataset(filename);
  calculate_cost_function(dataset);
  calculate_rmse(dataset);

# Import dataset from a wine CSV provided
def import_dataset(filename):

  # Array for our dataset
  dataset = [];

  # Open CSV file
  with open(filename, 'rb') as csvfile:

    # Skip header row
    next(csvfile);

    datareader = csv.reader(csvfile, delimiter=',');
    for row in datareader:

      # Typecast all row values as ints
      row = map(lambda x: float(x), row);

      # Add row to our dataset
      dataset.append(row);

  # Return imported dataset
  return dataset;

# Cost function calculation
def calculate_cost_function(dataset):

  # Slope variable
  slope = 0;

  # Iterate through each point
  for i in xrange(len(dataset)):

    # Calculate updated slope
    print "cost";

  return True;

# RMSE calculation
def calculate_rmse(dataset):

  # Total sum variable
  total_sum = 0;

  # Iterate through each point
  for i in xrange(len(dataset)):

    # Take the difference between predicted and actual squared
    difference = dataset[i][0] - (dataset[i][1]**2);

    # Add to our total sum
    total_sum += difference;

  # Average the value
  avg_difference = (total_sum / i);

  # Square root the average
  rmse = math.sqrt(avg_difference);

  # Return rmse
  return rmse;

# Execute main
main();
