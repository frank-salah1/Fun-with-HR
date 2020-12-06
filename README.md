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

1) Can we use a linear regression to make predictions of how long someone someone has worked at the company?
2) Can we use a logistic regressions to predict geneder of an employee?
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

## Conclusion

