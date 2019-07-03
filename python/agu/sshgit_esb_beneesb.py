# FUTURE REFERENCE: set remote url to https://username(w/o "@.com"):password@gitlab.beneservices.com/BI_Labs/<dir>.git

import paramiko	
import gitlab
import keyring

ssh_client= None

def main():
	print('\n*************BENE ESB backup: Starting*************\n')
	try:
		ssh_client=paramiko.SSHClient()
		ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		ssh_client.connect(hostname='80.88.187.171',username='BENEG1\Administrator',password=keyring.get_password("esb","administrator"))
		stdin, stdout, stderr = ssh_client.exec_command('d: && cd \TalendOS_ESB\Studio\workspace\BENE_ESB && git add -A && git commit -m \"test commit\" && git push origin master')
		out = stdout.read()
		print(out)
	except Exception as e:
		print('The following error has occurred during the BENE ESB backup process')
		print(e.message)
	finally:
		if ssh_client:
			ssh_client.close()
		print('\n*************BENE ESB backup: Complete*************\n')

			
if __name__ == '__main__':
	main()