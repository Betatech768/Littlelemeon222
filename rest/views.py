from django.shortcuts import render, redirect
from .models import Booking, Menu, Category, Take, Contact
from .forms import MenuForm, CategoryForm, TakeForm, BookingForm, CustomUserCreationForm, ContactForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout 


def loginPage(request): 
    
    if request.user.is_authenticated:
        return redirect ('admin')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get ('password')
        try: 
            user = User.objects.get(username=username)
        except: 
            messages.error(request, "User Does Not Exist")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login (request, user)
            return redirect ('admin')
        else:
            messages.error(request, "Incorrect Username or Password")
    context = {}
    return render ( request, 'rest/login.html', context)
        
def logoutUser(request):
    logout(request)
    return redirect('admin')
    
def home (request):
    menu = Menu.objects.all()
       
    if request.method == 'POST':
      email = request.POST['email']
      message = request.POST['message']
      
      
      form = Contact(Email=email, Message=message)
      form.save()
      
    context = { 'menu':menu}
      
    return render (request, 'rest/home.html', context)


# The above is the login_page view 


def adminportal(request):
    if not request.user.is_authenticated:
        return redirect('login_page')
    
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    categories = Category.objects.all()
    menus = Menu.objects.filter(category__name__icontains=q)
    bookings = Booking.objects.all()
    users = User.objects.all()
    takes = Take.objects.all()
    contact = Contact.objects.all()
    context = {
        'categories': categories,
        'menus': menus,
        'bookings': bookings,
        'users': users,
        'takes': takes,
        'contact':contact
    }
    
    return render(request, 'rest/admin.html', context)

# The Above is the book View (searching and filter was also added to it)

# done !!!!!!!!


def menu(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    menu = Menu.objects.filter(category__name__icontains=q)
    category= Category.objects.all()
    context = {'menu': menu, 'category':category}
    return render ( request, 'rest/menu.html', context)

# The above is for the Menu view 

def about (request): 
    return render (request, 'about.html')

#  The dance represents the about page (modify later)


# The below views are views for CRUD operations (Create, Read, Update and Delete)
def createMenu(request):
    form = MenuForm() 
    
    if request.method == 'POST':
        form = MenuForm(request.POST)
        if form.is_valid():
                form.save()
        return redirect ('admin')
    context = {'form':form}
    return render  (request, 'rest/menu_form.html', context)

# Create Operations 


def updateMenu(request, pk):
    menu = Menu.objects.get(id=pk)
    form = MenuForm(instance = menu)
    if request.method == 'POST':
        form = MenuForm(request.POST, instance = menu)
        if form.is_valid():
            form.save()
        return redirect('admin')
    context = {'form': form }
    return render (request, 'rest/menu_form.html', context)

#  Update operations 

def deleteMenu (request, pk):
    menu = Menu.objects.get(id=pk)
    if request.method == 'POST':
        menu.delete()
        return redirect('admin')
    return render (request, 'rest/delete.html', {'obj': menu})


# delete operations 

def createCategory(request):
    form = CategoryForm() 
    
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
                form.save()
        return redirect ('admin')
    context = {'form':form}
    return render  (request, 'rest/category_form.html', context)


def createOrder(request):
    form = TakeForm() 
    
    if request.method == 'POST':
        form = TakeForm(request.POST)
        if form.is_valid():
                form.save()
        return redirect ('admin')
    context = {'form':form}
    return render  (request, 'rest/order_form.html', context)


def Orderpage(request, pk=None):
    odds = Menu.objects.get(name=pk)
    if request.method == 'POST':
        odds = TakeForm(request.POST)
        if odds.is_valid():
            odds.save()
            return redirect ('menu')
    context ={'odds':odds}
    return render (request, 'rest/orderpage.html', context)
        
#  create operations for creating orders 

def Thanks(request):
    return render (request, 'rest/Thanks.html')



def createBooking(request):
    form = BookingForm() 
    
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
                form.save()
        return redirect ('thanks')
    context = {'form':form}
    return render  (request, 'rest/booking_form.html', context)
#  create operations for creating Bookings 

def updateCat(request, pk):
    name = Category.objects.get(id=pk)
    form = CategoryForm(instance = name)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance = name)
        if form.is_valid():
            form.save()
        return redirect('admin')
    context = {'form': form }
    return render (request, 'rest/category_form.html', context)


def Thanks(request):
    return render(request, 'rest/Thanks.html')



# update Operations for deleting Categories 
def deleteCategory (request, pk): 
    cat = Category.objects.get(id=pk)
    if request.method == 'POST':
        cat.delete()
        return redirect ('admin')
    return render (request, 'rest/delete.html', {'obj': cat})
  
# delete Operations for deleting Categories 

def deleteBooking (request, pk): 
    boook = Booking.objects.get(id=pk)
    if request.method == 'POST':
        boook.delete()
        return redirect ('admin')
    return render (request, 'rest/delete.html', {'obj': boook})

# delete Operations for deleting Bookings 

def Booklist(request):
    booking = Booking.objects.all()
    context= {'booking':booking}
    return render (request, 'rest/bookinglist.html', context)

#  Book page view render  

def deleteUser(request, pk): 
    user = User.objects.get(id=pk)
    if request.method == 'POST':
        user.delete()
        return redirect ('admin')
    return render (request, 'rest/delete.html', {'obj': user})

#  User creation View

def createUser(request):
    form = CustomUserCreationForm() 
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            if form.cleaned_data.get('is_superuser'):
                user.is_superuser = True
                user.is_staff = True
            user.save()
            return redirect('admin')
        else:
            messages.error(request, 'An error occurred during registration')

    return render  (request, 'rest/user_creation_form.html', {'form': form})


def OrderList(request, pk):
    order = Take.objects.get(id = pk)
    context= {'order':order}
    return render (request, 'rest/order_list.html', context)


def menuDescription(request, pk):
    menu = Menu.objects.get(id=pk)
    context = { 'menu': menu}
    return render (request, 'rest/menu_description.html', context)


# def contact(request):
#     form = ContactForm()
    
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if  form.is_valid():
#             form.save()
#             return redirect ('home')
#     context = {'form':form}
            
#     return render (request, 'rest/contact.html', context)