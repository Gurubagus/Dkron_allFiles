# FUTURE REFERENCE: set remote url to https://username(w/o "@.com"):password@gitlab.beneservices.com/BI_Labs/<dir>.git

import paramiko	
import gitlab
import keyring

ssh_client= None

def main():
	print('\n*************QlikSense BeneReports Production backup: Starting*************\n')
	try:
		ssh_client=paramiko.SSHClient()
		ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		#ssh_client.connect(hostname='10.252.35.240',username='BENEG1\\Qlik_Admin',password='fh73&w2"DF')
		ssh_client.connect(hostname='10.252.35.240',username='BENEG1\\Qlik_Admin',password=keyring.get_password("qlik","beneg1\qlik_admin"))
		stdin, stdout, stderr = ssh_client.exec_command("cd \inetpub\wwwroot\BeneReports && git add -A && git commit -m \"auto-upload\" && git push origin master")
		out = stdout.read()
		print(out)
	except Exception as e:
		print('The following error has occurred during the QlikSense BeneReports Production backup process')
		print(e.message)
	finally:
		if ssh_client:
			ssh_client.close()
		print('\n*************QlikSense BeneReports Production backup: Complete*************\n')

			
if __name__ == '__main__':
	main()
	