# hashcat

% password recovery, password cracking

#plateform/linux  #target/local  #cat/CRACKING/PASSWORD 

## hashcat - wordlist generation
```
hashcat -r <RULE_FILE> --stdout <WORDLIST> > <OUTFILE>
```

## hashcat - md5 - wordlist
```
hashcat -m 0 <HASH_FILE> <WORDLIST>
```

## hashcat - basic md5 (joomla/wordpress $P$) - wordlist
```
hashcat -m 400 <HASH_FILE> <WORDLIST>
```

## hashcat - basic md5 (joomla/wordpress $P$) - wordlist with rules
```
hashcat -m 400 <HASH_FILE> <WORDLIST> -r /usr/share/doc/hashcat/rules/best64.rule 
```

## hashcat - kerberos ticket (TGS-REP)
```
hashcat -m 13100 <HASH_FILE> <WORDLIST> --force 
```

## hashcat - kerberos ticket (AS-REP)
```
hashcat -m 18200 <HASH_FILE> <WORDLIST> --force 
```

## hashcat - Domain Cached Credentials (DCC2)
```
hashcat -m 2100 <HASH_FILE> <WORDLIST> --force 
```
## hashcat - LM
```
hashcat -m 3000 <HASH_FILE> <WORDLIST> 
```

## hashcat - bcrypt Blowfish 
```
hashcat -m 3200 <HASH_FILE> <WORDLIST> 
```

## hashcat - NTLM
```
hashcat -m 1000 <HASH_FILE> <WORDLIST> 
```

## hashcat - NTLMv1
```
hashcat -m 5500 <HASH_FILE> <WORDLIST> 
```

## hashcat - NTLMv2
```
hashcat -m 5600 <HASH_FILE> <WORDLIST> 
```

## hashcat - NTLMv2 - Combination attack (ex:passpass,testtest,passtest,etc)
```
hashcat -m 5600 <HASH_FILE> <WORDLIST> --force
```

## hashcat - generate wordlist using rules
```
cat keywords.txt | hashcat -r <RULE_FILE> --stdout > ./<OUTFILE>
```

= wordlist: /usr/share/wordlist/rockyou.txt
= rule_file: /usr/share/doc/hashcat/rules/best64.rule 
= custom_wordlist: wordlist.lst