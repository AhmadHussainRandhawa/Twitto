from django.shortcuts import render, get_object_or_404, redirect
from .forms import TweetForm, UserRegisterationForm
from .models import Tweet
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

# def tweetPage(request):
#     return render(request, 'tweetPage.html')


def tweetList(request):
    tweets = Tweet.objects.all().select_related('user').order_by('-created_at')
    return render(request, 'tweetList.html', {'tweets': tweets})


@login_required
def tweetCreate(request):
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False) # form.save() here converts the data into Tweet model object.
            tweet.user = request.user
            tweet.save()
            messages.success(request, "✅ Tweet Created Successfully!")
            return redirect('tweetList')
    else:
        form = TweetForm()  # Empty form for GET request.
    
    return render(request, 'tweetForm.html', {'form': form})


@login_required
def tweetEdit(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)

    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            messages.success(request, '✅ Tweet Updated Successfully!')
            return redirect('tweetList')
    else: 
        form = TweetForm(instance=tweet)

    return render(request, 'tweetForm.html', {'form': form})


@login_required
def tweetDelete(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id)
    if tweet.user != request.user:
        return HttpResponseForbidden("⛔ You are not authorized to delete this tweet.")


    if request.method == "POST":
        tweet.delete()
        messages.success(request, '✅ Tweet Deleted Successfully!')
        return redirect('tweetList')
    
    return render(request, 'tweetConfirmDelete.html', {'tweet': tweet})


def contact(request):
    return render(request, 'contact.html')


def register(request):
    if request.method=='POST':
        form = UserRegisterationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('tweetList')

    else:
        form = UserRegisterationForm()

    return render(request, 'registration/register.html', {'form': form})
