#include<stdio.h>
#include<string.h>

void FUN_00400978(char *param_1)

{
  int local_14;
  char *local_10;
  
  local_14 = 0;
  local_10 = param_1;
  while ((*local_10 != 9 && (local_14 < 0x14))) {
    putchar((int)(char)(*local_10 ^ 9));
    local_10 = local_10 + 1;
    local_14 = local_14 + 1;
  }
  putchar(10);
  return;
}

void FUN_0040085d(void)

{
  int iVar1;
  char *__s2;
  char local_48;
  char local_47;
  char local_46;
  char local_45;
  char local_44;
  char local_43;
  char local_42;
  char local_41;
  char local_40;
  char local_3f;
  char local_3e;
  char local_3d;
  char local_3c;
  char local_3b;
  char local_3a;
  char local_39;
  char local_38;
  char local_37;
  char local_36;
  char local_35;
  char local_28 [20];
  int local_14;
  char *local_10;
  
  local_10 = "SuperSeKretKey";
  local_48 = 0x41;
  local_47 = 0x5d;
  local_46 = 0x4b;
  local_45 = 0x72;
  local_44 = 0x3d;
  local_43 = 0x39;
  local_42 = 0x6b;
  local_41 = 0x30;
  local_40 = 0x3d;
  local_3f = 0x30;
  local_3e = 0x6f;
  local_3d = 0x30;
  local_3c = 0x3b;
  local_3b = 0x6b;
  local_3a = 0x31;
  local_39 = 0x3f;
  local_38 = 0x6b;
  local_37 = 0x38;
  local_36 = 0x31;
  local_35 = 0x74;
  FUN_00400978(&local_35);
  /* } */
  return;
}

int main(){
FUN_0040085d();
}
