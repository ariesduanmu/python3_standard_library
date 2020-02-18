# PIPE not work in win
import subprocess

print("write: ")
proc = subprocess.Popen(
	['cat', '-'], # this hangs and wait user input then echo that
	stdin=subprocess.PIPE,
	)
proc.communicate('stdin: to stdin\n'.encode('utf-8'))
