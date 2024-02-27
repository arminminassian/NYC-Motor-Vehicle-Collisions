### Import packages in the virtual environment
import pandas as pd   ## search the package "pandans"
import statsmodels.api as sm    ## search the package "statsmodels"
import statsmodels.stats.api as sms   ## no need to install package
from statsmodels.compat import lzip   ## no need to install package
import matplotlib.pyplot as plt    ## search the package "matplotlib"
import seaborn as sns     ## search the package "seaborn"
import scipy.stats as scipy    ## search the package "scipy"
from scipy.stats import shapiro   ## no need to install package
import sys   ## no need to install package
import os   ## no need to install package

os.chdir(r"C:\Users\armin\Desktop\Visualisation")
##Change the address to your working folder

pd.set_option('display.max_columns', 500)
## Display all columns when printing results

mydata = pd.read_csv("Motor_Vehicle_Collisions_Crashes_Armin.csv")
## Remember to include “r” first inside the bracket.

file = open('output.txt','wt')
sys.stdout = file
## Open a text file and save all results into the text file

print(mydata.describe())
## Display summary statistics of the data

df = pd.DataFrame(mydata)
##Transform the dataset into two-dimensional, size-mutable, potentially heterogeneous tabular data

######################## Linear regression with only one independent variable
x = df['CONTRIBUTING_FACTOR_ALCOHOL_INVOLVEMENT']
##Define the independent variables in the model
y = df['KILLED_NOTKILLED']
##Define t he dependent variable in the model

# with statsmodels
x = sm.add_constant(x)  # adding a constant
##Add a constant in the regression model

model1 = sm.Logit(y, x).fit()
##Fit the model
results_model1 = model1.summary()
print(results_model1)
##Output the results



######################## Linear regression with only multiple independent variables

x = df[['Summer', 'Winter', 'Rush_Hrs12to18', 'Night_Hrs21to3', 'BOROUGH_BRONX', 'BOROUGH_QUEENS', 'BOROUGH_MANHATTAN', 'CONTRIBUTING_FACTOR_DRIVER_INATTENTION/DISTRACTION', 'CONTRIBUTING_FACTOR_ALCOHOL_INVOLVEMENT', 'CONTRIBUTING_FACTOR_FOLLOWING_TOO_CLOSELY', 'VEHICLE_TYPE_CODE_STATION_WAGON/SPORT_UTILITY_VEHICLE', 'VEHICLE_TYPE_CODE_SEDAN', 'VEHICLE_TYPE_CODE_PICK-UP_TRUCK']]
##Define the independent variables in the model
y = df['KILLED_NOTKILLED']
##Define t he dependent variable in the model

# with statsmodels
x = sm.add_constant(x)  # adding a constant
##Add a constant in the regression model

model2 = sm.Logit(y, x).fit()
##Fit the model
results_model2 = model2.summary()
print(results_model2)
##Output the results


file.close()
##Close the text file.


