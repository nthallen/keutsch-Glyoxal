tmcbase = base.tmc
cmdbase = /usr/local/share/huarp/phrtg.cmd
genuibase = glyoxal.genui
swsbase = glyoxal.sws

Module TMbase
Module BCtr rate=1
tmcbase = pps_time.tmc

SCRIPT = interact
TGTDIR = $(TGTNODE)/home/glyoxal
IGNORE = Makefile

glyoxalcol : -lsubbuspp
glyoxaldisp : BCtr_conv.tmc glyxoal.tbl
glyoxalalgo : BCtr_conv.tmc glyoxal.tma glyoxal.sws
doit : glyoxal.doit
