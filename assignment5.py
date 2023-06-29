numbers = []
for i in range(5):
    num = int(input("Enter number {}: ".format(i+1)))
    numbers.append(num)

sum_of_numbers = sum(numbers)
print("Sum of all the numbers:", sum_of_numbers)

smallest_number = min(numbers)
print("Smallest number:", smallest_number)

largest_number = max(numbers)
print("Largest number:", largest_number)

ascending_order = sorted(numbers)
print("List in ascending order:", ascending_order)

descending_order = sorted(numbers, reverse=True)
print("List in descending order:", descending_order)

numbers_tuple = tuple(numbers)
print("List converted into a tuple:", numbers_tuple)

del numbers
print("List deleted.")


