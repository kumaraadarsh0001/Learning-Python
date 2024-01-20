#Returns the list of available modules.
from email.errors import FirstHeaderLineIsContinuationDefect
import sys
all_module=sys.modules
for module in all_module:    #it will print all module in python sys
    print(module)