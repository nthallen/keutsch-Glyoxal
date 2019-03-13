tmcbase = base.tmc
cmdbase = /usr/local/share/huarp/phrtg.cmd
genuibase = glyoxal.genui
swsbase = glyoxal.sws
colbase = SB.cc SB.oui

Module TMbase
Module BCtr rate=1 LV=#
cmdbase = pps.cmd
tmcbase = pps.tmc
tmcbase = pps_time.tmc

SCRIPT = interact
TGTDIR = $(TGTNODE)/home/glyoxal
IGNORE = Makefile

glyoxalcol : -lsubbuspp
glyoxalsrvr : SB.cc SB.oui -lsubbuspp
glyoxaldisp : BCtr_conv.tmc glyoxal.tbl
glyoxalalgo : BCtr_conv.tmc glyoxal.tma glyoxal.sws
doit : glyoxal.doit
