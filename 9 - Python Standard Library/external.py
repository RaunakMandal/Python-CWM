import subprocess

# Legacy:
# subprocess.call
# subprocess.check_call
# subprocess.check_output
# subprocess.Popen

# New:
completed = subprocess.run(["python", "other.py"],
                           capture_output=True, text=True)
print("args", completed.args)
print("returncode", completed.returncode)
print("stdout", completed.stdout)
if completed.returncode != 0:
    print("stderr", completed.stderr)
