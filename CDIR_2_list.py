import os;
import re;

CDIR_PATTERN = re.compile("^([0-9]{1,3}\.){3}[0-9]{1,3}(\/([0-9]|[1-2][0-9]|3[0-2]))?$");

f = open('CDIR_list.txt', "r");
line = f.readline();
while line:
  cdir = line.strip();
  if (CDIR_PATTERN.match(cdir)):
    os.system('prips '+cdir);
  line = f.readline();
f.close();
