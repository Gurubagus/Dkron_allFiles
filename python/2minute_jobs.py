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
		stdin, stdout, stderr = ssh_client.exec_command("/usr/bin/bash -lc '/etl/cronjobs/2minute_jobs.sh' 1>/dev/null 2>/etl/logs/2minute_jobs.txt")
		out = stdout.read()
		print(out)
	except Exception as e:
		print('The following error has occurred during the XRM_Jobs dkron process')
		print(e.message)
	finally:
		if ssh_client:
			ssh_client.close()
		print('\n2Minute_Jobs complete\n')

			
if __name__ == '__main__':
	try:
		with time_limit(180):
			main()
	except TimeoutException as e:
		print("2minute_jobs time has exceeded the safety limit.")
		emailer.raise_error("2minute_jobs ERROR","The 2minute_jobs execution time has exceeded the 3 minute safety limit")