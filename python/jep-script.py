from java.util import ArrayList
from net.talvi.pythonjavabridgedemos import Main

# Test use of classes from the Java runtime
al = ArrayList()
al.add(2)
al.add(2)
print("2 + 2 =", al.stream().mapToInt(lambda x: x).sum())

# Test use of a class from a third-party jar
main = Main("sailor")
print(main.greet("Hello"))
