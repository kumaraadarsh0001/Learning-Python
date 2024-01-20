import phonenumbers
num="+91 7206137044"
from phonenumbers import geocoder
pepnumber=phonenumbers.parse(num)
location=geocoder.description_for_number(pepnumber,"en")
print(location)
from phonenumbers import carrier
service_pro=phonenumbers.parse(num)
print(carrier.name_for_number(service_pro,"en"))
"""import phonenumbers
from phonenumbers import timezone,geocoder,carrier
number=input("enter your no. with +__:")
phone=phonenumbers.parse(number) #parse give details of phone number
time=timezone.time_zones_for_number(phone)
carier=carrier.name_for_number(phone,"en")
reg=geocoder.description_for_number(phone,"en")
print(phone)
print(time)
print(carier)
print(reg)"""