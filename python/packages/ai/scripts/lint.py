# """
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# """

# import subprocess


# def lint():
#     subprocess.run(["poetry", "run", "pylint", "teams_ai_azml", "scripts", "tests"], check=True)
#     subprocess.run(
#         ["poetry", "run", "mypy", "--check-untyped-defs", "-p", "teams_ai_azml"], check=True
#     )
#     subprocess.run(["poetry", "run", "mypy", "--check-untyped-defs", "-p", "tests"], check=True)

"""
Copyright (c) Microsoft Corporation. All rights reserved.
Licensed under the MIT License.
"""

import subprocess
from pathlib import Path


for e in Path("./packages").glob("*"):
    if e.is_dir():
        print("------ Package[" + e.name + "] ------")
        subprocess.run(["poetry", "run", "lint"], cwd=e.absolute(), check=True)

# for e in Path("./samples").glob("*"):
#     if e.is_dir():
#         print("------ Samples[" + e.name + "] ------")
#         subprocess.run(["poetry", "run", "lint"], cwd=e.absolute(), check=True)
