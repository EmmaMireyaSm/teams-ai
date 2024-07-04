# """
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# """

# import shutil
# from pathlib import Path


# def clean():
#     base = Path("./")

#     for e in base.rglob("**/*"):
#         if (
#             e.match("dist")
#             or e.match("__pycache__")
#             or e.match(".pytest_cache")
#             or e.match("coverage")
#         ):
#             if e.is_dir():
#                 print(e)
#                 shutil.rmtree(e)

"""
Copyright (c) Microsoft Corporation. All rights reserved.
Licensed under the MIT License.
"""

import subprocess
from pathlib import Path


for e in Path("./packages").glob("*"):
    if e.is_dir():
        print("------ Package[" + e.name + "] ------")
        subprocess.run(["poetry", "run", "clean"], cwd=e.absolute(), check=True)

for e in Path("./samples").glob("*"):
    if e.is_dir():
        print("------ Sample[" + e.name + "] ------")
        subprocess.run(["poetry", "run", "clean"], cwd=e.absolute(), check=True)
