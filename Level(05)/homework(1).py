#  1) თუ დენის წყაროს ძაბვა 12V-ია და რეზისტორის წინაღობა 4Ω, იპოვე წრეში გამავალი დენი. (გამოიყენე ომის კანონი: 𝐼 = 𝑉/𝑅)
homework=input("Task ")

volt=int(input("Enter the volt value: "))
resistance=int(input("Enter the resistance: "))
I=volt/resistance
print(f"I = {float(I)}")