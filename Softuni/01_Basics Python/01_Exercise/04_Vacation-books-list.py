from math import floor

number_of_pages = int(input())
pages_per_hour = int(input())
days_per_book = int(input())

print (floor(floor(number_of_pages / pages_per_hour) / days_per_book))

