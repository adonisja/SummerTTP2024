def main():
    stock_prices = {'GOGL' : 849, 'FB' : 136, 'MSFT' : 64, 'AAPL' : 137,
                'AMZN' : 848, 'TWTR' : 16, 'CSCO' : 43.49, 'PG' : 141.96,
                'AXP' : 154.42, 'HD' : 289.24}
    budget = int(input('Enter your budget: $'))
    if budget <= 50:
        print('You are quite broke, Get Your Money Up!')
    elif budget > 250:
        print("Which prince decided on a new hobby?")
    else:
        print("Meh, I guess you're already here")
    print('Stocks you can afford are: ')
    for i in stock_prices:
        if stock_prices[i] <= budget:
            print(i)

if __name__ == "__main__":
    main()
