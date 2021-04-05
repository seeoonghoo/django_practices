from django.http import HttpResponse
from django.shortcuts import render


def main(request):
    return render(request, 'helloworld/main.html')

def hello1(request):
    name = request.GET["name"]
    return HttpResponse(f'<h1>Hello {name}</h1><a href="/">메인으로가기</a>', content_type='text/html; charset=utf-8')

def tags(request):
    return render(request, 'helloworld/tags.html')

def form(request):
    return render(request, 'helloworld/form.html')

def join(request):
    email = request.POST['email'] #이러면 딕셔너리를 만들어서 '' 안에 있는걸 키로 밸류랑 같이 가져와서 저장
    password = request.POST['password'] # 얘는 form 에서 보낸 password를 가져와서 저장. 위에는 email 이 되겠죠
    # 데이터를 넘기는건 이렇게 넘기면 된다
    # GET/ join? email=seongho&password=123 HTTP/1.0     이렇게 url에 나타나게 보냄
    # POST /join HTTP/1.0      /////            email=seongho&password=123 를 바디로 보냄. 얘는 url에 나타나지 x
    gender = request.POST['gender']
    hobbies = request.POST.getlist("hobbies") # 좀 여러개 가져오니까 list로 가져옴
    description = request.POST["desc"] # 얘는 쓰는대로 넘어옴
    print(email, password, gender, hobbies, description)
    return HttpResponse('ok', content_type='text/plain; charset=utf-8')