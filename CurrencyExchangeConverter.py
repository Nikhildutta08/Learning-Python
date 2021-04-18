import requests
import json

def currency_exchange_calc():

    date = input("\n\nPlease enter the date in 'YYYY-MM-DD' format or type 'latest': ")
    base_url = "https://api.ratesapi.io/api/" + date

    fromcurr = input("From Currency: ")
    tocurr = input("To Currency: ")
    while True:
        try:
            amount = float(input("Enter the amount to convert: "))
            break
        except:
            continue

    param = {'symbols':tocurr.upper(), 'base':fromcurr.upper()}

    response = requests.get(base_url, params=param)

    if response.ok == True:
        data = response.json()
        print(f"Exchange rate of {amount} {fromcurr.upper()} to {tocurr.upper()} on {data['date']} is: ", end='')
        print("{0:.2f}".format(amount*data['rates'][tocurr.upper()]))
    else:
        print(f"Error code:{response.status_code}", end='-')
        print(response.json()['error'])

def currency_codes():

    base_url = "https://api.ratesapi.io/api/latest"

    response = requests.get(base_url)

    print("Supported Currency Codes: ")
    
    mycurrcodes = response.json()['rates']
    for key,value in mycurrcodes.items():
        print(key, end=',')

if __name__ == '__main__':
    print("############################################################################################")
    print("###########################Welcome to currency exchange calculator##########################")
    print("############################################################################################")
    currency_codes()
    while True:
        currency_exchange_calc()
        ans = ''
        while ans not in ('Y','y','N','n'):
            ans = input("\nDo you want to continue?(Y/N): ")
        if ans.upper() == 'Y':
            continue
        else:
            break
