#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os,sys,urllib,json,time
from urllib import *

def banner():
	print("""
 Author : \033[1;32mMr.K3R3H\033[0m
 Tool : \033[1;32mCredit Card Checker And Tracker\033[0m
 Team : \033[1;32mBlackHole Security\033[0m
 Fb : \033[1;34mRonaldo ID\033[0m
 Github : \033[1;36mhttps://github.com/kereh\033[0m
 """)

banner()
target = raw_input("Enter First 6 Digits From Credit Card Number : ")
url = "https://lookup.binlist.net/" +target
operan = urlopen(url).read().decode("utf-8")
fuck = json.loads(operan)
data = fuck

banner()
time.sleep(5)
print
print "###########################"
time.sleep(4)
print
print "\033[1;32m* \033[1;36mScheme :\033[1;32m",str(data["scheme"])
print "\033[1;32m* \033[1;36mBank :\033[1;32m",str(data["bank"])
print "\033[1;32m* \033[1;36mType :\033[1;32m",str(data["type"])
print "\033[1;32m* \033[1;36mBrand :\033[1;32m",str(data["brand"])
print "\033[1;32m* \033[1;36mPrepaid :\033[1;32m",str(data["prepaid"])
print "\033[1;32m* \033[1;36mPrefix :\033[1;32m",(data["number"]["prefix"])
print "\033[1;32m* \033[1;36mLength :\033[1;32m",(data["number"]["length"])
print "\033[1;32m* \033[1;36mCountry :\033[1;32m",(data["country"]["alpha2"])
print "\033[1;32m* \033[1;36mName :\033[1;32m",(data["country"]["name"])
print "\033[1;32m* \033[1;36mNumeric :\033[1;32m",(data["country"]["numeric"])
print "\033[1;32m* \033[1;36mLatitude :\033[1;32m",(data["country"]["latitude"])
print "\033[1;32m* \033[1;36mLongtitude :\033[1;32m",(data["country"]["longitude"])
lat = (data["country"]["latitude"])
lon = (data["country"]["longitude"])
print "\033[1;32m* \033[1;36mLocation :\033[1;32m http://www.google.com/maps/place/%s,%s/@%s,%s,16z\033[0m" %(lat,lon,lat,lon)
print
sys.exit()