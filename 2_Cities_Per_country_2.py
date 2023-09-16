india = ["HYD","Vizag","mumbai","delhi",'kolkatha']
usa   = ["NYC","WC","north carilone","taxes","arizona"]
PAK   = ["lahore","jaislambar","POK"]

city1 = input("Enter the first city1 : ")
city2 = input("Enter the second city2 : ")

if city1 in india and city2 in india :
    print(f'{city1} and {city2}  are present in the india')

elif city1 in usa and city2 in usa :
    print(f'{city1} and {city2} are presnt in the usa')

elif city1 in PAK and city2 in PAK :
    print(f'{city1} and {city2} are present int the PAK')

else :
    print('the entered cities are from the different countrys')
