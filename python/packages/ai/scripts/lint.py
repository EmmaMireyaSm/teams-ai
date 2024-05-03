"""
Copyright (c) Microsoft Corporation. All rights reserved.
Licensed under the MIT License.
"""

import subprocess


def lint():
    subprocess.run(["poetry", "run", "pylint", "teams_ai_azml", "scripts", "tests"], check=True)
    subprocess.run(
        ["poetry", "run", "mypy", "--check-untyped-defs", "-p", "teams_ai_azml"], check=True
    )
    subprocess.run(["poetry", "run", "mypy", "--check-untyped-defs", "-p", "tests"], check=True)
