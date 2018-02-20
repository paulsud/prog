import pandas as pd
import glob
import urllib.request
import urllib.error
import datetime
import os


def download(ident):
    url = "https://www.star.nesdis.noaa.gov/smcd/emb/vci/VH/get_provinceData.php?country=UKR&provinceID="+str(ident)+"&year1=1981&year2=2018&type=Mean"
    vhi_url = urllib.request.urlopen(url)
    now = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    out = open('vhi_id_%02d.csv' % ident, 'wb')
    out.write(vhi_url.read())
    out.close()
    os.rename('vhi_id_%02d.csv' % ident, 'downloaded_at_' + now + '_vhi_id_%02d.csv' % ident)
    print("VHI is downloaded...")


for ident in range(1, 28):
    download(ident)