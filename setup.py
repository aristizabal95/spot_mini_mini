import os
from setuptools import setup, find_packages

def get_packages():
    path = os.path.dirname(__file__)
    contents = os.listdir(path)
    contents = [asset for asset in contents if os.path.isdir(os.path.join(path, asset))]
    return contents

with open("requirements.txt", "r") as f:
    requires = []
    for line in f:
        req = line.split("#", 1)[0].strip()
        if req and not req.startswith("--"):
            requires.append(req)

setup(name='spotmicro',
      version='0.0.0',
      author="Spot Micro AI",
      packages=["spotmicro"],
      install_requires=requires,

    )