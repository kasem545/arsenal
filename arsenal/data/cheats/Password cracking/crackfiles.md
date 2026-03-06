# Crack files

% bruteforce, crack, files

#plateform/linux  #target/local  #cat/CRACKING/PASSWORD 

# John the Ripper *2john Cheatsheet

## ZIP - john
```
zip2john <zip_file> > <output_file|hash>
```

## RAR - john
```
rar2john <rar_file> > <output_file|hash>
```

## 7-Zip - john
```
7z2john <7z_file> > <output_file|hash>
```

## TAR - john
```
tar2john <tar_file> > <output_file|hash>
```

## PDF - john
```
pdf2john <pdf_file> > <output_file|hash>
```

## Microsoft Office (Modern) - john
```
office2john <docx|xlsx|pptx_file> > <output_file|hash>
```

## TrueCrypt - john
```
truecrypt2john <container_file> > <output_file|hash>
```

## BitLocker - john
```
bitlocker2john -i <image_file> > <output_file|hash>
```

## LUKS - john
```
luks2john <luks_image> > <output_file|hash>
```

## WPA/WPA2 Capture - john
```
hccap2john <capture_file> > <output_file|hash>
```

## PCAP Capture - john
```
pcap2john <pcap_file> > <output_file|hash>
```

## SSH Private Key - john
```
ssh2john <id_rsa> > <output_file|hash>
```

## PuTTY Key - john
```
putty2john <ppk_file> > <output_file|hash>
```

## PKCS#12 Certificate - john
```
pfx2john <pfx_file> > <output_file|hash>
```

## KeePass Database - john
```
keepass2john <database.kdbx> > <output_file|hash>
```

## Password Safe - john
```
pwsafe2john <database.psafe3> > <output_file|hash>
```

## LastPass Export - john
```
lastpass2john <lastpass_export> > <output_file|hash>
```

## macOS DMG - john
```
dmg2john <image.dmg> > <output_file|hash>
```

## Bitcoin Wallet - john
```
bitcoin2john <wallet.dat> > <output_file|hash>
```

## Ethereum Wallet - john
```
ethereum2john <wallet.json> > <output_file|hash>
```

= wordlist: /usr/share/wordlists/rockyou.txt
