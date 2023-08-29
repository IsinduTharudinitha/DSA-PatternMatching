# User-Defined Regex
Implement Regex characters using the Knuth-Morris-Pratt (KMP) string matching algorithm. The solution was done using the Python programming language. 

<br /><br />
## How to run?
First, go to the [main.py]() file. This is the code file in this scenario. You can run it using your own test cases and open the [patternmatch.txt]() file to view the outputs. If you want to add a new test case, go to the [pattern.txt]()  and [text.txt]() files to create your own test case.


<br />

You can change this text file name to your own file name.
```python
text = open("text.txt", 'r')
pattern = open("pattern.txt", 'r')
output = open("patternmatch.output", 'w')
```

`regExpression.py` contains the Regex file, and the main file imports functions from the `regExpression.py` file.
<br/><br/>
#
First, import `regExpression.py` and set the alias to re. Because `regExpression` is too long and hard to handle.
```python
import regExpression as re
```

<br /><br />

## Method
I use the `Knuth-Morris-Pratt (KMP)` algorithm to implement this and filter the pattern using simple if statements. Also, the matiching condition is called to the relevant function, and the output is given as a Boolean value.

```python
def search(Str, Pattern):
    
    if any(i == '|' for i in Pattern):
        return search(Str, Pattern.split('|')[0]) or search(Str, Pattern.split('|')[1])

    
    elif Pattern[0] == "^" and Pattern[-1] == "$":
        return start_with_and_ends_with(Str, Pattern)

    
    elif Pattern[0] == "^":
        return startWith(Str, Pattern)

    
    elif Pattern[-1] == "$":
        return endsWith(Str, Pattern)

    
    return kmp(Str, Pattern)
```

In this version, the program recognizes `^` `|` `$` as the regex character.


____

