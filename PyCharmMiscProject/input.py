
#input() take user input
#in string strip()used in removing space from right and left side of user input
#title()function used in capitalising first letter of word
name = input("What is your Name ? : ").strip().title()
#fstring (f)
print(f"Hello,{name} we welcome you")

"""
Prints the values to a stream, or to sys.stdout by default.


sep
string inserted between values, default a space.
end
string appended after the last value, default a newline.
file
a file-like object (stream); defaults to the current sys.stdout.
flush
whether to forcibly flush the stream.
`print(*values, sep=" ", end="\n", file=None, flush=False)` on docs.python.org 
"""

