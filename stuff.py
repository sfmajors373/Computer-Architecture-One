[sarah@endora ~]$ python
Python 3.6.2 (default, Jul 20 2017, 03:52:27)
[GCC 7.1.1 20170630] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
>>> with open('test.txt', 'r') as txtfile:
...     while (line = txtfile.read() != "")
  File "<stdin>", line 2
    while (line = txtfile.read() != "")
                ^
SyntaxError: invalid syntax
>>>     while (line = txtfile.read()) != ""
  File "<stdin>", line 1
    while (line = txtfile.read()) != ""
    ^
IndentationError: unexpected indent
>>>     while (line = txtfile.read()) != "":
  File "<stdin>", line 1
    while (line = txtfile.read()) != "":
    ^
IndentationError: unexpected indent
>>> with open('test.txt', 'r') as txtfile:
...     while (line = txtfile.read()) != "":
  File "<stdin>", line 2
    while (line = txtfile.read()) != "":
                ^
SyntaxError: invalid syntax
>>> with open('test.txt', 'r') as txtfile:
...     while True:
...             line = txtfile.readline()
...

^CTraceback (most recent call last):
  File "<stdin>", line 3, in <module>
KeyboardInterrupt
>>> with open('test.txt', 'r') as txtfile:
...     while True:
...             line = txtfile.readline()
...             if line == "":
...                     break;
...             else:
...                     print(line)
...
1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20

>>> def testcode(txtfile):
...     print(line)
...     line = txtfile.readline()
...
>>> with open('test.txt', 'r') as txtfile:
...     while True:
...             line = txtfile.readline()
...             if line == "":
...                     break;
...             else:
...                     testcode(txtfile)
...
Traceback (most recent call last):
  File "<stdin>", line 7, in <module>
  File "<stdin>", line 2, in testcode
UnboundLocalError: local variable 'line' referenced before assignment
>>> def testcode2(txtfile):
...     line = txtfile.readline()
...     print(line)
...
>>> with open('test.txt', 'r') as txtfile:
...     while True:
...             if line == "":
...                     break;
...             else:
...                     testcode2(txtfile)
  File "<stdin>", line 5
    else:
        ^
IndentationError: expected an indented block
>>> with open('test.txt', 'r') as txtfile:
...     line = txtfile.readline()
...     while True:
KeyboardInterrupt
>>> with open('test.txt', 'r') as txtfile:
...     while True:
...             line = txtfile.readline()
...             if line == "":
...                     break;
...             else:
...                     testcode2(txtfile)
...
2

4

6

8

10

12

14

16

18

20

>>>

