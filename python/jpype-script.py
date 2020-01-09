#!/usr/bin/env python3

import jpype
from common import jar_path

jpype.startJVM(jpype.getDefaultJVMPath(),
               "-ea",
               "-Djava.class.path=" + jar_path,
               convertStrings=False)

jpype.java.lang.System.out.println("This was printed via System.out.println.")

main = jpype.JPackage("net").talvi.pythonjavabridgedemos.Main("Jeff")
print(main.greet("Morning"))

jpype.shutdownJVM()
