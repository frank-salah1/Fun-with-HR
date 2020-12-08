# HR
 
## Overview

HR has a large amount of data on staff in an organization.  This can be very useful for an organization, however most organizations do not leverage there data in a useful way.  HR has data such as salary, home addresses, education, years at the organization and much more.  The dataset I will be working will is called the HR Analytics Case Study, which can be found on [Kaggle](https://www.kaggle.com/vjchoudhary7/hr-analytics-case-study).

My goal is to look at the data to see how we can use a linear regression, a logistic regression, and k-means cluster to glean useful information that the company can leverage.

## Contents
- [Data](): contains original data and manipulated data used for k-means clustering, along with outputs from the predictions.
- [Notebooks](): contains the Jupyter notebooks used for data analysis and creating linear and logisitc regressions.
-Final Report.ipynb

## Goal

This project will use linear and logistic regressions to execute the following goals:

1) Can we use a linear regression to predict long someone someone has worked at the company?
2) Can we use a logistic regressions to predict the gender of an employee?
3) Can we use a k-means cluster to determine if there are any hidden groups in the employees?


## Dataset

This data set is from a Kaggle data set called ["HR Analytics Case Study"](https://www.kaggle.com/vjchoudhary7/hr-analytics-case-study).  I will be using general_data.csv. The dataset has the following columns:

- Age
- Attrition: Whether the employee left in the previous year or not
- BusinessTravel: How frequently the employees travelled for business purposes in the last year
- Department: Department in company
- DistanceFromHome: Distance from home in kms
- Education: Education Level
- EducationField: Field of education
- EmployeeCount
- EmployeeID
- Gender
- JobLevel: Job level at company on a scale of 1 to 5
- JobRole: Name of job role in company
- MaritalStatus
- MonthlyIncome: Monthly income in rupees per month
- NumCompaniesWorked: Total number of companies the employee has worked for
- Over18
- PercentSalaryHike: Percent salary hike for last year
- Standard Hours
- StockOptionLevel
- TotalWorkingYears: Total number of years the employee has worked so far
- TrainingTimesLastYear: Number of times training was conducted for this employee last year
- YearsAtCompany
- YearsSinceLastPromotion
- YearsWithCurrManager: Number of times training was conducted for this employee last year

## Requirements
- yellowbrick
- sklearn
- matplotlib
- numpy
- pandas

## Results

### Goal 1

The linear regression chosen had a test r-squared of approx. 68% and a train of approx. 66%.  This is a decent linear regression.  Since we can make some predictions with this linear regression, we can then determine what needs to be needs to happen in order for new and existing employees need to be retained, ex. additional training, a certain amount of years with a manager, etc.

### Goal 2

The logistic regressions chosen had an accuracy test score of approx. 60% and a training score of approx. 59%, which on the surface appears to be a good start and a logistic regression that could use some work and fine tuning.  However, when displaying the results of the logistic regression, we see it only predicted 0 (female) as the gender code and never predicting 1 (male), therefore the score is just happenstance.  In some ways this is good because it shows that there is no clear gender pay discrepancy, however further analysis could be done to see if other features could help predict gender.

### Goal 3

Based on looking at the dataset, the monthly income was the main factor that was used to deteremine the 4 groupings.  

The monthly income for each grouping was approx. as follows:

- 10090 to 42720 (Low)
- 42840 to 82680 (Medium-Low)
- 83210 to 143360 (Medium-High)
- 144110 to 199990 (High)

Beyond these groupings, there did not appear to be anything ese discernable from these groupings.


## Conclusion

Between the 3 machine learning methods used, the linear regression was the most succesful and useable.  The linear regression was able to determine years at a company based on several input features.  This linear regression can then be used to determine the factors needed to help get an employee to stay and continue employment.

The logistic regression, was not as succesful.  It was unable to predict gender based on monthly income and other input fetures.  Based on this, it shows there was no discenrable difference in pay between male and femal staff.

The k-means cluster created 4 different groupings.  These groupings were primarilly based on salary.

Overall there are definitely hidden gems within this dataset and other datasets like it.  With additional work, more predictions can be made.
