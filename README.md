# PEusbMcu
Author: Mandeep
Date: 28 Nov,2017

Current situation with prof einstein to make control work
1. turn off P.E.(prof. Einstein)
2. reset the nodemcu
3. wait 5 sec
4. start P.E.
5. after P.E. tells you "now return to steinomatic to continue" wait a second
6. start scratch program or serial control (calls connect_tcp())

sending node.restart() may restart the nodemcu?

For chinese wemos d1 r2 wifi clone, look for drivers for CH340g chip to enable serial communication on Mac and Windows
Board drivers on Mac
Link? https://github.com/adrianmihalko/ch340g-ch34g-ch34x-mac-os-x-driver

To put lua firmware on d1 r2 board, 
1. get firmware from nodemcu build service https://nodemcu-build.com/
2. get nodemcu-pyflasher https://github.com/marcelstoer/nodemcu-pyflasher
3. (Linux) enable usb serial access permissions on linux for user 
   sudo usermod -a -G dialout $USER
   re-start linux
4. (Linux) if device is at /dev/ttyUSB0 in pyflasher
python ./esptool.py --chip esp8266 --port /dev/ttyUSB0 write_flash -fm dio -ff 20m -fs detect    0x0000 ./nodemcu-master-12-modules-2017-11-24-10-00-45-integer.bin
5. install java runtime and get ESPlorer https://esp8266.ru/esplorer/
6. start ESPlorer, connect and then press rese on board
7. upload lua files to d1 r2 board, first peinstein1.lua and then init.lua
8. call init_wifi("ssid","password") to connect to prof einstein and save config
9. board is ready to use
