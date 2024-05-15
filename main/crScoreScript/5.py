import requests

# URL of your API endpoint
url = 'http://127.0.0.1:5000/predict_credit_score'

# Data for a new applicant
new_applicant_data = {
    'RevolvingUtilizationOfUnsecuredLines': [0.2],
    'age': [27],
    'NumberOfTime30-59DaysPastDueNotWorse': [11],
    'DebtRatio': [0.2],
    'MonthlyIncome': [9340],
    'NumberOfOpenCreditLinesAndLoans': [7],
    'NumberOfTimes90DaysLate': [17],
    'NumberRealEstateLoansOrLines': [9],
    'NumberOfTime60-89DaysPastDueNotWorse': [8],
    'NumberOfDependents': [10]
}

# Send POST request to the API endpoint
response = requests.post(url, json=new_applicant_data)

# Print the predicted credit score
print("Credit Score for New Applicant:", response.json()['credit_score'])
