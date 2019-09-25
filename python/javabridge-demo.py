#!/usr/bin/env python3

import os
import javabridge

javabridge.start_vm(run_headless=True, class_path=javabridge.JARS +
                    ["../java/target/pythonjavabridgedemos-1.0-SNAPSHOT.jar"])
try:
    # Bind a Java variable and run a script that uses it.
    print(javabridge.run_script(
        'java.lang.String.format("Hello, %s!", greetee);',
        dict(greetee="world")))

    # Wrap a Java object and call some of its methods.
    array_list = javabridge.JWrapper(javabridge.make_instance(
        "java/util/ArrayList", "()V"))
    array_list.add("ArrayList item 1")
    array_list.add("ArrayList item 2")
    print("ArrayList size:", array_list.size())
    print("First ArrayList item:", array_list.get(0))

    # Wrap a Java object from our jar and call a method.
    main1 = javabridge.JWrapper(javabridge.make_instance(
        "net/talvi/pythonjavabridgedemos/Main",
        "(Ljava/lang/String;)V", "Alice"))
    print(main1.greet("Hello"))

    # Wrap a Java object using JClassWrapper (no signature required)
    main2 = javabridge.JClassWrapper(
        "net.talvi.pythonjavabridgedemos.Main")("Bob")
    print(main2.greet("Hi there"))
    print("2 + 2 = ", main2.add(2, 2))


finally:
    javabridge.kill_vm()
