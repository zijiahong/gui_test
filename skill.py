import pid,os 
ids = pid.get_pid("dnf")
print(ids)
for id in ids:
	cmd = 'taskkill -f -pid %s' % id
	print(cmd)
	os.system(cmd)