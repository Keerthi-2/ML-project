from django.http import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render
import joblib

def home(request):
    return render(request,'home.html')

def result(request):
    regressor=joblib.load('finalized_model.sav')
    lis=[]
    lis.append(request.GET['experience'])

    ans=regressor.predict([lis])
    
    context="the predicted salary is "+str(ans)
    print(context)
    return HttpResponse(context)
    return render(request,'result.html',{"ans": context})
     