from django.http import HttpResponse
import simplejson
import time
import base64
import os

def login(request):
    '''
    check username and password in the database. If they match, then
    generate a unique token (nonce) and a timestamp.
    '''
    if request.POST:
        username = request.POST["username"]
        password = request.POST["password"]
        
        # ... database check ...
        
        sessionid = base64.b64encode(os.urandom(16))
        timestamp = time.time()
        
        data = simplejson.dumps({"sessionid": sessionid,"timestamp": timestamp})
        return HttpResponse(data, mimetype="application/json")
    else:
        # change to a better error handling mechanism
        return HttpResponse(None, mimetype="application/json")
