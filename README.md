# unicode-decode
<h1>Python library to convert unicode to string & back</h1>

There are 4 functions in the library

<h2>Initialization to convert unicode string to text</h2>

from unicodeclass import UnicodeClass
uni = UnicodeClass("41424344" , types = "unicode")

<h3>Getting the string</h3>
print(uni.getTextString())

Output: ABCD

<h4>Getting a list containing the elements of the string</h4>
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
