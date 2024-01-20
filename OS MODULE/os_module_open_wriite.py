#IT CAN CREATE AFILE NAME GIVEN BY YOU
#AND WRITE ANYTHING WRINTEN BY YOU IN WRITE(CODE)
import os
fd = "kumar_aadarsh.txt"

# popen() is similar to open()
file = open(fd, 'w')
file.write("Hello\nI am yours\nlovely boy badshah")
file.close()
file = open(fd, 'r')
text = file.read()
print(text)

# popen() provides a pipe/gateway and accesses the file directly
file = os.popen(fd, 'w')
file.write("Hello")
# File not closed, shown in next function.
