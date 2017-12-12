#!/usr/bin/env python
import csv, sqlite3

con = sqlite3.connect('paldaruo-metadata.db')
con.text_factory=str
cur = con.cursor()

cur.execute("DROP TABLE IF EXISTS metadata")
cur.execute("CREATE TABLE metadata (uid, amlder, byw, iaithgyntaf, plentyndod, rhanbarth, cyd_destun, rhyw, blwyddyngeni);")

with open('/srdk_projects/cy/corpus/audio/paldaruo/metadata.csv','rb') as fin:
	dr=csv.DictReader(fin)
	to_db = [(i['uid'], i['amlder'], i['byw'], i['iaithgyntaf'], i['plentyndod'], i['rhanbarth'], i['cyd_destun'], i['rhyw'], i['blwyddyngeni']) for i in dr]

cur.executemany("INSERT INTO metadata (uid, amlder, byw, iaithgyntaf, plentyndod, rhanbarth, cyd_destun, rhyw, blwyddyngeni) VALUES (?,?,?,?,?,?,?,?,?);", to_db)
con.commit()
con.close()
