# Shared code for Python scripts

import os

script_dir = os.path.dirname(os.path.abspath(__file__))
jar_path = os.path.join(script_dir, "..", "java", "target",
                        "pythonjavabridgedemos-1.0.jar")
