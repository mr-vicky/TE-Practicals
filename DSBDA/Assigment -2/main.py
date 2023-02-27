"""
Assingment-2
Data Wrangling II
Create an “Academic performance” dataset of students and perform the following operations using
Python.
1. Scan all variables for missing values and inconsistencies. If there are missing values and/or
inconsistencies, use any of the suitable techniques to deal with them.
2. Scan all numeric variables for outliers. If there are outliers, use any of the suitable
techniques to deal with them.
3. Apply data transformations on at least one of the variables. The purpose of this
transformation should be one of the following reasons: to change the scale for better
understanding of the variable, to convert a non-linear relation into a linear one, or to
decrease the skewness and convert the distribution into a normal distribution.
Reason and document your approach properly.

"""

import pandas as pd

left = pd.DataFrame({
    'id': [1, 2, 3, 4, 5 ],
    'name': ['Vivek', 'Sanket', 'Nitesh', 'Prathamesh', 'Yash'],
    'email_id': ['vivek@gmail.com', 'sanket@gmail.com', 'nitesh@gmail.com', 'prathamesh@gmail.com', 'yash@gmail.com'] ,
    'marks': ['99', '100', '99', '100', '99']
})

right = pd.DataFrame({
    'id': [6, 7, 8, 9, 10],
    'name': ['Tokiyo', 'Refel', 'Manila', 'Nitya', 'Alica'],
    'email_id': ['vivek@gmail.com', 'sanket@gmail.com', 'nitesh@gmail.com', 'prathamesh@gmail.com', 'yash@gmail.com'] ,
    'marks': ['98', '97', '98', '95', '99']
})

average_marks = left['marks'].astype(int).mean()

left = left.drop('roll no', axis=1)

left = loc[0, 'marks'] = None

new_row = {'id': 6, 'name': 'Tatya', 'email_id': 'tatya@gmal.com', 'marks': '100'};
left = left.append(new_row, ignore_index=True)

left.loc[left['name'] == 'Alex', 'marks'] = '88'

print(left)
print(right)

marged_df = pd.merge(left, right, on='id')
printed(marged_df)

print("The average of the 'marks' column in the 'left' DaraFrame is:", average_marks )