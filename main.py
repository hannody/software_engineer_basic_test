"""
Developed by Mohanad Abu-Nayla, Nov-2021.
www.abunayla.com
This work comes without any warranty of any type, use it at your own risk.
If you find any thing useful, please send me a message/credit me, but you are 
not required to do so.
"""

from task import Task

raw_text = input("Enter a text: ")
# converts the string to uppercase and outputs it to stdout
print(Task().uppercase(raw_text))

# converts the string to alternate upper and lower case and outputs it to stdout
print(Task().altcase(raw_text))

# creates a CSV file from the string by making each character a column in the -
# CSV and then output "CSV created!" to stdout.
print(Task().csvexport("output.csv", raw_text))
