
"""
Last login: Sun May 31 09:51:52 on console

The default interactive shell is now zsh.
To update your account to use zsh, please run `chsh -s /bin/zsh`.
For more details, please visit https://support.apple.com/kb/HT208050.
(base) markeias-mbp:~ markeia$ cd "one Drive"
-bash: cd: one Drive: No such file or directory
(base) markeias-mbp:~ markeia$ cd "One Drive" 
-bash: cd: One Drive: No such file or directory
(base) markeias-mbp:~ markeia$ cd onedrive
(base) markeias-mbp:onedrive markeia$ ls
Carrie Mae Brox.docx
Data Analytics Bootcamp
Documents
Getting started with OneDrive.pdf
Icon?
Pictures
(base) markeias-mbp:onedrive markeia$ cd "Data Analytics Bootcamp"
(base) markeias-mbp:Data Analytics Bootcamp markeia$ ls
Excel Module			Python Module
Module Write Ups.docx		Visual Basic Applications
(base) markeias-mbp:Data Analytics Bootcamp markeia$ cd "Python Module"
(base) markeias-mbp:Python Module markeia$ ls
Activities		Election_Analysis
Activities.zip
(base) markeias-mbp:Python Module markeia$ cd "Election_Analysis"
(base) markeias-mbp:Election_Analysis markeia$ ls
README.md		python_practice.py
(base) markeias-mbp:Election_Analysis markeia$ python 3 python_practice.py
python: can't open file '3': [Errno 2] No such file or directory
(base) markeias-mbp:Election_Analysis markeia$ python3
Python 3.7.6 (default, Jan  8 2020, 13:42:34) 
[Clang 4.0.1 (tags/RELEASE_401/final)] :: Anaconda, Inc. on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> python_practive.py
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'python_practive' is not defined
>>> exit()
(base) markeias-mbp:Election_Analysis markeia$ python3 python_practice.py
Hello World
(base) markeias-mbp:Election_Analysis markeia$ python3
Python 3.7.6 (default, Jan  8 2020, 13:42:34) 
[Clang 4.0.1 (tags/RELEASE_401/final)] :: Anaconda, Inc. on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> type(ballots)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'ballots' is not defined
>>> type(1,341)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: type() takes 1 or 3 arguments
>>> type(1, 341)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: type() takes 1 or 3 arguments
>>> type(73.81)
<class 'float'>
>>> type("")
<class 'str'>
>>> type("true")
<class 'str'>
>>> type(true)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'true' is not defined
>>> type('true')
<class 'str'>
>>> type(True)
<class 'bool'>
>>> help(keywords)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'keywords' is not defined
>>> help("keywords")

Here is a list of the Python keywords.  Enter any keyword to get more help.

False               class               from                or
None                continue            global              pass
True                def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield
break               for                 not                 

>>> 5+3*3
14
>>> 8//5-3
-2
>>> 8+22*2-4
48
>>> 16-3/2+7-1
20.5
>>> 3**3%5
2
>>> 5+9*3/2-4
14.5
>>> 5%5
0
>>> 4%3
1
>>> 55/32
1.71875
>>> 55//32
1
>>> 552/32
17.25
>>> 552//32
17
>>> 5+(9*3/2-4)
14.5
>>> 5+(9*3/(2-4))
-8.5
>>> countries = ["Nigeria","USA","Mali","Ghana"]
>>> countries
['Nigeria', 'USA', 'Mali', 'Ghana']
>>> countries(0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'list' object is not callable
>>> countries[0]
'Nigeria'
>>> print(countries[2])
Mali
>>> countries[-1]
'Ghana'
>>> countries[-2]
'Mali'
>>> counties.append("London")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'counties' is not defined
>>> countries.append("London")
>>> countries
['Nigeria', 'USA', 'Mali', 'Ghana', 'London']
>>> countries.insert(2, "Ethiopia")
>>> countries 
['Nigeria', 'USA', 'Ethiopia', 'Mali', 'Ghana', 'London']
>>> countries.pop(2)
'Ethiopia'
>>> countries
['Nigeria', 'USA', 'Mali', 'Ghana', 'London']
>>> countries.remove("Mali")
>>> countries
['Nigeria', 'USA', 'Ghana', 'London']
>>> countries.pop("Ghana")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object cannot be interpreted as an integer
>>> countries
['Nigeria', 'USA', 'Ghana', 'London']
>>> pwd
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'pwd' is not defined
>>> exit()
(base) markeias-mbp:Election_Analysis markeia$ cd..
-bash: cd..: command not found
(base) markeias-mbp:Election_Analysis markeia$ cd ..
(base) markeias-mbp:Python Module markeia$ ls
Activities		Election_Analysis
Activities.zip
(base) markeias-mbp:Python Module markeia$ cd "Activies"
-bash: cd: Activies: No such file or directory
(base) markeias-mbp:Python Module markeia$ cd "Activities"
(base) markeias-mbp:Activities markeia$ ls
A1-Stu_HelloVariableWorld	B4-Stu_NumberChain
A2-Ins_Variables		B5-Ins_Loops
A3-Stu_GroceryList		C1-Stu_ReadNetFlix
A4-Ins_List			C2-Ins_BasicRead
A5-Stu_HobbyBook		C3-Ins_ReadCSV
A6-Ins_Dicts			C4-Ins_WriteCSV
B1-Stu_ConditionalConundrum	D1-Stu_Functions
B2-Ins_Conditionals		D2-Evr_List_Comprehensions
B3-Stu_RockPaperScissors
(base) markeias-mbp:Activities markeia$ cd "A3-Stu_GroceryList"
(base) markeias-mbp:A3-Stu_GroceryList markeia$ ls
Solved		Unsolved
(base) markeias-mbp:A3-Stu_GroceryList markeia$ cd "Unsolved"
(base) markeias-mbp:Unsolved markeia$ ls
grocery_list.py
(base) markeias-mbp:Unsolved markeia$ python3 grocery_list.py
['Creamer', 'Milk', 'Peanut Butter', 'Jelly']
['Creamer', 'Milk', 'Almond Butter', 'Jelly']
['Creamer', 'Milk', 'Almond Butter']
['Creamer', 'Milk', 'Almond Butter', 'Coffee']
(base) markeias-mbp:Unsolved markeia$ python3
Python 3.7.6 (default, Jan  8 2020, 13:42:34) 
[Clang 4.0.1 (tags/RELEASE_401/final)] :: Anaconda, Inc. on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> countries_tuple = ("Mali","Ghana","Ethiopia")
>>> len(countries_tuple)
3
>>> countries_tuple[1]
'Ghana'
>>> countries_tuple(1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object is not callable
>>> countries_tuple[0:1]
('Mali',)
>>> countries_tuple[0:2]
('Mali', 'Ghana')
>>> countries_tuple[:1]
('Mali',)
>>> countries_tuple[:2]
('Mali', 'Ghana')
>>> countries_tuple[:-2]
('Mali',)
>>> countries_tuple[1:2]
('Ghana',)
>>> countries_tuple[-1]
'Ethiopia'
>>> countries_tuple[:-1]
('Mali', 'Ghana')
>>> countries_dict = {Mali:5090
... }
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'Mali' is not defined
>>> countries_dict = {Mali:5000}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'Mali' is not defined
>>> countries_dict["Mali"] = 5000
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'countries_dict' is not defined
>>> countries_dict = {}
>>> countries_dict["Mali"] = 5000
>>> countries_dict = {"Mali": 5000,"Ghana
  File "<stdin>", line 1
    countries_dict = {"Mali": 5000,"Ghana
                                        ^
SyntaxError: EOL while scanning string literal
>>> exit()
(base) markeias-mbp:Unsolved markeia$ python3
Python 3.7.6 (default, Jan  8 2020, 13:42:34) 
[Clang 4.0.1 (tags/RELEASE_401/final)] :: Anaconda, Inc. on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> countries_dict = 
  File "<stdin>", line 1
    countries_dict = 
                    ^
SyntaxError: invalid syntax
>>> countries_dictionary = {"Mali": 5000, "Ghana": 6000, "Ethiopia": 7000}
>>> countries_dictionary
{'Mali': 5000, 'Ghana': 6000, 'Ethiopia': 7000}
>>> print(countries_dictionary)
{'Mali': 5000, 'Ghana': 6000, 'Ethiopia': 7000}
>>> print(f"The voting population of Mali is {countries_dictionary["Mali"]} and the voting population of Ethiopia is {countries_dictionary["Ethiopia"]}")
  File "<stdin>", line 1
    print(f"The voting population of Mali is {countries_dictionary["Mali"]} and the voting population of Ethiopia is {countries_dictionary["Ethiopia"]}")
                                                                       ^
SyntaxError: invalid syntax
>>> print(f"The voting population of Mali is {countries_dictionary ["Mali"]} and the voting population of Ethiopia is {countries_dictionary ["Ethiopia"]}")
  File "<stdin>", line 1
    print(f"The voting population of Mali is {countries_dictionary ["Mali"]} and the voting population of Ethiopia is {countries_dictionary ["Ethiopia"]}")
                                                                        ^
SyntaxError: invalid syntax
>>> print(f'The voting population of Mali is {countries_dictionary ["Mali"]} and the voting population of Ethiopia is {countries_dictionary ["Ethiopia"]}')
The voting population of Mali is 5000 and the voting population of Ethiopia is 7000
>>> countries_dictionary.values
<built-in method values of dict object at 0x107d3d9b0>
>>> countries_dictionary.values()
dict_values([5000, 6000, 7000])
>>> countries_dictionary.items()
dict_items([('Mali', 5000), ('Ghana', 6000), ('Ethiopia', 7000)])
>>> countries_dictionary.keys()
dict_keys(['Mali', 'Ghana', 'Ethiopia'])
>>> print(f"The voting population of Mali is {countries_dictionary ["Mali"]} and the voting population of Ethiopia is {countries_dictionary ["Ethiopia"]}")
  File "<stdin>", line 1
    print(f"The voting population of Mali is {countries_dictionary ["Mali"]} and the voting population of Ethiopia is {countries_dictionary ["Ethiopia"]}")
                                                                        ^
SyntaxError: invalid syntax
>>> countries_dictionary.get("Mali")
5000
>>> countries_dictionary(["Mali"])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'dict' object is not callable
>>> countries_dictionary = dict()
>>> countries_dictionary(["Mali"])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'dict' object is not callable
>>> dict("Mali")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: dictionary update sequence element #0 has length 1; 2 is required
>>> countries_dictionary.get(["Mali"])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
>>> countries_dictionary("Mali")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'dict' object is not callable
>>> countries_dictionary.get["Mali"]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> countries_dictionary[('Mali')]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'Mali'
>>> countries_dictionary[("Mali")]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'Mali'
>>> countries_dictionary.get("Mali")
>>> ext()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'ext' is not defined
>>> exit()
(base) markeias-mbp:Unsolved markeia$ python3
Python 3.7.6 (default, Jan  8 2020, 13:42:34) 
[Clang 4.0.1 (tags/RELEASE_401/final)] :: Anaconda, Inc. on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> countries_dict = {"Mali": 5000, "Ethiopia": 6000, "Ghana": 7000}
>>> countries_dict.get("Mali")
5000
>>> countries_dict["Mali"]
5000
>>> countries_dict[("Mali)]
  File "<stdin>", line 1
    countries_dict[("Mali)]
                          ^
SyntaxError: EOL while scanning string literal
>>> countries_dict[("Mali")]
5000
>>> voting_data
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'voting_data' is not defined
>>>     print(f"The voting population of Mali is {countries_dictionary ["Mali"]} and the voting population of Ethiopia is {countries_dictionary ["Ethiopia"]}")
  File "<stdin>", line 1
    print(f"The voting population of Mali is {countries_dictionary ["Mali"]} and the voting population of Ethiopia is {countries_dictionary ["Ethiopia"]}")
    ^
IndentationError: unexpected indent
>>> exit()
(base) markeias-mbp:Unsolved markeia$ python3
Python 3.7.6 (default, Jan  8 2020, 13:42:34) 
[Clang 4.0.1 (tags/RELEASE_401/final)] :: Anaconda, Inc. on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> my_list = ["Mali","Ethiopia","Nigeria"]
>>> my_list = countries 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'countries' is not defined
>>> "countries" = my_list
  File "<stdin>", line 1
SyntaxError: can't assign to literal
>>> my_list = "countries"
>>> if len("countries")>2:
... "This is a true statement"
  File "<stdin>", line 2
    "This is a true statement"
                             ^
IndentationError: expected an indented block
>>> if len("countries")>2:
... print("this is a true statement")
  File "<stdin>", line 2
    print("this is a true statement")
        ^
IndentationError: expected an indented block
>>> if my_list[1]== "Ethiopia":
... print("this statement is true")
  File "<stdin>", line 2
    print("this statement is true")
        ^
IndentationError: expected an indented block
>>> if my_list[1]== "Ethiopia":
...     print("this statement is true")
... 
>>> 
>>> if my_list[1]== "Ethiopia":
...     print(my_list[1])
... 
>>> exit()
(base) markeias-mbp:Unsolved markeia$ python3
Python 3.7.6 (default, Jan  8 2020, 13:42:34) 
[Clang 4.0.1 (tags/RELEASE_401/final)] :: Anaconda, Inc. on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> counties = ["Arapahoe", "Denver", "Jefferson"]
>>> if counties[1] == "Denver":
...     print(counties[1])
... 
Denver
>>> countries = ["Mali", "Ethiopia", "Ghana"]
>>> if countries[2] == "Ghana":
...     print(countries[2])
... 
Ghana
>>> if countries[1] != "Ethiopia":
...     print(countries[2])
... else:
...     print(countries[1])
... 
Ethiopia
>>> temperature = int(input("what is the temperature outside"))
what is the temperature outside
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: ''
>>> temperature = int(input("what is the temperature outside?"))
what is the temperature outside?
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: ''
>>> temperature = int(input("what is the temperature outside?"))
what is the temperature outside? if temperature > 8
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: ' if temperature > 8'
>>> 
>>> 
>>> 
>>> 
>>> tojakgkagpj
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'tojakgkagpj' is not defined
"""