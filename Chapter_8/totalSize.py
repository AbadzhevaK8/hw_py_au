#! python3
#! /usr/bin/python3

import os
totalSize = 0
for filename in os.listdir('/usr/bin'):
  totalSize = totalSize + os.path.getsize(os.path.join('/usr/bin', filename))
print(totalSize)
