from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from emaillist01 import models

def index(request):
    results = models.findall()
    data = {
        "emaillist_list" : results
    } # 받은 데이터를 emaillist_list 이걸로 보내겠다, 이러면 저거 findall로 만든 것들을 보내고, index.html 에서 표출 가능
    return render(request, 'emaillist01/index.html', data)

def form(request):
    return render(request, 'emaillist01/form.html')

def add(request):
    firstname = request.POST["fn"] #form.html 에서 name 으로 지정해서 보낸 데이터를 가져옴. 그니까 가서 잘 확인을 해야함
    lastname = request.POST["ln"]
    email = request.POST["email"]

    models.insert(firstname, lastname, email)

    return HttpResponseRedirect("/emaillist01") #그냥 http리스폰스는 계속 db에 쳐 들어가니까 그걸 하고 다른 html로 꽂아줘야함. 글작성하면 게시글 리스트 보이는거 알죠?