# Crack files

% bruteforce, crack, files

#plateform/linux  #target/local  #cat/CRACKING/PASSWORD 

# John the Ripper *2john Cheatsheet

## ZIP - john
```
zip2john <FILE> > <OUTFILE|hash>
```

## RAR - john
```
rar2john <FILE> > <OUTFILE|hash>
```

## 7-Zip - john
```
7z2john <FILE> > <OUTFILE|hash>
```

## TAR - john
```
tar2john <FILE> > <OUTFILE|hash>
```

## PDF - john
```
pdf2john <FILE> > <OUTFILE|hash>
```

## Microsoft Office (Modern) - john
```
office2john <docx|xlsx|pptx_file> > <OUTFILE|hash>
```

## TrueCrypt - john
```
truecrypt2john <container_file> > <OUTFILE|hash>
```

## BitLocker - john
```
bitlocker2john -i <image_file> > <OUTFILE|hash>
```

## LUKS - john
```
luks2john <luks_image> > <OUTFILE|hash>
```

## WPA/WPA2 Capture - john
```
hccap2john <capture_file> > <OUTFILE|hash>
```

## PCAP Capture - john
```
pcap2john <pcap_file> > <OUTFILE|hash>
```

## SSH Private Key - john
```
ssh2john <id_rsa> > <OUTFILE|hash>
```

## PuTTY Key - john
```
putty2john <ppk_file> > <OUTFILE|hash>
```

## PKCS#12 Certificate - john
```
pfx2john <pfx_file> > <OUTFILE|hash>
```

## KeePass Database - john
```
keepass2john <database.kdbx> > <OUTFILE|hash>
```

## Password Safe - john
```
pwsafe2john <database.psafe3> > <OUTFILE|hash>
```

## LastPass Export - john
```
lastpass2john <lastpass_export> > <OUTFILE|hash>
```

## macOS DMG - john
```
dmg2john <image.dmg> > <OUTFILE|hash>
```

## Bitcoin Wallet - john
```
bitcoin2john <wallet.dat> > <OUTFILE|hash>
```

## Ethereum Wallet - john
```
ethereum2john <wallet.json> > <OUTFILE|hash>
```

= wordlist: /usr/share/wordlists/rockyou.txt
