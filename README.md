# unicode-decode
Python library to convert unicode to string & back

There are 4 functions in the library

Initialization to convert unicode string to text

from unicodeclass import UnicodeClass
uni = UnicodeClass("41424344" , types = "unicode")

Getting the string
print(uni.getTextString())

Output: ABCD

Getting a list containing the elements of the string
print(uni.getTextList())

Output: ['A' , 'B' , 'C' , 'D'] 


Initialization to convert text string to Unicode

from unicodeclass import UnicodeClass
uni = UnicodeClass("ABCD" , types = "text")

Getting the String
print(uni.getUnicodeString())

Output: 41424344


Getting the List
print(uni.getUnicodeList())

Output: ['41', '42', '43', '44']
