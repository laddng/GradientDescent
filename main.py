# Nick Ladd - CSC 391 Machine Learning
# Date: 10/02/16
# Dr. Cho
#
# Input: A csv file that contains a dataset on different
# wines that we would like to analyze for linear regressions.
#
# Output: A table that consists of the iteration, cost
# function of that iteration, and the RMSE of that iteration.
# In addition, we will include two graphs, one of the cost function
# and one of the RMSE at each iteration.
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
  dataset_length = 0;
  variable_to_analyze = 1;
  wine_quality_column = 11;

  # Function calls
  dataset = import_dataset(filename);
  dataset_length = len(dataset);
  calculate_cost_function(dataset, dataset_length, variable_to_analyze, wine_quality_column);

# Dataset import - imports the dataset from a wine CSV provided
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

# Cost function calculation - computes the cost function and returns the values to screen.
def calculate_cost_function(dataset, dataset_length, variable_to_analyze, wine_quality_column):

  # Slope variable
  slope = 0;

  # Iterate through each point
  for i in xrange(dataset_length):

    # Our current iteration variable
    value = dataset[i][variable_to_analyze];

    # Calculate the cost function
    cost = value;

    # Calculate the RMSE
    rmse = calculate_rmse(dataset, i);

    # Print the iteration's values ( properly tabbed )
    print("| Iteration: " + str(i + 1) + " \t| Cost: " + str(cost) + " \t| RMSE: " + str(rmse) + " \t|").expandtabs(4);

  return True;

# RMSE calculation - calculates the RMSE of a given dataset and iteration.
def calculate_rmse(dataset, iteration):

  if iteration > 0:

    # Total sum variable
    total_sum = 0;

    # Iterate through each point
    for i in xrange(iteration):

      # Take the difference between predicted and actual squared
      difference = dataset[i][0] - (dataset[i][1]**2);

      # Add to our total sum
      total_sum += difference;

    # Average the value
    avg_difference = (total_sum / iteration);

    # Square root the average
    rmse = math.sqrt(avg_difference);

    # Return rmse
    return rmse;

  else:
    return 0;

# Execute main
main();

