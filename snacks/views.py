# Create your views here.
from django.views.generic import ( ListView,
                                   CreateView,
                                   UpdateView,
                                   DeleteView,
                                   TemplateView,
                                   DetailView,
                                   View
                                    )

from django.shortcuts import render

from .models import Snack



class HomeView(TemplateView):
    template_name = "home.html"
    

class SnackListView (ListView):
    template_name = "snacks_list.html"
    model = Snack

class SnackDetailView(DetailView):
    template_name = "snack_detail.html"
    model = Snack


class SnackCreateView(CreateView):
    template_name = "snack_create.html"
    model = Snack
    fields = ["title", "purchaser", "description"]



class SnackUpdateView(UpdateView):
    template_name = "snack_update.html"
    model = Snack
    fields = ["title", "description"]

class SnackDeleteView(DeleteView):
    template_name = "snack_delete.html"
    model = Snack
    success_url ='/'


class MyCustomView(View):

    queryset= Snack.objects.all
    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        data = request.data

        my_Snack={
            "title" : data["title"],
            "description" : data["description"],

        }

        my_object = Snack.objects.create(**Snack)
        my_object.save()

        return render(request, "home.html", {})




    def put(self, request, *args, **kwargs):
        pass


    def delete(self, request, *args, **kwargs):
        pass