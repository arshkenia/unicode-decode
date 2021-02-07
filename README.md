# unicode-decode
<h1>Python library to convert unicode to string & back</h1>

There are 4 functions in the library

<h2>Initialization to convert unicode string to text</h2>

<pre><code>from unicodeclass import UnicodeClass
uni = UnicodeClass("41424344" , types = "unicode")
</code></pre>

<h3>Getting the string</h3>
<pre><code>print(uni.getTextString())
</code></pre>

Output: ABCD

<h3>Getting a list containing the elements of the string</h4>
<pre><code>print(uni.getTextList())
</code></pre>
Output: ['A' , 'B' , 'C' , 'D'] 


<h2>Initialization to convert text string to Unicode</h2>

<pre><code>from unicodeclass import UnicodeClass
uni = UnicodeClass("ABCD" , types = "text")
</code></pre>

<h3>Getting the String</h3>
<pre><code>print(uni.getUnicodeString())
</code></pre>

Output: 41424344


<h3>Getting the List</h3>
<pre><code>print(uni.getUnicodeList())
</code></pre>
Output: ['41', '42', '43', '44']
