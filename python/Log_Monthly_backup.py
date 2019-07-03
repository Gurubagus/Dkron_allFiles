from shutil import copyfile
from datetime import datetime
import keyring
import os
import paramiko
import sys
sys.path.append("/home/benemenadmin/PyResources") # Directory for Python classes
import time_limit
from time_limit import *
import emailer


def main():
	try:
		ssh_client=paramiko.SSHClient()
		ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		ssh_client.connect(hostname='80.88.187.155',username='benemen',password=keyring.get_password("talend", "benemen"))
		stdin, stdout, stderr = ssh_client.exec_command('cd /etl/python_jobs && python error_log_monthly_copier.py')
		today = datetime.today()
		string = "Error Log Successfully stored and reset for {}-{}".format(int(today.month) -1, today.year)
		print(string)

		
	except Exception as e:
		print("Error occurred:")
		print(e)
	
	finally:
		if ssh_client:
			ssh_client.close()
		
if __name__=="__main__":
	try:
		with time_limit(600):
			main()
	except TimeoutException as e:
		print("Log_Monthly_Backup time has exceeded the safety limit.")
		emailer.raise_error("Log_Monthly_Backup ERROR","The Log_Monthly_Backup execution time has exceeded the 10 minute safety limit")