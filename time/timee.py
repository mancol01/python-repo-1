import time



#*****************************************************
es=time.time()  #seconds

tmg=time.gmtime()
lt=time.localtime()     # 9 tuple gmt and local 

tim=time.asctime()  #localtime
local_time=time.ctime(es)
#******************************************************

########################
print(f"\nTime epoch seconds:\t{es}\n\n")

######### gmtime
print(f"Using gmtime f(x): {tmg}\n\n")

######### localtime
print(f"Using localtime f(x): {lt}\n")

######################## local time with asctime
print(f"Local time is (using asctime f(x)): {tim}")

########################local time with ctime
print(f"Local time is(using ctime f(x)): {local_time}\n")

######### fetching an item from 9 tuple
print(f"This Hour is : {lt.tm_hour}")

#******************************************************
#inverse of localtime f(x) or return seconds since epoch
# equivalent to time.time()
t=lt
tg=tmg
local_timeE = time.mktime(t)
Gmt_timeE= time.mktime(tg)
print(f"local_timeE is as seconds: {local_timeE}")
print(f"Gmt_timeE is as seconds: {Gmt_timeE}")

#********************************************************
#using strftime to return time with any struct_time tuple
#notes A

strTmTup=lt
timestr1 = time.strftime("%Y-%m-%d, %H:%M:%S",strTmTup)
print("\nusing strftime method: {0}".format(timestr1))

timestr2 = time.strftime("%d-%m-%Y, %H:%M:%S",strTmTup)
print("using strftime method: {0}".format(timestr2))

timestr3 = time.strftime("Day: %a %Y-%m-%d, %H:%M:%S",strTmTup)
print("using strftime method: {0}\n".format(timestr3))

############ strptime inverse of strftime
timestr4 = time.strftime(" %a %Y-%m-%d",strTmTup)
print("using strftime method: {0}".format(timestr4))

time_strng=timestr4

strippingTime=time.strptime(time_strng," %a %Y-%m-%d")
print(strippingTime)





#********************************************************
'''
notes A

%a          Locale’s abbreviated weekday name.

%A          Locale’s full weekday name.

%b          Locale’s abbreviated month name.

%B          Locale’s full month name.

%c          Locale’s appropriate date and time                    representation.

%d          Day of the month as a decimal number [01,31].

%H          Hour (24-hour clock) as a decimal number 
            [00,23].

%I          Hour (12-hour clock) as a decimal number
            [01,12].

%j          Day of the year as a decimal number [001,366].

%m          Month as a decimal number [01,12].

%M          Minute as a decimal number [00,59].

%p          Locale’s equivalent of either AM or PM.

%S          Second as a decimal number [00,61].


%U          Week number of the year 
            (Sunday as the first day of the week) as a
            decimal number [00,53]. All days in a new
            year preceding the first Sunday are
            considered to be in week 0.

%w          Weekday as a decimal number [0(Sunday),6].

%W          Week number of the year 
            (Monday as the first day of the week) as a
            decimal number [00,53]. All days in a new 
            year preceding the first Monday are
            considered to be in week 0.

%x          Locale’s appropriate date representation.

%X          Locale’s appropriate time representation.

%y          Year without century as a decimal number
            [00,99].

%Y          Year with century as a decimal number.

%z          Time zone offset indicating a positive or
            negative time difference from UTC/GMT of
            the form +HHMM or -HHMM, where H represents
            decimal hour digits and M represents decimal
            minute digits [-23:59, +23:59].

%Z          Time zone name (no characters if no time zone
            exists).

%%          A literal '%' character.

'''
#********************************************************


