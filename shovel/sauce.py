# noinspection PyUnresolvedReferences
from shovel import task
import subprocess
import os

@task
def deploy():
    #command to push file to sauce storage
    print("Publishing APK file to Sauce Storage")
    command = ['curl',
               '-u',
               "{sauce_user}:{sauce_key}".format(sauce_user=os.environ['SAUCE_USER'],sauce_key=os.environ['SAUCE_KEY']), #auth info
               '-X',
               'POST',
               '-H',
               '"Content-Type: application/octet-stream"',
               "https://saucelabs.com/rest/v1/storage/{user}/app-debug.apk?overwrite=true".format(user=os.environ['SAUCE_USER']), #sauce storage location
               '--data-binary',
               '@staging/app-debug.apk'] # file to upload location
    print(' '.join(command))
    result = subprocess.call(' '.join(command), shell=True)
    if result != 0:
        print("Publishing to Sauce Storage Failed.")
        exit(1)

