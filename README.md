
# Green Destinations Attrition Analysis

## Overview

This project provides a Python script (`green_destinations.py`) designed to analyze employee attrition at "Green Destinations," a travel agency. The script uses data to calculate the overall attrition rate and investigate the impact of key factors such as age, years at the company, and monthly income on employee retention. Visualizations (box plots) are generated to illustrate these relationships, helping to identify potential trends or patterns contributing to employees leaving.

## Problem Statement

Green Destinations has observed an increase in employee attrition. The HR Director is seeking to understand the underlying causes by identifying any significant trends or patterns in the data. Specifically, the objectives are:
1.  To determine the overall attrition rate (percentage of employees who have left).
2.  To analyze if factors like age, years at the company, and monthly income play a role in employee attrition.

## Solution

The `green_destinations.py` script offers a solution to the problem statement by performing the following:

1.  **Data Loading and Initial Inspection**: The script loads employee data from a CSV file (expected to be named `greendestination (1).csv`). It then prints the head of the DataFrame and provides an information summary to ensure data integrity and proper loading.
2.  **Attrition Rate Calculation**: It calculates the attrition rate, defined as the percentage of employees who have left the company. This rate is then printed to the console.
    $$\text{Attrition Rate} = \frac{\text{Number of Employees Who Left}}{\text{Total Number of Employees}} \times 100$$
3.  **Factor-Based Analysis and Visualization**: The script analyzes the relationship between attrition and the following factors: 'Age', 'YearsAtCompany', and 'MonthlyIncome'. For each factor, it generates a box plot comparing the distribution of the factor for employees who attrited versus those who did not. These plots are saved as individual image files (e.g., `Age_vs_Attrition.png`), providing visual insights into which factors might be influencing attrition.
