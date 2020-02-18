import hashlib
import sys
import os


def choose_algorithm():
	algorithms = list(hashlib.algorithms_available)
	for idx, algorithm in enumerate(algorithms):
		print(idx+1, algorithm)
	num = len(algorithms)

	choosed = 0

	while True:
		choosed = input(f"Choose the hash algorithm you wanna use(1-{num}): ")
		if choosed.isdigit() and 1 <= int(choosed) <= num:
			choosed = int(choosed)
			break
		else:
			exit = input("Illegal input, do you wanna exit(y/n): ")
			if exit.lower() == "y":
				sys.exit(0)

	if choosed < 1 or choosed > num:
		sys.exit(1)

	return algorithms[int(choosed)-1]

def crypto_data():
	path = input(f"Data to hash, file path: ")
	if not os.path.exists(path):
		print(f"{path} not exists, exiting...")
		sys.exit(1)

	with open(path, 'rb') as f:
		content = f.read()
	return content, path

def main():
	algorithm = choose_algorithm()
	data, path = crypto_data()
	print(f"Hashing({algorithm}) file({path})...")
	h = hashlib.new(algorithm)
	h.update(data)
	print(h.hexdigest())

if __name__ == "__main__":
	main()