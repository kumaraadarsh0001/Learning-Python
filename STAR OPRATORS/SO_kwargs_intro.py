def intro(**kwargs):
    # print(kwargs)
    # print(type(kwargs))
    for k, v in kwargs.items():
        print(f"{k}={v}")
dct={"first_name":'lovely',"middle_name":'boy',"last_name":'badshah'}
#unpaking dictionary from **dictionary name(dct)
intro(**dct) #passing dictonary in kwarsgs
print()
intro(first_name="KUMAR",middle_name="AADARSH",last_name="CHANDRAVANSHI")