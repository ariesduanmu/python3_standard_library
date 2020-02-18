import subprocess

try:
	completed = subprocess.run(
		'echo to stdout; echo to stderr 1>&2; exit 1',
		shell=True,
		check=False,
		stdout=subprocess.PIPE,
		stderr=subprocess.PIPE,
		)
except subprocess.CalledProcessError as err:
	print(f"[-] Error: {err}")
else:
	print(f"returncode: {completed.returncode}")
	print(f"Have {len(completed.stdout)} bytes in stdout: {completed.stdout}")
	print(f"Have {len(completed.stderr)} bytes in stderr: {completed.stderr}")