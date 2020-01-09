# This is a pure Python demo script, in the sense that it doesn't
# explicitly invoke any Python/Java bridge framework. It expects to find
# the Java demo package net.talvi.pythonjavabridgedemos available for
# import as a Python package, and expects an instance of the Java demo
# class Main bound to the name "main". It can be invoked from Jep and
# from Jython.

from java.util import ArrayList
from net.talvi.pythonjavabridgedemos import Main

# Demonstrate use of classes from the Java runtime.
al = ArrayList()
al.add(2)
al.add(2)
print("2 + 2 =", al.stream().mapToInt(lambda x: x).sum())

# Demonstrate use of a preset variable.
print(main.greet("Hello"))

# Demonstrate instantiation and use of a class from a third-party jar.
my_main = Main("Medea")
print(my_main.greet("Good health"))
