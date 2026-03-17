num = 9
if num % 2 == 0:
    print("Number is Even")
else:
    print("Number is Odd")



a = 10
b = 25
c = 15

if a > b and a > c:
    print(f"{a} is the largest")
elif b > a and b > c:
    print(f"{b} is the largest")
else:
    print(f"{c} is the largest")


for i in range(1, 21):
    print(i)


num = 5
factorial = 1

for i in range(1, num + 1):
    factorial = factorial * i

print(f"Factorial is {factorial}")


num = 7
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")



text = "hello world"
vowels = "aeiou"
count = 0

for char in text:
    if char in vowels:
        count = count + 1

print("Number of vowels:", count)



text = "python"
reversed_text = ""

for char in text:
    reversed_text = char + reversed_text

print("Reversed string:", reversed_text)



num = 11
is_prime = True

if num > 1:
    for i in range(2, num):
        if num % i == 0:  # Kisi se divide ho gaya
            is_prime = False
            break

if is_prime and num > 1:
    print(f"{num} is Prime")
else:
    print(f"{num} is NOT Prime")



numbers = [10, 20, 30, 40]
total = 0

for n in numbers:
    total = total + n

print("Sum of numbers:", total)



numbers = [15, 82, 34, 99, 21]
largest = numbers[0]

for n in numbers:
    if n > largest:
        largest = n

print("Largest number:", largest)



numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = []

for n in numbers:
    if n not in unique_numbers:
        unique_numbers.append(n)

print("Unique List:", unique_numbers)



numbers = [1, 2, 3, 2, 4, 2, 5]
target = 2
count = 0

for n in numbers:
    if n == target:
        count = count + 1

print(f"{target} appeared {count} times.")



text = "madam"

if text == text[::-1]:
    print(f"{text} is a Palindrome")
else:
    print(f"{text} is not a Palindrome")




terms = 10
n1, n2 = 0, 1

for _ in range(terms):
    print(n1, end=" ")
    next_num = n1 + n2
    n1 = n2
    n2 = next_num




student = {
    "Name": "Rahul",
    "Age": 20,
    "Subject": "Python"
}

for key, value in student.items():
    print(f"{key}: {value}")




numbers = [42, 12, 89, 33, 7]

n = len(numbers)
for i in range(n):
    for j in range(0, n - i - 1):
        if numbers[j] > numbers[j + 1]:
            # swap (jagah badli)
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print("Sorted list:", numbers)




list1 = [1, 2, 3]
list2 = [4, 5, 6]

merged_list = list1 + list2
print("Merged List:", merged_list)




sentence = "Learning Python is very fun"

words_list = sentence.split()
total_words = len(words_list)

print("Total words:", total_words)




import random

random_number = random.randint(1, 100)
print("Random Number:", random_number)
