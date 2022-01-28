# To print the number of special characters in a string
# string = "Chandana@345#$%^^&12********3"
# count = 0
# for i in string:
#     if not('A' <= i <= 'Z' or 'a' <= i <= 'z' or ('0' <= i <= '9')):
#         count += 1
# print(count)

# To traverse through list :
# without using range function
# l = ["python", 2, 3.2, "Selenium", "Java"]
# for item in l:
#     print(item, end= ', ')

# Traversing through a list in reverse order :
# using reverse function
# l = ["python", 2, 3.2, "Selenium", "Java"]
# l.reverse()
# print(l)

# using slicing
# l = ["python", 2, 3.2, "Selenium", "Java"]
# l = l[::-1]
# print(l)

# Using range function
# l = ["python", 2, 3.2, "Selenium", "Java"]
# for i in range(len(l)-1, -1, -1):
#     print(l[i], end= ' ')

# To print odd index in the list using slicing
# l = ["python", 2, 3.2, "Selenium", "Java"]
# for i in l[::2]:
#     print(i, end=', ')
#
# # To print even index in the list using Slicing
# l = ["python", 2, 3.2, "Selenium", "Java"]
# for i in l[1::2]:
#     print(i, end=', ')

# l = ["python", "Chandana", 5+3j, 45.68, "Kalyani", "Selenium", "Java"]
# for i in l:
#     if i in l:
#         if isinstance(i, str):
#             print(i[::-1], end=' ,')
#         else:
#             print(i, end=', ')

# files = ["google.com", "infosys.co", "apple.xls", "tyss.pdf"]
# for file in files:
#     print()
#
# li = ["Python", "dad", "hai", "malayalam", "madam", "mam"]
# set_ = set()
# for element in li:
#     if element == element[::-1]:
#         set_.update([element])
# print(set_)

s1="hai"
s2="hello"
# print(zip(s1,s2))
print(id(s




