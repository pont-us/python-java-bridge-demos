#!/usr/bin/env jython

# This is a standalone jython demo script, demonstrating access to classes
# from the Java runtime and from a third-party jar.

from common import jar_path
import sys

# Demonstrate use of classes from the Java runtime.
from java.util import ArrayList
al = ArrayList()
al.add(2)
al.add(2)
print "2 + 2 =", al.stream().mapToInt(lambda x: x).sum()

# Jython lets us add jar files to sys.path.
sys.path.append(jar_path)

# Import a Java class from the jar file added above.
from net.talvi.pythonjavabridgedemos import Main

# Demonstrate instantiation and use of a class from a third-party jar.
my_main = Main("Medea")
print my_main.greet("Good health")
