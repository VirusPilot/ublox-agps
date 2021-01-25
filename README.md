# ublox AssistNowOnline
This fork is intended to be used e.g. in combination with Stratux, e.g. with a ublox 7/8/9 USB GPS or a ublox 8 based T-Beam

AssistNowOnline significantly speeds up the time to a first fix, particularily when the chipset's battery buffered data is outdated

## Prepare the script
- `sudo apt install python3 python3-pip`
- `sudo pip3 install requests`
- `sudo pip3 install pyserial` (consider adding `--upgrade --force-reinstall` in case of AttributeError: module 'serial' has no attribute 'Serial')
- `sudo pip3 install argparse`

## Run the script via commandline, using your private Token and the intended device, e.g.
- `python3 u-blox_agps.py -t <myToken> -d /dev/ublox8` for GPYes 2.0 or
- `python3 u-blox_agps.py -t <myToken> -d /dev/ttyUSB0` for T-Beam

## Include the script in Stratux Europe
- add `python3 u-blox_agps.py -t ... -d ...` e.g. to /root/stratux-pre-start.sh right after echo powersave or to /etc/rc.local

## tbd:
- currently eth0 connection for internet access required, should be replaced by EFB internet access
