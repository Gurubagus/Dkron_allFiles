import paramiko	
import gitlab
import keyring
import sys
sys.path.append("/home/benemenadmin/PyResources") # Directory for Python classes
import time_limit
from time_limit import *
import emailer

ssh_client= None

def main():
	try:
		ssh_client=paramiko.SSHClient()
		ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		ssh_client.connect(hostname='80.88.187.155',username='benemen',password=keyring.get_password("talend", "benemen"))
		stdin, stdout, stderr = ssh_client.exec_command("/usr/bin/bash -lc 'cd /etl/talend_jobs ; /etl/cronjobs/minute_jobs.sh' 1>/dev/null 2>/etl/logs/1minute_jobs.txt")
		out = stdout.read()
		print(out)
	except Exception as e:
		print('The following error has occurred during the XRM_Jobs dkron process')
		print(e.message)
	finally:
		if ssh_client:
			ssh_client.close()
		print('\n1Minute_Jobs complete\n')

			
if __name__ == '__main__':
	try:
		with time_limit(120):
			main()
	except TimeoutException as e:
		print("1minute_jobs time has exceeded the safety limit.")
		emailer.raise_error("1minute_jobs ERROR","The 1minute_jobs execution time has exceeded the 2 minute safety limit")