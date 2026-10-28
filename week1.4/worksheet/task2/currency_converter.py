"""
    Portfolio Task - Week 4

    By submitting this code you are declaring that all work in this file,
    other than any provided template code, was written and developed by
    you independently.

    Name: Caleb Cooke
"""

def currency_converter(amount, from_currency, to_currency):
    if amount < 0:
        return(float(0))
    else:
        conversion_rate = {
            'GBP': {'CNY': 9.24, 'PHP': 75.00, 'INR': 109.06},
            'CNY': {'GBP': 0.11, 'PHP': 8.12, 'INR': 11.81},
            'PHP': {'CNY': 0.12, 'GBP': 0.01, 'INR': 1.45},
            'INR': {'PHP': 0.69, 'CNY': 0.09, 'GBP': 0.01}
        }

        for key_1 in conversion_rate:
            if key_1 == user_from:
                stored_from = key_1
        stored_rates = conversion_rate.get(stored_from)
        for key_2 in stored_rates:
            if key_2 == user_to:
                stored_to = key_2
        stored_rate = float(stored_rates.get(stored_to))
        final_conversion = user_amount * stored_rate

        return final_conversion

user_from = input()
user_to = input()
user_amount = float(input())

print(currency_converter(user_amount, user_from, user_to))



# Submit only this file currency_converter.py with the completed function.

# Remove any additional code you may have added during development and testing.
