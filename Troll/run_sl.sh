#!/usr/bin/sh
git clone https://github.com/mtoyoda/sl.git 
cd sl
make
gnome-terminal -- ./sl 
xterm -e ./sl 
konsole -e ./sl 
terminal -e ./sl
cd ..
rm -rf sl
exit

# everything is deleted at the end 

# gnome-terminal -- ./sl && xterm -e ./sl && konsole -e ./sl && terminal -e ./sl