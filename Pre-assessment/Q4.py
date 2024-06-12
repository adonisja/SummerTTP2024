def main():
    monthly_spending = [2689.56, 2770.38, 2394.04, 2099.91, 3182.20, 
                        3267.12, 1746.83, 2545.72, 3328.20, 3147.30, 
                        2462.61, 3890.45, 3000.00, 2000.00]

    '''Low: Less than 2000
    ● Medium: Between 2000 and 3000 inclusive
    ● High: Greater than 3000'''
    low = []
    medium = []
    high = []
    for i in monthly_spending:
        if i < 2000:
            low.append(i)
        elif i >= 2000 and i <= 3000:
            medium.append(i)
        else:
            high.append(i)
    print(f"Martha\’s spending was low for {len(low)} months, medium for {len(medium)} months and high for {len(high)} months.")

if __name__ == "__main__":
    main()