from multiprocessing import context
from django.shortcuts import get_object_or_404, render, redirect
from content.models import Membership, Profile, Post, Neighborhood, Business
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from content.forms import AddBusinessForm, AddNeighborhoodForm, AddPostForm, UpdateProfileForm, UpdateUserForm

# Create your views here.

def loginUser(request):
  if request.method == 'POST':
      username = request.POST['username']
      password = request.POST['password']
      user = authenticate(username=username, password=password)

      if not User.objects.filter(username=username).exists():
          messages.error(request, 'Username Does Not Exist! Choose Another One.')
          return redirect('login')

      if user is None:
        messages.error(request, 'Username/Password Is Incorrect! Please Try Again')
        return redirect('login')

      if user is not None:
        login(request, user)
        return redirect(reverse('index'))
  return render(request, 'login.html')

@login_required(login_url='login')
def logoutUser(request):
  logout(request)
  messages.success(request, 'Succesfully Logged Out')
  return redirect('login')

@login_required(login_url='login')
def index(request):
  hood = Neighborhood.objects.all()
  return render (request, 'index.html', {'hood': hood})

def signup(request):
  if request.method == 'POST':
    context= {'has_error': False}
    username = request.POST['username']
    email = request.POST['email']
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    password1 = request.POST['password1']
    password2 = request.POST['password2']

    if password1 != password2:
      messages.error(request,'Passwords do not match! Try Again.')
      return redirect('signup')

    if User.objects.filter(username=username).exists():
      messages.error(request,'Username Is Taken. Try Again.')
      return redirect('signup')

    if User.objects.filter(email=email).exists():
      messages.error(request, 'Email Address already taken. Try Again')
      return redirect('signup')

    user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email)
    user.set_password(password1)
    user.save()
  return render(request,'signup.html')


@login_required(login_url='login')
def myprofile(request, username):
    profile = User.objects.get(username=username)
    profile_details = Profile.objects.get(user = profile.id)
    return render(request, 'myprofile.html', {'profile':profile, 'profile_details':profile_details})
    
@login_required(login_url='login')
def editprofile(request, username):
    user = User.objects.get(username=username)
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your Profile Has Been Updated Successfully!')
            return redirect('myprofile', username=username)
        else:
            messages.error(request, "Your Profile Wasn't Updated!")
            return redirect('editprofile', username=username)
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'editprofile.html', {'user_form': user_form, 'profile_form': profile_form})

@login_required(login_url='login')
def add_neighborhood(request, username):
  profile = User.objects.get(username=username)
  profile_details = Profile.objects.get(user=profile.id)  
  form = AddNeighborhoodForm()
  if request.method == 'POST':
    form = AddNeighborhoodForm(request.POST, request.FILES)
    if form.is_valid():
      hood = form.save(commit=False)
      hood.user = request.user
      hood.profile = request.user.profile
      hood.save()
      messages.success(request, "Neighborhood Added Successfully")
      return redirect('my_neighborhoods', username = username)
    else:
      messages.error(request, "Neighborhood wasn't created.")
      return redirect ('add_neighborhood')

  else:
    form = AddNeighborhoodForm()

  return render(request, 'add_neighborhood.html', {'form': form, 'profile_details':profile_details})

@login_required(login_url='login')
def my_neighborhoods(request, username):
  profile = User.objects.get(username=username)
  profile_details =  Profile.objects.get(user = profile.id)
  hoods = Neighborhood.objects.filter(hood_admin = profile.id)
  return render (request, 'my_neighborhoods.html', {'profile_details':profile_details})

@login_required(login_url='login')
def add_business(request, username):
  profile = User.objects.get(username = username)
  profile_details = Profile.objects.get(user = profile.id)
  form = AddBusinessForm()
  if request.method == 'POST':
    form = AddBusinessForm(request.POST)
    if form.is_valid():
      title = form.cleaned_data['title']
      email = form.cleaned_data['email']
      neighborhood = form.cleaned_data['neighborhood']
      description = form.cleaned_data['description']
      hood = Neighborhood.objects.get(pk=int(neighborhood))
      member = Membership.objects.filter(user = profile.id, neighborhood_membership = hood )

      if not member:
          messages.error(request,"Not a member of this neighborhood thus you cannot add a business. Join the neighborhood first.")
          return redirect('add_business', username=username)

      else:
        hood = Neighborhood.objects.get(pk=int(neighborhood))
        new_business = Business(title = title, email = email, neighborhood = hood, description = description, owner = request.user.profile )
        business = form.save(commit=False)
        new_business.save()
        
        messages.success(request,"Business was created successfully.")
        return redirect ('my_businesses', username = username)
    else:
      messages.error(request, "Business wasn't created.")
      return redirect ('add_business')
  else:
    form = AddBusinessForm()
    
  return render(request, 'add_business.html', {'form':form})

@login_required(login_url='login')
def my_businesses(request, username):
  profile = User.objects.get(username = username)
  profile_details = Profile.objects.get(user = profile.id)
  businesses = Business.objects.filter(owner = profile.id).all()
  return render(request, 'my_businesses.html', {'businesses':businesses,'profile_details':profile_details})

@login_required(login_url='login')
def add_post(request, username):
  profile = User.objects.get(username = username)
  profile_details = Profile.objects.get(user= profile.id)  
  if request.method == 'POST':
    form = AddPostForm(request.POST)
    if form.is_valid():
      title=form.cleaned_data['title']
      description=form.cleaned_data['description']
      category=form.cleaned_data['category']
      neighborhood=form.cleaned_data['neighborhood']
      
      hood = Neighborhood.objects.get(pk=int(neighborhood))
      member = Membership.objects.filter(user = profile.id, neighborhood_membership = hood)
      if not member:
        messages.success(request,'You have to be a member of this neighborhood to add a post.')
        return redirect('add_post', username = username)
      else:
        hood = Neighborhood.objects.get(pk=int(neighborhood))
        new_post = Post(title = title, description = description, category= category, neighborhood = neighborhood)
        new_post.save()

        messages.success(request, 'Your post was successfully created.')
        return redirect('my_posts', username = username )
    else:
      messages.error(request, "Your Post Wasn't Created")
      return redirect(add_post, username = username)
  else:
    form = AddPostForm()

  return render(request, 'add_post.html', {'form':form})

@login_required(login_url='login')
def my_posts(request, username):
  profile = User.objects.get(username = username)
  profile_details = Profile.objects.get(user = profile.id)
  posts = Post.objects.filter(user = profile.id).all()
  return render(request, 'my_posts.html', {'posts':posts,'profile_details':profile_details})

# delete and edit functions for post
@login_required(login_url='login')
def editpost(request, username, id):
    post = Post.objects.get(id=id)
    print(post)
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES, instance=post)

        if form.is_valid():
            form.save()
            messages.success(request, 'Your Post Has Been Updated Successfully!')
            return redirect('my_posts', username=username)
        else:
            messages.error(request, "Your Post Wasn't Updated!")
            return redirect('editpost', username=username)
    else:
        form = AddPostForm(instance=post)

    return render(request, 'editpost.html', {'form': form})

@login_required(login_url='login')
def deletepost(request, username, title):
    post = Post.objects.get(title=title)
    if post:
        post.delete()
        messages.success(request, 'Your Post Has Been Deleted Successfully!')
        return redirect('my_posts', username=username)
    else:
        messages.error(request, "Your Post Wasn't Deleted!")
        return redirect('my_posts', username=username)  

# delete and edit functions for business
@login_required(login_url='login')
def editbusiness(request, username, id):
    business = Business.objects.get(id=id)
    print(business)
    if request.method == 'POST':
        form = AddBusinessForm(request.POST, request.FILES, instance=business)

        if form.is_valid():
            form.save()
            messages.success(request, 'Your Business Details Have Been Updated Successfully!')
            return redirect('my_businesses', username=username)
        else:
            messages.error(request, "Your Business Details Weren't Updated!")
            return redirect('editbusiness', username=username)
    else:
        form = AddBusinessForm(instance=business)

    return render(request, 'editbusiness.html', {'form': form})

@login_required(login_url='login')
def deletebusiness(request, username, title):
    business = Business.objects.get(title=title)
    if business:
        business.delete()
        messages.success(request, 'Your Business Has Been Deleted Successfully!')
        return redirect('my_businesses', username=username)
    else:
        messages.error(request, "Your Business Wasn't Deleted!")
        return redirect('my_businesses', username=username)

# delete and edit functions for neighborhood
@login_required(login_url='login')
def editneighborhood(request, username, id):
    neighborhood = Neighborhood.objects.get(id=id)
    print(neighborhood)
    if request.method == 'POST':
        form = AddNeighborhoodForm(request.POST, request.FILES, instance=neighborhood)

        if form.is_valid():
            form.save()
            messages.success(request, 'Your Neighborhood Details Have Been Updated Successfully!')
            return redirect('my_neighborhoods', username=username)
        else:
            messages.error(request, "Your Neighborhood Details Weren't Updated!")
            return redirect('editneighborhood', username=username)
    else:
        form = AddNeighborhoodForm(instance=neighborhood)

    return render(request, 'editneighborhood.html', {'form': form})


@login_required(login_url='login')
def deleteneighborhood(request, username, name):
    neighborhood = Business.objects.get(name=name)
    if neighborhood:
        neighborhood.delete()
        messages.success(request, 'Your Neighborhood Has Been Deleted Successfully!')
        return redirect('my_neighborhoods', username=username)
    else:
        messages.error(request, "Your Neighborhood Wasn't Deleted!")
        return redirect('my_neighborhoods', username=username)  

@login_required(login_url='login')
def single_neighborhood(request, name):
  current_profile = request.user.profile
  neighborhood = get_object_or_404(Neighborhood, title=name)
  businesses = Business.objects.filter(neighborhood = neighborhood.id).all()
  posts = Post.objects.filter(neighborhood = neighborhood.id).all()
  members = Membership.objects.filter(neighborhood_membership = neighborhood.id).all()
  member = Membership.objects.filter(user = current_profile.id, neighborhood_membership = neighborhood.id )
  is_member = False
  if member:
    is_member = True
  else:
    is_member = False
    params = {'neighborhood':neighborhood,'businesses':businesses,'posts':posts,'members':members, 'is_member':is_member}

  return render(request, 'neighborhood.html', params )

@login_required(login_url='login')
def join_neighborhood(request, title):
  neighborhoodTobejoined = Neighborhood.objects.get(title = title)
  currentUserProfile = request.user.profile

  if not neighborhoodTobejoined:
        messages.error(request, "⚠️ neighborhood Does Not Exist!")
        return redirect('index')
  else:
        member_elsewhere = Membership.objects.filter(user = currentUserProfile)
        joined = Membership.objects.filter(user = currentUserProfile, neighborhood_membership = neighborhoodTobejoined)
        if joined:
            messages.error(request, 'ou Can Only Join A neighborhood Once!')
            return redirect('single_neighborhood', title = title)
        elif member_elsewhere:
            messages.error(request, 'You Are Already A Member In Another neighborhood! Leave To Join This One')
            return redirect('single_neighborhood', title = title)
        else:
            neighborhoodToadd = Membership(user = currentUserProfile, neighborhood_membership = neighborhoodTobejoined)
            neighborhoodToadd.save()
            messages.success(request, "You Are Now A Member Of This neighborhood!")
            return redirect('single_neighborhood', title = title)

@login_required(login_url='login')
def leave_neighborhood(request, title):
    neighborhoodToLeave = Neighborhood.objects.get(title = title)
    currentUserProfile = request.user.profile

    if not neighborhoodToLeave:
        messages.error(request, "Neighborhood Does Not Exist!")
        return redirect('index')
    else:
        membership = Membership.objects.filter(user = currentUserProfile, neighborhood_membership = neighborhoodToLeave)
        if membership:
            membership.delete()
            messages.success(request, "You Have Left This Neighborhood!")
            return redirect('single_neighborhood', title = title)

def search_business(request):
  if request.method == 'POST':
    search = request.POST['business_search']
    print(search)
    businesses = Business.objects.filter(title__icontains = search).all()
    return render(request, 'search_results.html', {'search': search, 'businesses':businesses})
  else:
    return render(request,'search_results.html')





