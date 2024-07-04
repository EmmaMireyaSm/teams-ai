# """
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# """

# import subprocess


# def ci():
#     subprocess.run(["poetry", "check"], check=True)
#     subprocess.run(["poetry", "run", "lint"], check=True)
#     subprocess.run(["poetry", "run", "test"], check=True)
#     subprocess.run(["poetry", "build"], check=True)

"""
Copyright (c) Microsoft Corporation. All rights reserved.
Licensed under the MIT License.
"""

import subprocess
from pathlib import Path


for e in Path("./packages").glob("*"):
    if e.is_dir():
        print("------ Package[" + e.name + "] ------")
        subprocess.run(["poetry", "run", "ci"], cwd=e.absolute(), check=True)

# for e in Path("./samples").glob("*"):
#     if e.is_dir():
#         print("------ Sample[" + e.name + "] ------")
#         subprocess.run(["poetry", "run", "ci"], cwd=e.absolute(), check=True)
