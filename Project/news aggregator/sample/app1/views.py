from django.contrib import messages
from django.contrib import auth
from django.shortcuts import render, redirect
from django.http import HttpResponse
from app1.models import userdet
from app1.form import userform


def show2(request):
    return render(request, "login.html")


def show3(request):
    return render(request, "home.html")


def show4(request):
    return render(request, "contactus.html")


def show5(request):
    return render(request, "blog.html")


def show6(request):
    return render(request, "aboutus.html")


def show7(request):
    return render(request, "signup.html")
    email = request.GET.get('email')
    email = request.GET.get('psw')


def show8(request):
    return render(request, "hello.html")


def show9(request):
    return render(request, "dashboardM.html")


def sports(request):
    return render(request, "sports.html")


def feedback(request):
    return render(request, "feedback.html", )


def adduser(request):
    # model = userforn
    form_class = userform
    return render(request, "userdet.html", {'form': form_class})


def insuser(request):
    user = userdet.objects.all()
    form = userform(request.POST)
    if form.is_valid():
        form.save()
        pass
    return HttpResponse("Record Inserted !!!")


def showuser(request):
    users = userdet.objects.all()
    return render(request, "showusers.html", {'users': users})


def edit(request, id):
    user = userdet.objects.get(id=id)
    return render(request, 'edit.html', {'user': user})


def update1(request, id):
    user = userdet.objects.get(id=id)
    form = userform(request.POST, instance=user)
    if form.is_valid():
        form.save()
        return redirect("/showusers")
    return render(request, 'edit.html', {'user': user})


def delete1(request, id):
    user = userdet.objects.get(id=id)
    user.delete()
    return redirect("/showusers")


def redirct(param):
    pass


def login2(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        u = auth.authenticate(username=email, password=password)
        if u is None:
            messages.error(request, 'invalid user name and password')
            return redirect('/login')
        else:
            auth.login(request, u)
            request.session['email'] = email
            return redirect('/dashboardM')
    else:
        return render(request, "hello.html")


def logout(request):
    del request.session['email']
    auth.logout(request)
    return redirect('/')


def addemp(request):
    if request.method == "POST":
        form = EmpForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                handle_uploaded_file(request.FILES['file'])
                form.save()
                return HttpResponse("record inserted")
            except:
                pass
        else:
            return redirect('/index')


def addempform(request):
    # model = userforn
    form_class = EmpForm
    return render(request, "addemp.html", {'form': form_class})


import requests
from bs4 import BeautifulSoup


def topnews(request):
    page = requests.get("https://www.divyabhaskar.co.in/")
    soup = BeautifulSoup(page.content, 'html.parser')
    li_1 = soup.find_all("li", {"class", "_24e83f49"})
    news = []
    links = []
    c = 1
    for i in li_1:
        print("=" * 50)
        a_1 = i.find("a")
        links.append("https://www.divyabhaskar.co.in" + a_1.get("href"))
        div_2 = a_1.find("div")
        h3_1 = div_2.find("h3")
        news.append(h3_1.text.strip())
        c += 1
    data = {}
    c = 0
    for i in range(len(links)):
        if i == 7:
            break
        data[links[i]] = news[i]
        i += 1
    data1 = topnews1()
    data2 = images()
    data3 = imageheadlines()
    return render(request, "home.html", {'data': data, 'data1': data1, 'data2': data2, 'data3': data3})

def topnews1():
    page = requests.get("https://www.tv9gujarati.com/")
    soup = BeautifulSoup(page.content, 'html.parser')

    li_8 = soup.find_all("h3", {"class", "h3"})
    news = []
    links = []

    c = 1
    for i in li_8:
        a_8 = i.find("a")
        links.append(a_8.get("href"))
        news.append(a_8.text.strip())
        c += 1

    data8 = {}
    c = 0
    for i in range(len(links)):
        if i == 7:
            break
        data8[links[i]] = news[i]
        i += 1

    return data8

"""
def bnews():
    page = requests.get("https://www.divyabhaskar.co.in/mera-shaher/local/gujarat/vadodara/")
    soup = BeautifulSoup(page.content, 'html.parser')
    li_1 = soup.find_all("li", {"class", "_24e83f49"})
    print(li_1)
    news = []
    links = []
    c = 1
    for i in li_1:
        print("=" * 50)
        a_1 = i.find("a")
        links.append("https://www.divyabhaskar.co.in/mera-shaher" + a_1.get("href"))
        div_2 = a_1.find("div")
        h3_1 = div_2.find("h3")
        news.append(h3_1.text.strip())
        c += 1
    data1 = {}
    c = 0
    for i in range(len(links)):
        if i == 7:
            break
        data1[links[i]] = news[i]
        i += 1
    return data1
"""
def images():
    page = requests.get("http://sandesh.com/")
    soup = BeautifulSoup(page.content, 'html.parser')
    div_1 = soup.find_all("div", {"class", "d-s-top-news"})

    img1 = []
    a1 = []
    for i in div_1:
        a = i.find("a")
        img = i.find("img")
        img1.append(img.get("src"))
        a1.append(a.get("href"))
        print(a)
        print(img)
    print(len(img1))
    print(len(a1))

    data1 = {}
    c = 0
    for i in range(len(a1)):
        if c == 5:
            break;
        data1[a1[i]] = img1[i]
        c = c + 1
    for i in data1:
        print(i)
        # data1=""
    # return render(request, "home.html", {'data': data1})
    return data1

def headlines():
    page = requests.get("http://sandesh.com/")
    soup = BeautifulSoup(page.content, 'html.parser')
    div_1 = soup.find_all("div", {"class", "d-s-top-news"})
    div_2 = soup.find_all("div", {"class", "d-s-top-news-content-p"})

    h1 = []
    c = 0
    for i in div_1:
        if c == 1:
            break
        a = i.find("a")
        h1.append(a.text)
        c += 1
    for i in div_2:
        a = i.find("a")
        h1.append(a.text)
    return h1

def imageheadlines():
    i = images()
    h = headlines()

    data = zip(i.items(), h)
    data = list(data)
    for i in data:
        print(i, "\n\n")

    return data
#############################################################################################################

def sports(request):
    page = requests.get("https://www.divyabhaskar.co.in/sports/")
    soup = BeautifulSoup(page.content, 'html.parser')
    li_2 = soup.find_all("li", {"class", "_24e83f49"})
    news = []
    links = []

    c = 1
    for i in li_2:
        print("=" * 50)
        a_1 = i.find("a")
        links.append("https://www.divyabhaskar.co.in" + a_1.get("href"))
        div_2 = a_1.find("div")
        h3_1 = div_2.find("h3")
        news.append(h3_1.text.strip())
        c += 1

    data3 = {}
    c = 0
    for i in range(len(links)):
        if i == 7:
            break
        data3[links[i]] = news[i]
        i += 1
        data1 = sports_images()
        data = imageheadlines1()
        data4 = sports2()
    # data=""
    return render(request, "sports.html", {'data3': data3, 'data1': data1, 'data': data, 'data4': data4})


def sports_images():
    page = requests.get("http://sandesh.com/category/sports/")
    soup = BeautifulSoup(page.content, 'html.parser')
    div_1 = soup.find_all("div", {"class", "d-s-trending-sec"})

    img1 = []
    a1 = []
    for i in div_1:
        a = i.find("a")
        img = i.find("img")
        img1.append(img.get("src"))
        a1.append(a.get("href"))
        print(a)
        print(img)
    print(len(img1))
    print(len(a1))

    data5 = {}
    c = 0
    for i in range(len(a1)):
        if c == 5:
            break;
        data5[a1[i]] = img1[i]
        c = c + 1
    for i in data5:
        print(i)
        # data1=""
    # return render(request, "home.html", {'data': data1})
    return data5

def headlines1():
    page = requests.get("http://sandesh.com/category/sports/")
    soup = BeautifulSoup(page.content, 'html.parser')
    div_1 = soup.find_all("div", {"class", "d-s-movie-name-date"})
    div_2 = soup.find_all("p", {"class", "d-s-trend-news-content d-s-NSG-regular"})

    h1 = []
    c = 0
    for i in div_2:
        #if c == 1:
        #    break
        a = i.find("a")
        h1.append(a.text)
        c += 1
    for i in div_2:
        a = i.find("a")
        h1.append(a.text)
    return h1


def imageheadlines1():
    i = sports_images()
    h = headlines1()

    data = zip(i.items(), h)
    data = list(data)
    for i in data:
        print(i, "\n\n")
    return data


def sports2():
    page = requests.get("https://www.divyabhaskar.co.in/sports/")
    soup = BeautifulSoup(page.content, 'html.parser')
    li_2 = soup.find_all("li", {"class", "_24e83f49"})
    news = []
    links = []

    c = 1
    for i in li_2:
        print("=" * 50)
        a_1 = i.find("a")
        links.append("https://www.divyabhaskar.co.in" + a_1.get("href"))
        div_2 = a_1.find("div")
        h3_1 = div_2.find("h3")
        news.append(h3_1.text.strip())
        c += 1

    data4 = {}
    c = 0
    for i in range(8, 15):
        data4[links[i]] = news[i]
    return data4

#####################################################################################
def worldnews(request):
    page = requests.get("https://www.divyabhaskar.co.in/international/")
    soup = BeautifulSoup(page.content, 'html.parser')
    li_3 = soup.find_all("li", {"class", "_24e83f49"})
    news = []
    links = []

    c = 1
    for i in li_3:
        print("=" * 50)
        a_1 = i.find("a")
        links.append("https://www.divyabhaskar.co.in" + a_1.get("href"))
        div_2 = a_1.find("div")
        h3_1 = div_2.find("h3")
        news.append(h3_1.text.strip())
        c += 1

    data4 = {}
    c = 0
    for i in range(len(links)):
        if i == 7:
            break
        data4[links[i]] = news[i]
        i += 1
        data1 = worldnews2()
        data5 = world_images()
        data = imageheadlines3()
    return render(request, "worldnews.html", {'data4': data4, 'data1': data1, 'data5': data5 , 'data': data})

def world_images():
    page = requests.get("http://sandesh.com/category/world/")
    soup = BeautifulSoup(page.content, 'html.parser')
    div_1 = soup.find_all("div", {"class", "d-s-trending-sec"})

    img1 = []
    a1 = []
    for i in div_1:
        a = i.find("a")
        img = i.find("img")
        img1.append(img.get("src"))
        a1.append(a.get("href"))
        print(a)
        print(img)
    print(len(img1))
    print(len(a1))

    data5 = {}
    c = 0
    for i in range(len(a1)):
        if c == 5:
            break;
        data5[a1[i]] = img1[i]
        c = c + 1
    for i in data5:
        print(i)
        # data1=""
    # return render(request, "home.html", {'data': data1})
    return data5

def headlines5():
    page = requests.get("http://sandesh.com/category/world/")
    soup = BeautifulSoup(page.content, 'html.parser')
    div_2 = soup.find_all("p", {"class", "d-s-trend-news-content d-s-NSG-regular"})

    h1 = []
    c = 0
    for i in div_2:
        #if c == 1:
         #   break
        a = i.find("a")
        h1.append(a.text)
        c += 1
    for i in div_2:
        a = i.find("a")
        h1.append(a.text)
    return h1


def imageheadlines3():
    i = world_images()
    h = headlines5()

    data = zip(i.items(), h)
    data = list(data)
    for i in data:
        print(i, "\n\n")
    return data



def worldnews2():
    page = requests.get("https://www.divyabhaskar.co.in/international/")
    soup = BeautifulSoup(page.content, 'html.parser')
    li_3 = soup.find_all("li", {"class", "_24e83f49"})
    news = []
    links = []

    c = 1
    for i in li_3:
        print("=" * 50)
        a_1 = i.find("a")
        links.append("https://www.divyabhaskar.co.in" + a_1.get("href"))
        div_2 = a_1.find("div")
        h3_1 = div_2.find("h3")
        news.append(h3_1.text.strip())
        c += 1

    data1 = {}
    c = 0
    for i in range(8, 15):
        data1[links[i]] = news[i]
    return data1

############################################################################
def vadodaranews(request):
    page = requests.get("https://www.tv9gujarati.com/vadodara")
    soup = BeautifulSoup(page.content, 'html.parser')

    li_8 = soup.find_all("h3", {"class", "h3"})
    news = []
    links = []

    c = 1
    for i in li_8:
        a_8 = i.find("a")
        links.append(a_8.get("href"))
        news.append(a_8.text.strip())
        c += 1

    data8 = {}
    c = 0
    for i in range(len(links)):
        if i == 7:
            break
        data8[links[i]] = news[i]
        i += 1
        data1 = barodanews()
    return render(request, "vadodaranews.html", {'data8': data8 ,'data1': data1})

def barodanews():
    page = requests.get("https://www.divyabhaskar.co.in/mera-shaher/local/gujarat/vadodara/")
    soup = BeautifulSoup(page.content, 'html.parser')
    li_1 = soup.find_all("li", {"class", "_24e83f49"})
    print(li_1)
    news = []
    links = []
    c = 1
    for i in li_1:
        print("=" * 50)
        a_1 = i.find("a")
        links.append("https://www.divyabhaskar.co.in/mera-shaher" + a_1.get("href"))
        div_2 = a_1.find("div")
        h3_1 = div_2.find("h3")
        news.append(h3_1.text.strip())
        c += 1
    data1 = {}
    c = 0
    for i in range(len(links)):
        if i == 7:
            break
        data1[links[i]] = news[i]
        i += 1
    return data1

#############################################################################################






import psycopg2 as ps


def ins_feedback(request):
    if request.method == "POST":
        fname = request.POST.get("fname")
        emailid = request.POST.get("emailid")
        contactno = request.POST.get("contactno")
        feedback = request.POST.get("feedback")
        conn = ps.connect(database="dsph", user="postgres", password="devansh", host="localhost", port="5432")
        cur = conn.cursor()
        val = "('" + fname + "','" + emailid + "','" + contactno + "','" + feedback + "', True)"
        cur.execute("insert into app1_feedback(fname,emailid,contactno,feedback, status) values" + val)
        conn.commit()
        return redirect('/')


def covid19(request):
    page = requests.get("https://www.grainmart.in/news/coronavirus-covd-19-live-cases-tracker-john-hopkins/?amp")
    soup = BeautifulSoup(page.content, 'html.parser')
    div_1 = soup.find_all("div", {"class", "sk-st-th"})
    div_2 = soup.find_all("div", {"class", "sk-st-tr"})
    tdata = []
    for i in div_1:
        j = i.find_all("div", {"class", "sk-st-td"})

        for k in j:
            tdata.append(k.text.strip())
    print(tdata)
    th1 = []
    th2 = []
    for i in range(5):
        th1.append(tdata[i])
    for i in range(5, 10):
        th2.append(tdata[i])
    temp = []
    tdata2 = []
    for i in div_2:
        j = i.find_all("div", {"class", "sk-st-td"})
        for k in j:
            temp.append(k.text)
    c = 0
    tmp = []
    for i in range(len(temp)):
        if c % 5 == 0 and c > 0:
            tdata2.append(tmp)
            tmp = []
        tmp.append(temp[i])
        l1 = ['\nMaharashtra\n', '\n1902458\n3106\n', '\n58376\n', '\n49942\n75\n', '\n1794080\n4122\n']
        c1 = 0
    return render(request, "covid-19.html", {'th1': th1, 'th2': th2, 'td1': tdata2})



























