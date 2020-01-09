#!/usr/bin/env python3

# Demonstration script for jpy

from common import jar_path
import jpy

jpy.create_jvm(["-Djava.class.path=" + jar_path])
StringBuilder = jpy.get_type("java.lang.StringBuilder")
sb = StringBuilder()
sb.append("Demonstration of ")
sb.append("StringBuilder")
print(sb.toString())

Main = jpy.get_type("net.talvi.pythonjavabridgedemos.Main")
main = Main("Bob")
print(main.greet("Wotcha"))
