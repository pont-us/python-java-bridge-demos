#!/usr/bin/env python3

import jpype
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
jar_path = os.path.join(script_dir, "..", "java", "target",
                        "pythonjavabridgedemos-1.0-SNAPSHOT-"
                        "jar-with-dependencies.jar")

jpype.startJVM(jpype.getDefaultJVMPath(),
               "-ea",
               "-Djava.class.path=" + jar_path,
               convertStrings=False)

jpype.java.lang.System.out.println("test")

main = jpype.JPackage("net").talvi.pythonjavabridgedemos.Main("Jeff")
print(main.greet("Morning"))

jpype.shutdownJVM()
