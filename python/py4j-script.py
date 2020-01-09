#!/usr/bin/env python3

from py4j.java_gateway import JavaGateway

gateway = JavaGateway()

# Demonstrate use of standard Java classes.

cal = gateway.jvm.java.util.\
    GregorianCalendar(2008, gateway.jvm.java.util.Calendar.DECEMBER, 3)
weekday = cal.getDisplayName(gateway.jvm.java.util.Calendar.DAY_OF_WEEK,
                             gateway.jvm.java.util.Calendar.LONG_FORMAT,
                             gateway.jvm.java.util.Locale.ENGLISH)
print("Python 3 was released on a {}.".format(weekday))

# Demonstrate use of the class provided as an entry point.

print(gateway.entry_point.greet("Salutations"))

# Demonstrate instantiation and use of a third-party class.

main = gateway.jvm.net.talvi.pythonjavabridgedemos.Main("Trismestigus")
print(main.greet("Felicitations"))
