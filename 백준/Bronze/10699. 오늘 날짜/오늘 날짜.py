from time import localtime

tm = localtime()

print("{0}-0{1}-{2}".format(tm.tm_year,tm.tm_mon,tm.tm_mday))
