# hashcat

% password recovery, password cracking

#plateform/linux  #target/local  #cat/CRACKING/PASSWORD 

## hashcat - md5 - wordlist
```
hashcat -m 0 <hash_file> <wordlist>
```

## hashcat - basic md5 (joomla/wordpress $P$) - wordlist
```
hashcat -m 400 <hash_file> <wordlist>
```

## hashcat - basic md5 (joomla/wordpress $P$) - wordlist with rules
```
hashcat -m 400 <hash_file> <wordlist> -r /usr/share/doc/hashcat/rules/best64.rule 
```

## hashcat - kerberos ticket (TGS-REP)
```
hashcat -m 13100 <hash_file> <wordlist> --force 
```

## hashcat - kerberos ticket (AS-REP)
```
hashcat -m 18200 <hash_file> <wordlist> --force 
```

## hashcat - Domain Cached Credentials (DCC2)
```
hashcat -m 2100 <hash_file> <wordlist> --force 
```
## hashcat - LM
```
hashcat -m 3000 <hash_file> <wordlist> 
```

## hashcat - bcrypt Blowfish 
```
hashcat -m 3200 <hash_file> <wordlist> 
```

## hashcat - NTLM
```
hashcat -m 1000 <hash_file> <wordlist> 
```

## hashcat - NTLMv1
```
hashcat -m 5500 <hash_file> <wordlist> 
```

## hashcat - NTLMv2
```
hashcat -m 5600 <hash_file> <wordlist> 
```

## hashcat - NTLMv2 - Combination attack (ex:passpass,testtest,passtest,etc)
```
hashcat -m 5600 <hash_file> <wordlist> --force
```

## hashcat - generate wordlist using rules
```
cat keywords.txt | hashcat -r <rule_file> --stdout > ./<custom_wordlist>
```

= wordlist: /usr/share/wordlist/rockyou.txt
= rule_file: /usr/share/doc/hashcat/rules/best64.rule 
= custom_wordlist: wordlist.lst