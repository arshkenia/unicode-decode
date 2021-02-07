# unicode-decode
<h1>Python library to convert unicode to string & back</h1>

There are 4 functions in the library

<h2>Initialization to convert unicode string to text</h2>

from unicodeclass import UnicodeClass
uni = UnicodeClass("41424344" , types = "unicode")

<h3>Getting the string</h3>
print(uni.getTextString())

Output: ABCD

<h3>Getting a list containing the elements of the string</h4>
print(uni.getTextList())

Output: ['A' , 'B' , 'C' , 'D'] 


<h2>Initialization to convert text string to Unicode</h2>

'''from unicodeclass import UnicodeClass
uni = UnicodeClass("ABCD" , types = "text")'''

<h3>Getting the String</h3>
print(uni.getUnicodeString())

Output: 41424344


<h3>Getting the List</h3>
print(uni.getUnicodeList())

Output: ['41', '42', '43', '44']
