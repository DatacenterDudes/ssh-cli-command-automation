# Paramiko is a Python implementation of the SSHv2 protocol, providing both client and server functionality
import paramiko

#Define the variables required to SSH into a client
ssh = paramiko.SSHClient()

#Auto accepts unknown keys - do not use if connecting to an untrusted machine
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#Example ssh.conect('10.255.55.100', username='admin', password='Netapp1!'
ssh.connect('$host_ip', username='$username', password='$password')

#Example cli_commands = ['cluster show', 'network interface show']
cli_commands = ['$cli_command_1', '$cli_command_2', '$etc']

#Function to execute commands
def run_command(command):
    #Set Standard In, Standard Output, and Standard Error for SSH to the exeucted command
    stdin,stdout,stderr = ssh.exec_command(command)

    print('*** ' + command + ' ***')
    print('')

    #Read and print all lines from command output
    for line in iter(stdout.readline, ''):
        print line.rstrip()

    print('')

#Run through all commands in the cli_commands list and execute in the command function
for commands in cli_commands:
    run_command(commands)

#Close the SSH Session
ssh.close()
