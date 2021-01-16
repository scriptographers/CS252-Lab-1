import sqlite3
import csv

con = sqlite3.connect("measurements.sqlite")

cur = con.cursor()
cur.execute("SELECT * FROM reports WHERE sessionid=2")
data = cur.fetchall()
print(len(data[0]))

with open('measurements.csv', 'w') as f:
    writer = csv.writer(f, lineterminator='\n')
    writer.writerow(["_id", "sessionid", "report", "systime", "simstate", "netopname", "netopcode", "roaming",
                     "nettype", "callstate", "datastate", "dataact", "datarx", "datatx", "nstartid", "nstopid",
                     "ngsm", "numts", "nlte", "nrssi", "nregcells", "tech", "mcc", "mnc",
                     "lactac", "nodeid", "cid", "pscpci", "rssi", "rsrq", "rssnr", "slev",
                     "gps", "accur", "lat", "long", "clat", "clong", "band", "arfcn"])
    for tup in data:
        writer.writerow(tup)
