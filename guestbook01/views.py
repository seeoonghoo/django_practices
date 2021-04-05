from django.http import HttpResponseRedirect
from django.shortcuts import render

from guestbook01 import models


def index(request):
    results = models.findall()
    data = {
        "guestbook_list" : results
    } # 받은 데이터를 emaillist_list 이걸로 보내겠다, 이러면 저거 findall로 만든 것들을 보내고, index.html 에서 표출 가능
    return render(request, 'guestbook01/index.html', data)


def add(request):
    name = request.POST["name"] #form.html 에서 name 으로 지정해서 보낸 데이터를 가져옴. 그니까 가서 잘 확인을 해야함
    password = request.POST["password"]
    message = request.POST["message"]

    models.insert(name, password, message)

    return HttpResponseRedirect("/guestbook01/")

def deleteform(request):

    results = request.GET["no"]
    data = {"no" : results}

    return render(request, 'guestbook01/deleteform.html',data)

def delete(request):

    no = request.POST["no"]
    password = request.POST["password"]

    models.deleteby_no_and_password(no,password)

    return HttpResponseRedirect("/guestbook01")