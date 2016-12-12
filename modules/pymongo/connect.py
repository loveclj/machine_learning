#!/usr/bin/env python
# coding=utf-8

import  pymongo

mongoHost = "192.168.3.248"
mongoPort = 27017
client    = pymongo.MongoClient(mongoHost, mongoPort)

db     = client["patent"]

user   = "patsnap_r"
passwd = "patsnap123"

db.authenticate(user, passwd)

patentCollection = db["patent"]

print patentCollection.find_one({"kd":"A"})

