# Surfs Up Analysis

## Overview
####
A business proposal to create an ice cream and surf shop combination has been pitched to an enthusiastic backer. However, the potential backer has requested a data analysis of the weather on Oahu, Hawaii to determine if this combination shop is truly feasible. An overarching analysis has been presented already, but the backer has now requested a specific look at temperatures in the peek of winter and summer. The months of June and December have been selected to show the historical averages of a peek and slow season through the years. Using Python code, Jupyter Notebook, and SQLite, queries are created and then saved to dataframes in order to analyze the weather data using summary statistics for the sustainability of the potential business venture. 

## Results
####
Below are the results from the two queries: 

* The average temperature in June is roughly 75 degrees, four degrees higher than the average temperature in December. 
* December has about 200 less data points than the month of June, meaning the two months do not have the same amount of data to pull from.
* The minimum temperature in December is 56 degrees, which is eight degrees lower than the minimum temperatures in June. 
* Both months share a rough standard deviation of roughly 3, meaning the data falls within a normal, reliable distribution.  

## Summary
####
The statistical analysis performed on the months of June and December are an important evaluation of whether the ice cream and surf shop would be feasible. Knowing the temperature during the hottest month and coldest month can give any potential investors on whether or not people would be interested in surfing or eating ice cream on the beach year round. Hawaii is known for its tropical climate, however, most tourist locations have a peek season and slow season. Looking purely at the temperature, there isn't a significant difference in the average monthly temperature, meaning that there is potential for success. However, just looking at temperature ignores other important factors such as weather conditions that may be best for surfing. Knowing more about the rainfall in December and June could prove that even if the temperature is warm enough, it may not be perfect ice cream or surfing weather. A query performed for the months of June and December with the precipitation selected instead of the temperature in the Measurement table would easily show whether or not excessive raining will be a problem. 

####
