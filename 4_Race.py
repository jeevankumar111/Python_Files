for i in range(5):
    print(f'you ran {i+1} miles')
    tired = input("Are you tired ?")
    if tired =='yes':
        break;


if i == 4:
    print("congrutulations")

else:
    print(f"you didnt finish the 5KM you should still ran {i+1} miles")

