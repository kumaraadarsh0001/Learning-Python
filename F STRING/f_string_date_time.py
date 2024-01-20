#date and time 
from datetime import datetime
today=datetime(2022,9,23)
print(f"{today}")
print(f"{today:%d-%B-%Y}")