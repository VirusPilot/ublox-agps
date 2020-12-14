# ublox AssistNowOnline
This fork is intended to be used e.g. in combination with Stratux, e.g. with a ublox 9 USB GPS or a ublox 8 based T-Beam

AssistNowOnline significantly speeds up the time to a first fix, particularily when the chipset's battery buffered data is outdated

## Prepare the script
- `apt install python-serial python-requests`
- modify `myToken` accordingly
- modify `comPort` if neccessary for other ublox chipsets

## Run the script via commandline
`python u-blox_agps.py`

## Include the script in Stratux Europe
- add `python u-blox_agps.py` e.g. to /root/stratux-pre-start.sh right after echo powersave ...

## tbd:
- currently eth0 connection for internet access required, should be replaced by EFB internet access
- script should have more fexibility wrt. earlier ublox chipsets
