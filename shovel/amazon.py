
# noinspection PyUnresolvedReferences
from shovel import task
import subprocess
import os

@task
def package():
    print("checking tests are collectable")
    result = subprocess.call("py.test --collect-only tests/", shell=True)
    if result != 0:
        print("test collection failed.")
        exit(1)

    print("generating wheelhouse dependencies.")
    result = subprocess.call("pip wheel --wheel-dir wheelhouse -r requirements.txt", shell=True)
    if result != 0:
        print("Generating wheel failed.")
        exit(1)

    print("cleaning unused files.")
    subprocess.call("find . -name '__pycache__' -type d -exec rm -r {} +", shell=True)
    subprocess.call("find . -name '*.pyc' -exec rm -f {} +", shell=True)
    subprocess.call("find . -name '*.pyo' -exec rm -f {} +", shell=True)
    subprocess.call("find . -name '*~' -exec rm -f {} +", shell=True)

    print("zipping test files.")
    result = subprocess.call("zip -r test_bundle.zip tests/ wheelhouse/ requirements.txt", shell=True)
    if result != 0:
        print("Failed to Zip files for Amazon.")
        exit(1)