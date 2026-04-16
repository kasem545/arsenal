# impacket-mssqlclient

## impacket-mssqlclient - Login with Windows-Auth
```
impacket-mssqlclient <DOMAIN>/'<username>'@<IP> -windows-auth
```

## impacket-mssqlclient - Connect using SQL server authentication
```
impacket-mssqlclient '<username>':'<PASSWORD>'@<IP>
```

## impacket-mssqlclient - Connect using pass-the-hash authentication
```
impacket-mssqlclient <DOMAIN>/'<username>'@<IP> -hashes <HASH>
```

## impacket-mssqlclient - Connect using Kerberos authentication (requires valid tickets):
```
impacket-mssqlclient -k <DOMAIN>/'<username>'@<IP>
```

## impacket-mssqlclient - Execute a specific SQL command upon connection
```
impacket-mssqlclient '<username>':'<PASSWORD>'@<IP> -query '<QUERY>'
```

## impacket-mssqlclient - Execute multiple SQL commands from a file
```
impacket-mssqlclient '<username>':'<PASSWORD>'@<IP> -file '<sql_file>'
```

## impacket-mssqlclient - Connect to a specific database instance (default is None):
```
impacket-mssqlclient '<username>':'<PASSWORD>'@<IP> -db <database>
```