from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from app1.models import Movies
from app1.forms import Movieform
# from django.db.models import Q

# def home(request):
#     m = Movies.objects.all()
#     return render(request, 'home.html',{'m':m})
class movieslistview(ListView):
    model=Movies
    template_name="home.html"
    context_object_name="m"

# def addfilm(request):
#     if (request.method == "POST"):
#         t = request.POST['t']
#         y = request.POST['y']
#         d = request.POST['d']
#         i = request.FILES['i']
#         m = Movies.objects.create(name=t, year=y, desc=d, img=i)
#         m.save()
#         return home(request)
#     return render(request,'addfilm.html')
class Addfilm(CreateView):
    model=Movies
    template_name="addfilm.html"
    fields = ('name','desc','year','img')
    success_url = reverse_lazy('app1:home')

# def viewdetails(request,p):
#     m = Movies.objects.get(id=p)
#     return render(request,'viewdetails.html',{'m':m})

class detailview(DetailView):
    model=Movies
    template_name="viewdetails.html"
    context_object_name="m"

# def deletemovie(request,p):
#
#     m = Movies.objects.get(id=p)
#     m.delete()
#     return home(request)
class deletemovie(DeleteView):
    model=Movies
    template_name="delete.html"
    success_url=reverse_lazy('app1:home')

# def editmovie(request,p):
#     m = Movies.objects.get(id=p)
#     form = Movieform(instance=m)
#     if (request.method == "POST"):
#         form = Movieform(request.POST,request.FILES,instance=m)
#
#         if form.is_valid():
#             form.save()
#             return home(request)
#     return render(request, 'editmovie.html', {'form': form})

class editmovie(UpdateView):
    model=Movies
    template_name="editmovie.html"
    fields=('name','desc','year','img')
    success_url=reverse_lazy('app1:home')
