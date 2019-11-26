#!/usr/bin/env python3

import jnius_config
from common import jar_path

jnius_config.set_classpath(jar_path)

from jnius import autoclass

Main = autoclass("net.talvi.pythonjavabridgedemos.Main")
main = Main("John")
print(main.greet("G'day"))
print("55 + 89 =", main.add(55, 89))
