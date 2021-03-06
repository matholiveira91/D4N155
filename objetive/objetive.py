# -*- coding: utf-8 -*-
#from func_timeout import func_timeout, FunctionTimedOut
import sys
import mechanicalsoup # needed

args = 0
# Connect to target
browser = mechanicalsoup.StatefulBrowser()

try:
    status = browser.open(sys.argv[1]) # func_timeout(15, browser.open, args=sys.argv[1])

    if 'text/' in status.headers['Content-Type']:
        pass
    else:
        exit(2)

except:
    exit(1)

# All functions for get values
def all():
    value = ""
    for p in browser.get_current_page().select('p'):
        value = value + p.text + ' '

    for h1 in browser.get_current_page().select('h1'):
        value = value + h1.text + ' '

    for link in browser.get_current_page().select('a'):
        value = value + link.text + ' '

    if value:
        return value.translate(str.maketrans('', '','–,'))
    else:
        exit(2)

# All texts
print(all())
