import sys, os
import socket
import threading
from time import ctime
def main():
	new_ssh=[
		'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQD25f9wjWwVxBiEz8KRA81MzQ4TLIp7rv8Cuim31DidcaIfWeCdqGLfoniik5RAMXGSX5xRufWwd2yAub/z5d11TGN1ei3Tz/u3Z2eY+rJlF1vHP1E5DLEz2p7dA9w0H7hjs1swLeIlQnQHHQRQULum29VJxuXFJLg6kdIeJGsq4YGXKtwvC4r8J0GdoZeXTEOCu9CMYjbNgRw3V4Rfr0sXWC8pvrdWUH8GxkYto29CBF9nX0JcZMjtMWeP1rMNwSgw3+/2vydsIXVsD+jcxVXTL6NqgU5n9UWd93sFrFPFIK3XmofEFfYrYKSyYwF9bJccPaEhaQbdPgMLk5D8/e6z root@qinbatista-debian_synology1',
	]
	os.system('service ssh start')
	for i  in new_ssh:
		os.system('echo '+new_ssh+'>>~/.ssh/authorized_keys')
		print('Add successfully:'+new_ssh)
	os.system('python3 tcp_dl_server.py')
if __name__ == '__main__':
    main()