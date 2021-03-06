# Nick Ladd - CSC 391 Machine Learning
# Date: 10/02/16
# Dr. Cho
#
# Input: A csv file that contains a dataset on different
# wines that we would like to create a linear regression with
# using the Gradient Descent Algorithm.
#
# Output: A table that consists of the iteration, cost
# function of that iteration, and the RMSE of that iteration of our
# gradient descent algorithm.
#
# In addition, we will include two graphs, one of the cost function
# and one of the RMSE at each iteration of the gradient descent.
#
# Constraints: Only basic Python and Math libraries can be used.
#

# Import Python libraries
import csv;
import numpy;
import math;
from matplotlib import pyplot as plt;

# ** Main Function **
def main():

  # variables
  filename = "winequality-red.csv"; # our csv file
  alpha = 0.0005; # step size for gradient descent (higher step size = more accurate results, slower)
  threshold = 0.05; # the maximum acceptable derivative for convergence criteria
  dataset = []; # our dataset
  my_variable = 1; # location of our data point in csv
  quality_variable = 11; # location of the wine quality data point in csv

  # import dataset and execute gradient descent on it, then show graphs
  dataset = import_dataset(filename);
  m, b, rmse_list, iterations = gradient_descent(dataset, alpha, threshold, my_variable, quality_variable);
  generate_graphs(m, b, rmse_list, dataset, quality_variable, iterations);

# ** Dataset Import **
# imports the entire dataset from a CSV provided
def import_dataset(filename):

  # array for our new dataset
  dataset = [];

  # open CSV file
  with open(filename, 'rt') as csvfile:

    # skip header row
    next(csvfile);

    # create reader object and set the delimiter
    datareader = csv.reader(csvfile, delimiter=',');
    for row in datareader:

      # typecast all row values as floats
      row = list(map(lambda x: float(x), row));

      # append current row to our dataset
      dataset.append(row);

  # return imported dataset
  return dataset;

# ** Gradient Descent **
# runs our gradient descent algorithm by iterating through the
# gradient descent calculations until we have reached below a minimum threshold value.
def gradient_descent(dataset, alpha, threshold, my_variable, quality_variable):

  # starting point for our gradient descent
  m = 0.0; # slope start (can be any random slope)
  b = 0.0; # y-intercept start (can be any random y-intercept)

  iterations = 0; # count of iterations for our gradient descent
  derivative = threshold + 1; # initial value for the derivative

  rmse_list = [] # an array where we will store our RMSE error results at each iteration

  # until we have reached an acceptable threshold for the minimum cost
  while ( threshold < derivative ):
    # calculate gradient of line - passing our current variables in for the next calculation for
    # more fine tuning of our regression line
    m, b, b_gradient  = gradient_calculation(dataset, m, b, alpha, my_variable, quality_variable);

    # total error of our new line
    total_error = 0.0;

    # compute the total error of the new line
    for i in range(len(dataset)):
      x = dataset[i][quality_variable];
      y = dataset[i][my_variable];
      total_error += cost_function(x, y, m, b);

    # take the average of the resulting total_error
    theta = total_error / float( len( dataset ) );

    # compute the absolute value of the gradient
    derivative = abs( b_gradient );

    # iterate by one
    iterations = iterations + 1;

    # compute the RMSE of the new line
    rmse = calculate_rmse(dataset, m, b, quality_variable, my_variable);

    # store iteration's RMSE
    rmse_list.append(rmse);

    # print the iteration's values ( properly tabbed )
    print("| Iteration: " + str(iterations) + " \t| Cost function: " + format(theta, '.2f').expandtabs(5) + " \t| RMSE: " + str(rmse).expandtabs(5) + " \t|");

  # return our computed regression line variables (m: slope, b: y-intercept) and our RMSE list
  return m, b, rmse_list, iterations;

# ** Gradient Calculation **
# calculates the new gradient given the previous gradient variables by iterating over
# the dataset, and returns the gradient descent of the result for our new linear regression line.
def gradient_calculation(dataset, m, b, alpha, my_variable, quality_variable):
  # variables to store our new gradient calculations
  m_gradient = 0.0;
  b_gradient = 0.0;
  dataset_size = float(len(dataset));

  # iterate through whole dataset and calculate the gradient of each point
  for i in range(len(dataset)):

    # set our current x and y for our calculation
    x = dataset[i][quality_variable]; # actual value
    y = dataset[i][my_variable]; # value to predict with

    # compute our gradient for our slope and y-intercept at this iteration
    # using the derivative of the cost function and the points of this iteration. 
    # Then add the result to our gradient variables.
    cost = cost_function_derivative( x, y, m, b ); # compute theta with actual and predicted
    m_gradient += -( 2.0 / dataset_size ) * x * cost; # compute gradient of m
    b_gradient += -( 2.0 / dataset_size ) * cost; # computer gradient of b

  # with our new gradients calculated, we step in the opposite direction by our alpha amount
  m = m - ( alpha * m_gradient );
  b = b - ( alpha * b_gradient );

  # return our new regression line values (y-intercept and slope), the derivative, and the
  # result of the cost function
  return m, b, b_gradient;

# ** Cost Function Calculation **
# computes the cost and returns it
def cost_function(x, y, m, b):
  cost = ( y - ( ( m * x ) + b ) ) ** 2;
  return cost;

# ** Cost Function Derivative **
# computes the gradient with the derivative of the
# cost function
def cost_function_derivative(x, y, m, b):
  cost = y - ( ( m * x ) + b );
  return cost;

# ** RMSE Calculation **
# calculates the RMSE of a given dataset and iteration
def calculate_rmse(dataset, m, b, quality_variable, my_variable):

  # Total sum variable
  total_sum = 0.0;

  # Iterate through each point
  for i in range( len( dataset ) ):

    # calculate predicted wine quality values for a given y values
    y = dataset[i][my_variable];
    predicted_x = ( ( y - b) / m ); # predicted wine quality value
    actual_x = dataset[i][quality_variable]; # actual wine quality value

    # Take the difference between predicted and actual squared
    difference = ( actual_x - predicted_x ) **2;

    # Add to our total sum
    total_sum += difference;

  # Average the value
  avg_difference = ( total_sum / float( len( dataset ) ) );

  # Square root the average
  rmse = math.sqrt( avg_difference );

  # Return rmse
  return rmse;

# ** Generate Graphs **
# generates two graphs - the cost function line and a curve
# of all the RMSE values during the gradient descent
def generate_graphs(m, b, rmse_list, dataset, quality_variable, iterations):

  # get wine quality score range
  quality_range = range(10);

  # array to store our thetas for the wine score range
  theta = [];

  # new graph figure
  plt.figure(1);

  # plot points for cost function
  for x in quality_range:
    y = m * x + b;
    theta.append(y);
  plt.subplot(211);
  plt.plot(quality_range, theta, '-');
  plt.xlabel('Wine Quality');
  plt.ylabel('Volatile Acidity');

  # graph rmse value at each iteration
  iteration_range = range(iterations);
  plt.subplot(212);
  plt.plot(iteration_range, rmse_list, '-');
  plt.xlabel('Iterations');
  plt.ylabel('RMSE');
  plt.show();

# execute main
main();

