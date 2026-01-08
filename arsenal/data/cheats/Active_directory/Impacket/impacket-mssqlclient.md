# impacket-mssqlclient

## impacket-mssqlclient - Login with Windows-Auth
```
impacket-mssqlclient <domain>/'<username>'@<ip> -windows-auth
```

## impacket-mssqlclient - Connect using SQL server authentication
```
impacket-mssqlclient '<username>':'<password>'@<ip>
```

## impacket-mssqlclient - Connect using pass-the-hash authentication
```
impacket-mssqlclient <domain>/'<username>'@<ip> -hashes <hash>
```

## impacket-mssqlclient - Connect using Kerberos authentication (requires valid tickets):
```
impacket-mssqlclient -k <domain>/'<username>'@<ip>
```

## impacket-mssqlclient - Execute a specific SQL command upon connection
```
impacket-mssqlclient '<username>':'<password>'@<ip> -query "<QUERY>"
```

## impacket-mssqlclient - Execute multiple SQL commands from a file
```
impacket-mssqlclient '<username>':'<password>'@<ip> -file '<sql_file>'
```

## impacket-mssqlclient - Connect to a specific database instance (default is None):
```
impacket-mssqlclient '<username>':'<password>'@<ip> -db <database>
```