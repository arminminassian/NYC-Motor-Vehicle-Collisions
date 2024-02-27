**Overview**

This project aims to identify statistically significant variables impacting fatalities in motor vehicle accidents in New York City (NYC). The analysis involves data cleaning and the conversion of qualitative variables into dummy variables using Excel. Subsequently, a multiple logistic regression model is implemented in Python to predict the likelihood of fatalities based on various factors such as Alcohol Involvement, Weather, Accident time, Accident Borough, Driver Distraction, Vehicle Type, etc. 

**Data Cleaning and Preprocessing**

The dataset containing information on motor vehicle collisions in NYC is cleaned and preprocessed using Excel. This involves handling missing data, removing duplicates, and converting qualitative variables into dummy variables for use in the regression model. The cleaned dataset is then imported into Python for further analysis.

**Implementation of Logistic Regression Model**

The logistic regression model is implemented in Python using the statsmodels library. Two models are constructed: one with a single independent variable and another with multiple independent variables. The models are fitted to the data, and the statistical significance of the variables is assessed to identify factors contributing significantly to fatalities in motor vehicle accidents.

**Results and Insights**

The regression models provide insights into the factors that significantly influence the likelihood of fatalities in NYC motor vehicle accidents. The coefficients and p-values of the variables highlight their importance and statistical significance in predicting fatalities. These insights can inform policymakers, urban planners, and law enforcement agencies in implementing targeted interventions and measures to reduce fatalities and enhance road safety in NYC.

**Conclusion**

By leveraging data cleaning techniques, logistic regression modeling, and statistical analysis, this project offers valuable insights into the determinants of fatalities in motor vehicle accidents in NYC. The findings contribute to the understanding of road safety dynamics and can guide efforts to mitigate risks and improve safety outcomes on NYC roads.
