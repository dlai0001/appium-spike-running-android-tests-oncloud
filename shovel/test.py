# noinspection PyUnresolvedReferences
from shovel import task
from subprocess import PIPE
import subprocess


@task
def run():
    command = ['py.test',
               'tests/',
               '--junitxml=results.xml']

    print(' '.join(command))
    result = subprocess.call(' '.join(command), shell=True)
    if result != 0:
        exit(1)