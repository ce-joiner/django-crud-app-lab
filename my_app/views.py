from django.shortcuts import render, redirect
from .models import Tea, Teaware
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import BrewingForm
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
# Import the mixin for class-based views
from django.contrib.auth.mixins import LoginRequiredMixin

# from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')  

# class Tea:
#     def __init__(self, name, description, type, origin, image):
#         self.name = name
#         self.description = description
#         self.type = type
#         self.origin = origin
#         self.image = image
        
# teas = [
#     Tea('2024 Nightlife', 'Heavy, creamy mouthfeel with an airy sweetness and aroma', 'Moonlight white', 'Yunnan, China', 'images/2024Nightlife.png' ),
#     Tea('2016 Poundcake', 'A blend of raw Puer material that has strength, medium light bitterness, and sweetness', 'Raw Puer', 'Yunnan, China', 'images/poundcake.png'),
#     Tea('Duckshit on the Breeze', 'Elegant and wisy take on the classic Duckshit tea', 'Dancong Oolong', 'Guangdong Province, China', 'images/duckshit.png'),
#     Tea('Fruit Bomb Lapsang', 'Heavy, intense fruit fragrances over a full bodied, smoky black tea', 'Lapsang Souchong', 'Fujian Province, China', 'images/FruitBombLapsang.png'),
# ]


@login_required  # only logged-in users can access this view
def tea_index(request):
    teas = Tea.objects.filter(user=request.user)  # Fetch all teas associated with the logged-in user
    return render(request, 'teas/index.html', {'teas': teas})

@login_required
def tea_detail(request, tea_id):
    tea = Tea.objects.get(id=tea_id)  # Fetch the specific tea object by its ID
    teaware = tea.teaware.all()  # Get all teaware associated with this tea
    available_teaware = Teaware.objects.exclude(teas=tea)  # Get teaware NOT associated with this tea
    brewing_form = BrewingForm()  # Create an instance of the BrewingForm
    return render(request, 'teas/details.html', {
        'tea': tea, 
        'teaware': teaware, 
        'available_teaware': available_teaware,  # Add this line
        'brewing_form': brewing_form
    })

class TeaCreate(LoginRequiredMixin, CreateView):
    model = Tea
    fields = [field.name for field in Tea._meta.fields if field.name != 'teaware']  # Exclude 'teaware' field from the form
    # success_url = '/teas/'  # Redirect to the tea index page after creation

    # This inherited method is called when a
    # valid cat form is being submitted
    def form_valid(self, form):
        # Assign the logged in user (self.request.user)
        form.instance.user = self.request.user  # form.instance is the cat
        # Let the CreateView do its job as usual
        return super().form_valid(form)
   
class TeaUpdate(LoginRequiredMixin, UpdateView):
    model = Tea
    fields = '__all__'  # Use all fields from the Tea model

class TeaDelete(LoginRequiredMixin, DeleteView):
    model = Tea
    success_url = '/teas/'  

@login_required  
def add_brewing(request, tea_id):
    form = BrewingForm(request.POST)  # Create a form instance with the submitted data
    if form.is_valid():  # Check if the form is valid
        new_brewing = form.save(commit=False)  # Create a Brewing instance without saving to the database yet
        new_brewing.tea_id = tea_id  # Associate the brewing with the specific tea
        new_brewing.save()  # Save the brewing instance to the database
    return redirect('tea-detail', tea_id=tea_id)  # Redirect to the tea detail page

class TeawareCreate(LoginRequiredMixin, CreateView):
    model = Teaware
    fields = '__all__'  # Use all fields from the Teaware model
    success_url = '/teaware/'  # Redirects to teaware list
    
class TeawareDetail(LoginRequiredMixin, DetailView):
    model = Teaware
   
class TeawareList(LoginRequiredMixin, ListView):
    model = Teaware
   
class TeawareUpdate(LoginRequiredMixin, UpdateView):
    model = Teaware
    fields = '__all__'  

class TeawareDelete(LoginRequiredMixin, DeleteView):
    model = Teaware
    success_url = '/teaware/'  # Redirects to teaware list after deletion

@login_required
def associate_teaware(request, tea_id, teaware_id):
    # Note that you can pass a toy's id instead of the whole object
    Tea.objects.get(id=tea_id).teaware.add(teaware_id)
    return redirect('tea-detail', tea_id=tea_id)  # Redirect to the tea detail page after association

@login_required
def remove_teaware(request, tea_id, teaware_id):
    Tea.objects.get(id=tea_id).teaware.remove(teaware_id)  # Remove the association between the tea and teaware
    return redirect('tea-detail', tea_id=tea_id)  # Redirect to the tea detail page after removal


# This class-based view uses Django's built-in LoginView to handle user authentication.
class Home(LoginView):
    template_name = 'home.html'

def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in
            login(request, user)
            return redirect('tea-index')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)