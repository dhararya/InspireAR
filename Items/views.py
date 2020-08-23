from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from random import randint
# Create your views here.
def index(request):
    tasks = Task.objects.all()

    form = TasksForm()

    if request.method == "POST":
        form = TasksForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {"tasks": tasks, "form": form}

    for task in tasks:
        if task.coin_value == 1:
            task.coin_value = (task.time *task.difficulty)/4
            task.save()

    return render(request, 'Items/list.html', context)

def register(request):
    users = User.objects.all()
    form = UserForm()

    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    ids_ = []
    for user in users:
        ids_.append(int(user.userid))
    new_id = randint(1000000,9999999)
    while int(new_id) in ids_:
        new_id = randint(1000000, 9999999)
    context = {"new_id": new_id, "form": form}

    return render(request, 'Items/register.html', context)

def qrcodes(request, pk):
    user = User.objects.get(id = pk)
    lst = user.links.split(",")
    context = {"user": user, "lst": lst}
    return render(request, 'Items/qrcodes.html', context)

def update_task(request, pk):
    task = Task.objects.get(id=pk)

    form = TasksForm(instance=task)

    if request.method == "POST":
        form = TasksForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            task.coin_value = task.time * task.difficulty
            task.save()
            return redirect('/')

    context = {"form": form}

    return render(request, 'Items/update_task.html', context)

def complete_task (request, pk):
    item = Task.objects.get(id = pk)

    if request.method == "POST":
        item.delete()
        num_obj = Task.objects.all().count()
        if num_obj != 0:
            return redirect('/')
        else:
            return redirect('/claim')

    context = {"item": item}
    return render(request, 'Items/complete.html', context)

def claim(request):
    users = User.objects.all()
    form = UserForm()
    link_str = 'https://i.imgur.com/Nv8Tq2k.png,https://i.imgur.com/chX45xD.png,https://i.imgur.com/23Dgu7N.png,https://i.imgur.com/4rrqbTL.png,https://i.imgur.com/uHWb86j.png,https://i.imgur.com/hCNqIws.png,https://i.imgur.com/LWC4kOa.png,https://i.imgur.com/dommMVM.png,https://i.imgur.com/wpFLIV5.png,https://i.imgur.com/b4uSmAD.png,https://i.imgur.com/7gTGmpJ.png,https://i.imgur.com/K3bQP8Q.png,https://i.imgur.com/BeAFMhx.png'
    links = link_str.split(',')
    index_ = randint(0, len(links)-1)
    link = links[index_]

    Dic = {'https://i.imgur.com/Nv8Tq2k.png': '4ed267d2-0bf7-448f-93d4-b35903e79855',
           'https://i.imgur.com/chX45xD.png': '47d80749-80d7-4b43-8619-4447add5836e',
           'https://i.imgur.com/23Dgu7N.png': '111e2563-af70-4862-bfa3-9d8ca5616951',
           'https://i.imgur.com/4rrqbTL.png': '116dca0f-fadb-47f1-9559-a7f72d5864b0',
           'https://i.imgur.com/uHWb86j.png': 'c20d8537-6ac1-4daa-a919-102461de4d56',
           'https://i.imgur.com/hCNqIws.png': ' 47cf306c-93f6-4a3d-bcbd-2342ecf71550',
           'https://i.imgur.com/LWC4kOa.png': 'a6130142-2441-40e7-80c0-899950a9e4c4',
           'https://i.imgur.com/dommMVM.png': '6369849a-c11d-45b5-b017-a9bc209a66cd',
           'https://i.imgur.com/wpFLIV5.png': 'f34680ab-ee74-44e2-b25a-f3ba0f583366',
           'https://i.imgur.com/b4uSmAD.png': 'fd027824-850d-43c6-9aa5-082ad0ded99f',
           'https://i.imgur.com/7gTGmpJ.png': 'ddd501fa-8f25-4123-a190-51c20ff7acf2',
           'https://i.imgur.com/K3bQP8Q.png': '384cfdd8-f9f2-4ec1-8f1b-13ffcc335779',
           'https://i.imgur.com/BeAFMhx.png': '71eee7d0-f0b4-4059-961f-0afc76db3fb3'}
    id_ = Dic[link]

    ids_ = []
    for user in users:
        ids_.append(int(user.userid))
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user_id = int(form.cleaned_data['userid'])
            if user_id in ids_:
                for user in users:
                    if int(user.userid) == (user_id):
                        if id_ not in user.items:
                            if len(user.items) == 0:
                                user.items = id_
                            else:
                                user.items += ","
                                user.items += id_
                            user.save()
                        return redirect('/adieu')


    context = {'form': form, 'link': link, "id_": id_, "users": users}

    return render(request, 'Items/claim.html', context)

def adieu(request):

    return render(request, 'Items/adieu.html', context = {})

def view_items(request):
    users =User.objects.all()
    form = UserForm()
    ids_ = []
    for user in users:
        ids_.append(int(user.userid))

    Dic = {'https://i.imgur.com/Nv8Tq2k.png': '4ed267d2-0bf7-448f-93d4-b35903e79855',
           'https://i.imgur.com/chX45xD.png': '47d80749-80d7-4b43-8619-4447add5836e',
           'https://i.imgur.com/23Dgu7N.png': '111e2563-af70-4862-bfa3-9d8ca5616951',
           'https://i.imgur.com/4rrqbTL.png': '116dca0f-fadb-47f1-9559-a7f72d5864b0',
           'https://i.imgur.com/uHWb86j.png': 'c20d8537-6ac1-4daa-a919-102461de4d56',
           'https://i.imgur.com/hCNqIws.png': ' 47cf306c-93f6-4a3d-bcbd-2342ecf71550',
           'https://i.imgur.com/LWC4kOa.png': 'a6130142-2441-40e7-80c0-899950a9e4c4',
           'https://i.imgur.com/dommMVM.png': '6369849a-c11d-45b5-b017-a9bc209a66cd',
           'https://i.imgur.com/wpFLIV5.png': 'f34680ab-ee74-44e2-b25a-f3ba0f583366',
           'https://i.imgur.com/b4uSmAD.png': 'fd027824-850d-43c6-9aa5-082ad0ded99f',
           'https://i.imgur.com/7gTGmpJ.png': 'ddd501fa-8f25-4123-a190-51c20ff7acf2',
           'https://i.imgur.com/K3bQP8Q.png': '384cfdd8-f9f2-4ec1-8f1b-13ffcc335779',
           'https://i.imgur.com/BeAFMhx.png': '71eee7d0-f0b4-4059-961f-0afc76db3fb3'}
    inv_Dic = {v: k for k, v in Dic.items()}
    images = ""
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user_id = int(form.cleaned_data['userid'])
            if user_id in ids_:
                for user in users:
                    if int(user.userid) == (user_id):
                        tags_str = user.items
                        tags = tags_str.split(',')
                        for item in tags:
                            if len(images) == 0:
                                images += inv_Dic[item]
                            else:
                                images += ","
                                images += inv_Dic[item]
                        user.links = images
                        user.save()
                        user = User.objects.get(userid=user_id)
                        context = {'form': form, 'user': user, 'users': users}
                        return render(request, 'Items/view_items.html', context)
    context = {'form': form, 'user': user, 'users': users}
    return render(request, 'Items/view_items.html', context)

def ownership(request):
    users = User.objects.all()
    data = ""
    for user in users:
        temp_data = str(user.userid)+":"+user.items+";"
        data += temp_data
    data = data[:-1]

    context = {'data': data}
    return render(request, 'Items/ownership.html', context)