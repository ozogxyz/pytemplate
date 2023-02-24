import subprocess

subprocess.call(["git", "init"])
subprocess.call(["git", "add", "*"])
subprocess.call(["git", "commit", "-m", "Initial commit"])
subprocess.call(["pre-commit", "install"])
subprocess.call(["pre-commit", "run", "--all-files"])
