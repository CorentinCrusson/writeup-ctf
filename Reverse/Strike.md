
https://hackropole.fr/fr/challenges/reverse/fcsc2024-reverse-strike/

## Description

L’objectif est d’afficher le flag !

## Write Up

On va prendre un décompiler online, on tombe là dessus :
```c
int main(int param_1,long param_2)

{
  int iVar1;
  size_t sVar2;
  byte local_21;
  uint local_20;
  int local_1c;
  void *local_18;
  uint local_c;
  
  local_18 = (void *)0x0;
  local_1c = -1;
  if (param_1 == 2) {
    sVar2 = strlen(*(char **)(param_2 + 8));
    local_20 = (uint)sVar2;
    if (((sVar2 & 1) == 0) && (local_18 = malloc(sVar2 & 0xffffffff), local_18 != (void *)0x0)) {
      for (local_c = 0; local_c < local_20; local_c = local_c + 2) {
        iVar1 = a(*(undefined *)((ulong)local_c + *(long *)(param_2 + 8)),
                  *(undefined *)(*(long *)(param_2 + 8) + (ulong)(local_c + 1)),&local_21);
        if ((iVar1 != 0) || (0x22 < local_21)) goto LAB_0010145a;
        *(char *)((ulong)(local_c >> 1) + (long)local_18) = charset[(local_21 + local_c) % 0x23];
      }
      if ((local_20 - 0xa2 < 2) &&
         (iVar1 = memcmp(local_18,to_check,(ulong)(local_20 >> 1)), iVar1 == 0)) {
        local_1c = 0;
      }
    }
  }
LAB_0010145a:
  if (local_18 != (void *)0x0) {
    free(local_18);
  }
  if (local_1c == 0) {
    printf(&DAT_001021d0,*(undefined8 *)(param_2 + 8));
  }
  else {
    puts("[-] Error ...");
  }
  return local_1c;
}

undefined8 a(undefined param_1,undefined param_2,byte *param_3)

{
  byte local_a;
  char local_9;
  
  switch(param_1) {
  case 0x30:
    local_9 = '\0';
    break;
  case 0x31:
    local_9 = '\x01';
    break;
  case 0x32:
    local_9 = '\x02';
    break;
  case 0x33:
    local_9 = '\x03';
    break;
  case 0x34:
    local_9 = '\x04';
    break;
  case 0x35:
    local_9 = '\x05';
    break;
  case 0x36:
    local_9 = '\x06';
    break;
  case 0x37:
    local_9 = '\a';
    break;
  case 0x38:
    local_9 = '\b';
    break;
  case 0x39:
    local_9 = '\t';
    break;
  default:
    return 0xffffffff;
  case 0x61:
    local_9 = '\n';
    break;
  case 0x62:
    local_9 = '\v';
    break;
  case 99:
    local_9 = '\f';
    break;
  case 100:
    local_9 = '\r';
    break;
  case 0x65:
    local_9 = '\x0e';
    break;
  case 0x66:
    local_9 = '\x0f';
  }
  switch(param_2) {
  case 0x30:
    local_a = 0;
    break;
  case 0x31:
    local_a = 1;
    break;
  case 0x32:
    local_a = 2;
    break;
  case 0x33:
    local_a = 3;
    break;
  case 0x34:
    local_a = 4;
    break;
  case 0x35:
    local_a = 5;
    break;
  case 0x36:
    local_a = 6;
    break;
  case 0x37:
    local_a = 7;
    break;
  case 0x38:
    local_a = 8;
    break;
  case 0x39:
    local_a = 9;
    break;
  default:
    return 0xffffffff;
  case 0x61:
    local_a = 10;
    break;
  case 0x62:
    local_a = 0xb;
    break;
  case 99:
    local_a = 0xc;
    break;
  case 100:
    local_a = 0xd;
    break;
  case 0x65:
    local_a = 0xe;
    break;
  case 0x66:
    local_a = 0xf;
  }
  *param_3 = local_a | local_9 << 4;
  return 0;
}

```
On comparent avec d'autres compiler, on se rend compte que la fonction main prend des arguments (arg, **argc)

et que la fonction to_check contient " congratulations! this is a strike :-) you should now see the flag printed ... #"