from django.shortcuts import render
from MusicClub.models import Root, Profile, Mensaje

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def index(request):
    #posts =  Root.objects.all().order_by("-creado_el")[:5]
    return render(request, "MusicClub/index.html")

def about(request):
    return render(request, "MusicClub/about.html")

class RootList(ListView):
    model = Root
    context_object_name = "roots"

class RootMineList(LoginRequiredMixin, RootList):
    
    def get_queryset(self):
        return Root.objects.filter(propietario=self.request.user.id).all()


class RootDetail(DetailView):
    model = Root
    context_object_name = "root"


class RootUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Root
    success_url = reverse_lazy("root-list")
    fields = '__all__'

    def test_func(self):
        user_id = self.request.user.id
        root_id =  self.kwargs.get("pk")
        return Root.objects.filter(propietario=user_id, id=root_id).exists()


class RootDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Root
    context_object_name = "root"
    success_url = reverse_lazy("root-list")

    def test_func(self):
        user_id = self.request.user.id
        root_id =  self.kwargs.get("pk")
        return Root.objects.filter(propietario=user_id, id=root_id).exists() 


class RootCreate(LoginRequiredMixin, CreateView):
    model = Root
    success_url = reverse_lazy("root-list")
    fields = '__all__'


class RootSearch(ListView):
    model = Root
    context_object_name = "roots"

    def get_queryset(self):
        criterio = self.request.GET.get("criterio")
        result = Root.objects.filter(nombre_interprete=criterio).all()
        return result

class Login(LoginView):
    next_page = reverse_lazy("root-list")

class SignUp(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('root-list')


class Logout(LogoutView):
    template_name = "registration/logout.html"


class ProfileCreate(LoginRequiredMixin, CreateView):
    model = Profile
    success_url = reverse_lazy("root-list")
    fields = ['avatar',]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ProfileUpdate(LoginRequiredMixin, UserPassesTestMixin,  UpdateView):
    model = Profile
    success_url = reverse_lazy("root-list")
    fields = ['avatar',]

    def test_func(self):
        return Profile.objects.filter(user=self.request.user).exists()
    
class MensajeCreate(CreateView):
    model = Mensaje
    success_url = reverse_lazy('mensaje-create')
    fields = '__all__'


class MensajeDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Mensaje
    context_object_name = "mensaje"
    success_url = reverse_lazy("mensaje-list")

    def test_func(self):
        return Mensaje.objects.filter(destinatario=self.request.user).exists()
    

class MensajeList(LoginRequiredMixin, ListView):
    model = Mensaje
    context_object_name = "mensajes"

    def get_queryset(self):
        import pdb; pdb.set_trace
        return Mensaje.objects.filter(destinatario=self.request.user).all()