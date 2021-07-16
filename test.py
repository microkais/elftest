from pwn import *
e=process('/a.out')
first_name='secret\n'
goal='\x05\x1d\x0d\x04\x10\X72'
last_name=''.join([chr(ord(first_name[i])^ord(goal[i]))for i in range(6)])+'\n'
print(e.recv().decode())
e.send(first_name.encode())
print(e.recv().decode())
e.send(last_name.encode())
print(e.recv().decode())
