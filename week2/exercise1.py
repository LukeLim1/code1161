"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"
# I think this line will print 'what does this line do?' when I execute it.
some_words = ['what', 'does', 'this', 'line', 'do', '?']  # It printed 'what does this line do?', but each word in a separate line.
for word in some_words:
    print(word)
for x in some_words:
    print(x)
# I think this will print 'what does this line do?' in each line
print(some_words)
# It would print 'some_words contains more than 3 words' since len(some_words) > 3
if len(some_words) > 3:
    print('some_words contains more than 3 words') # It printed 'some_words contains more than 3 words'

def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    print(platform.uname())

usefulFunction()
