month_list =["jan","feb","mar","apr","may"]
expense_list = [2334,2233,3333,2222,2122]
e=input("Enter your expense : ")
e = int(e)

month = -1

for i in range(len(expense_list)):
    if e == expense_list[i]:
        month =i
        break

if month != -1:
    print(f'You spend {e} in {month_list[month]}')
else:
    print(f'You didn\'t spend{e} in any month')