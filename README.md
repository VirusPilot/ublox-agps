# ublox AssistNowOnline
This fork is intended to be used in combination with Stratux Europe, particularly with a ublox 9 chipset

# Prepare the script
`apt install python-serial python-requests`

# Run the script via commandline
`python2 u-blox_agps.py`

# Include the script in Stratux Europe
add `python2 u-blox_agps.py` e.g. to /root/stratux-pre-start.sh right after echo powersave ...

# tbd:
- currently eth0 connection for internet access required, should be replaced