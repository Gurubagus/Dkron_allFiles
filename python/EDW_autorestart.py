import paramiko	
import re
import keyring
import datetime
import sys
sys.path.append("/home/benemenadmin/PyResources") # Directory for Python classes
import emailer
from time_limit import *

ssh_client= None
server_address='80.88.187.33'
server_username='gpadmin'
server_pass = keyring.get_password('ssh','gpadmin')
command = "gpstate -q"
restart = "gpstart -a"

def main(command, server_address, server_username, server_pass):
	try:
		ssh = paramiko.SSHClient()
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		ssh.connect(hostname=server_address,
					username=server_username,
					password=server_pass)
		session = ssh.get_transport().open_session()
		session.set_combine_stderr(True)
		session.get_pty()
		session.exec_command(command)
		stdin = session.makefile('wb', -1)
		stdout = session.makefile('rb', -1)
		out = stdout.read().decode("utf-8")
		
		if len(out) > 0:
			session.exec_command(restart)
			ts = datetime.datetime.now()
			print('Restart Required at %s')	% ts
			emailer.raise_error("EDW required a restart at {}".format(ts), "The Autorestart job found the EDW server to be inactive and send the command for a restart as of {}.".format(ts))
		else:
			ts = datetime.datetime.now()
			print('Server Active as of %s')	% ts
		
	except Exception as e:
		print("The following error has occurred during your requested process")
		print(e.message)
		emailer.raise_error("EDW Autorestart ERROR","The Autorestart job experienced the following error: {}".format(e.message))
	
	finally:
		if ssh:
			session.close()
			ssh.close()

			
if __name__ == '__main__':
	try:
		with time_limit(180):
			main(command, server_address, server_username, server_pass)
		
	except TimeoutException as e:
		print("Execution time has exceeded the safety limit.")
		emailer.raise_error("EDW Autorestart ERROR","The Autorestart job execution time has exceeded the safety limit")