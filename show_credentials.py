#!/usr/bin/env python
#
# Show credentials if any

file=open('.credentials')

for line in file:
  if line.startswith('username'):
    print line.split()[-1]
  if line.startswith('password'):
    print line.split()[-1]
