street = "4-14 BC colony"
city   = "Mandapeta"
country= "INDIA"

address = '\n'+street+'\n'+city+'\n'+country
print('First using the  + Operator : ',address)

address =f'\n{street}\n{city}\n{country}'
print('Second using the f string operator : ',address)