from __future__ import print_function
import datetime
from datetime import date
import re

def convert24(str1):
     
    if str1[-2:] == "AM" and str1[:2] == "12":
        return "00" + str1[2:-2]
           
    elif str1[-2:] == "AM":
        return str1[:-2]
     
    elif str1[-2:] == "PM" and str1[:2] == "12":
        return str1[:-2]
         
    else:
         
        return str(int(str1[:2]) + 12) + str1[2:8]
 
def convert12(str): 

	h1 = ord(str[0]) - ord('0') 
	h2 = ord(str[1]) - ord('0') 

	hh = h1 * 10 + h2 

	Meridian="" 
	if (hh < 12): 
		Meridian = "AM" 
	else: 
		Meridian = "PM" 

	hh %= 12 

	if (hh == 0): 
		print("12", end = "") 

		for i in range(2, 8): 
			print(str[i], end = "") 

	else: 
		print(hh,end="") 
		
		for i in range(2, 8): 
			print(str[i], end = "") 

	print(" " + Meridian) 

userstring = raw_input("Enter your time string: ") 

if re.search(r'\d{2}:\d{2}:\d{2}', userstring):
    if re.search(r'AM|PM', userstring):
        match = re.search(r'(\d{2}:\d{2}:\d{2}AM)|(\d{2}:\d{2}:\d{2}PM)', userstring)
        time = (match.group())
        print(convert24(time))

    else:
        match = re.search(r'\d{2}:\d{2}:\d{2}', userstring)
        time = (match.group())
        if __name__ == '__main__': 
            convert12(time)
else:
    print("Your imput does not contain time")