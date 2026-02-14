amount=int(input("enter the amount for withdraw "))

note1= amount//100
note2= (amount%100)//50
note3= ((amount%100)%50)//10

print(f"notes of rs 100 are {note1}")
print(f"notes of rs 50 are {note2}")
print(f"note of rs 10 are {note3}")