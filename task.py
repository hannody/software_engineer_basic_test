"""
Developed by Mohanad Abu-Nayla, Nov-2021.
www.abunayla.com
This work comes without any warranty of any type, use it at your own risk.
If you find any thing useful, please send me a message/credit me, but you are 
not required to do so.
"""

import csv


class Task:
    @staticmethod
    def uppercase(text):
        if text == "":
            return ""
        return text.upper()

    @staticmethod
    def altcase(text):
        if text == "":
            return ""

        alternate_text = ""
        for i, val in enumerate(text):
            if(i % 2 == 0):
                alternate_text += val.lower()
            else:
                alternate_text += val.upper()
        return alternate_text

    @staticmethod
    def csvexport(filename, data):
        with open(filename, 'w') as csvfile:
            try:
                txtwriter = csv.writer(csvfile, delimiter=',')
                txtwriter.writerow(data.lower())
                return "CSV created!"
            except Exception as e:
                return e
