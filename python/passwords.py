import keyring
import getpass

def main():

	system = raw_input('System:')
	username = raw_input('Please input username:')
	keyring.set_password(system,username,getpass.getpass())
	print('The password for ' +username+' in '+system+' has been set.\nPlease do not forget, you will not be able to recover at this point.\nFor misplaced passwords, please resubmit new entry.')
	
if __name__=='__main__':
	print('Please input the system in which the password will be used,\nand corresponding username.')
	main()