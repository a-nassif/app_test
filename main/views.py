import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    j = """
    {
       "version":"2.1",
       "name":"Java Example",
       "model":{
          "codeElement":{
             "codeElement":[
                {
                   "codeRelation":{
                      "_kdm_id":"id.3",
                      "_kdm_type":"code:HasType",
                      "_to":"id.14",
                      "_from":"id.2"
                   }
                }
            ]
        }
        }
    }
    """
    data = json.loads(j)
    return HttpResponse("ok")
