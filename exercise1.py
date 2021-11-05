N = int(input("Enter a number:"))
even_numbers = 0
odd_numbers = 0
even_number_count = 0
for numbers in range(1, N+1):
    if numbers % 2 == 0:
        even_numbers += numbers
        even_number_count += 1
    else:
        odd_numbers += numbers
print("Avg of even nmb: ", even_numbers/even_number_count, "Sum of odd nmb:", odd_numbers)

