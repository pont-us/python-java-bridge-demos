#!/usr/bin/env jep

# Demonstration script for Jep.

# Demonstrate use of classes from the Java runtime.

from java.util import *
cal = GregorianCalendar(2008, Calendar.DECEMBER, 3)
weekday = cal.getDisplayName(Calendar.DAY_OF_WEEK,
                             Calendar.LONG_FORMAT,
                             Locale.ENGLISH)
print("Python 3 was released on a {}.".format(weekday))

# Use of third-party jars is not demonstrated here since it is not possible to
# import jar files from within Jep's Python interpreter, but they can be
# used by setting the CLASSPATH variable before starting Jep.
