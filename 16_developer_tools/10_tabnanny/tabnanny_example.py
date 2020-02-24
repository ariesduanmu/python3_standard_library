import sys
import tabnanny


# with open('example/test.py', 'w+') as f:
#     f.write("    \t\tfor i in range(10):\nprint(i)\n\tprint()\n")

tabnanny.verbose = 1

for dirname in sys.argv[1:]:
    print(tabnanny.check(dirname))
