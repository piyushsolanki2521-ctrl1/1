import datetime
import pandas as pd
data = []

def adding():
    date = input("Enter Date (DD-MM-YYYY): ")
    try:
        date = datetime.date.strptime(date, "%d-%m-%Y")
        if date.year != today_date.year:
            print("Warning entered Date does not have the same year as today to start again press 0")
        elif date.month != today_date.month:
            print("Warning entered Date does not have the same month as today to start again press 0")
        elif date.day != today_date.day:
            print("Warning entered Date does not have the same day as today to start again press 0")
    except ValueError:
        print("Date Format Error")
        entry()
    category = input("Enter category(Food, Travel, Shopping, etc: )")
    if category == "0":
        return
    description = input("Enter short description: ")
    amount = int(input("Enter amount: "))
    dicti = {"date": date, "category": category, "description": description, "amount": amount}
    data.append(dicti)
    print("Date Added Successfully")

def viewing():
    if len(data) == 0:
        print("No Data Found")

    else:
        for i in data:
            print(i, end="\n")

def spending():
    what_to_see = input("Enter which category you want to see (all/category): ")
    if what_to_see.lower() == "all":
        total_amount = 0
        for item in data:
            total_amount += item.get("amount")
        print("Total Spending: ", total_amount)
    elif what_to_see.lower() == "category":
        all_spending = {}
        all_categories = []
        for item in data:
            cat = item.get('category')
            if cat not in all_categories:
                all_categories.append(cat)
        for cat in all_categories:
            total_cat_amount = 0
            for item in data:
                if item.get("category") == cat:
                    total_cat_amount += item.get('amount')
            all_spending[cat] = total_cat_amount
        print(all_spending)
    else:
        print("Invalid Choice")
        spending()

def filtering():
    filtered_data = []
    by_how = input("Filter by Month/Year/Date?: ")
    if by_how.lower() == "month":
        try:
            which = input("specify which month in numerical value")
            for item in data:
                if str(item.get("date").month) == which:
                    filtered_data.append(item)
            print(filtered_data)
        except ValueError:
            print("Invalid response")
            return
    elif by_how.lower() == "year":
        try:
            which = input("specify which year in numerical value")
            if len(which) == 2:
                which = "20" + which
            for item in data:
                if str(item.get("date").year) == which:
                    filtered_data.append(item)
            print(filtered_data)
        except ValueError:
            print("Invalid response")
            return
    elif by_how.lower() == "date":
        try:
            which = input("specify which date of this month in numerical value")
            for item in data:
                if str(item.get("date").day) == which and str(item.get("date").month) == today_date.month:
                    filtered_data.append(item)
            print(filtered_data)
        except ValueError:
            print("Invalid response")
            return
    else:
        print("Invalid response")
        return

def entry():

    answer = int(input('''
    1. Add Expense
    2. View All Expense
    3. Show total spending
    4. filter data
    5. Exit
    Enter your choice (1-5): 
    '''))

    if answer == 1:
        adding()
    elif answer == 2:
        viewing()
    elif answer == 3:
        spending()
    elif answer == 4:
        filtering()
    elif answer == 5:
        exit()
    else:
        print("Invalid Choice")
        entry()


while True:
    today_date = datetime.date.today()
    entry()