import paramiko	
import re
import keyring
import sys
sys.path.append("/home/benemenadmin/PyResources") # Directory for Python classes
import emailer
import time_limit
from time_limit import *
import datetime

ssh_client= None
server_address='80.88.187.155'
server_username='benemen'
server_pass = keyring.get_password('ssh','benemen')
command = "yum clean all; rm -rf /var/cache/yum"

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
		session.exec_command("sudo bash -c \"" + command + "\"")
		stdin = session.makefile('wb', -1)
		stdout = session.makefile('rb', -1)
		stdin.write(server_pass + '\n')
		stdin.flush()
		#print(stdout.read().decode("utf-8"))
	except Exception as e:
		print("The following error has occurred during your requested process")
		print(e.message)	
		emailer.raise_error("EDW encountered an error at {}".format(datetime.datetime.now()), "The ETL YUM Cleaner encountered the following error: {}.".format(e.message))
	finally:
		if ssh:
			session.close()
			ssh.close()
		print('\n yum clean all and rm -rf /var/cache/yum run successfully.\n')

			
if __name__ == '__main__':
	try:
		with time_limit(180):
			main(command, server_address, server_username, server_pass)
	except TimeoutException as e:
		print("Execution time has exceeded the safety limit.")
		emailer.raise_error("ETL/YUM Cleaner ERROR","The ETL YUM Cleaner job execution time has exceeded the safety limit")