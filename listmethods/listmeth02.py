#!/usr/bin/env python3
  
proto = ["ssh", "http", "https"]
protoa = ["ssh", "http", "https"]
print(proto)
print(proto[1])
proto.append("dns")
protoa.append("dns") #this will add d,n, and s
print(proto)

proto2 = [22,80,443,53]
proto.extend(proto2)
print(proto)
protoa.append(proto2)
print(protoa)
protoa.pop([4][0])
print(protoa)
