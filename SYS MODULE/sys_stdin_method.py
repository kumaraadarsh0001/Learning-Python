import sys
a=sys.stdin.read(5)
sys.stdout.write(a)
b=sys.stdin.read(10)
sys.stdout.write(b)
sys.stderr.write('Custom Error Message')