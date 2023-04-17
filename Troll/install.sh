#!/usr/bin/sh
git clone https://github.com/mtoyoda/sl.git
cd sl
make
konsole -e ./sl
cd ..
rm -rf sl
exit

