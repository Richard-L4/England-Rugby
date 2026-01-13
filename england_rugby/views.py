from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContactForm, RegisterForm, CommentForm
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import CardText, Comment
from django.core.paginator import Paginator


def index(request):
    return render(request, 'index.html', {'active_tab': 'index'})


def tournament(request):
    card_texts = CardText.objects.all().order_by('id')
    paginator = Paginator(card_texts, 2)  # max cards per page
    page_number = request.GET.get('page')  # Get the ? page= value from the url
    page_obj = paginator.get_page(page_number)  # auto handle invalid pages
    return render(request, 'tournament.html', {'active_tab': 'tournament',
                                               'page_obj': page_obj})


def tournament_detail(request, pk):
    card = get_object_or_404(CardText, pk=pk)
    is_saved = False
    if request.user.is_authenticated:
        is_saved = card.saved_by.filter(pk=request.user.pk).exists()

    if request.method == 'POST' and request.user.is_authenticated:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.card = card
            comment.save()
            return redirect('tournament-detail', pk=card.pk)
    else:
        form = CommentForm()

    comments = card.comments.all()

    context = {
        'card': card,
        'comments': comments,
        'form': form,
        'is_saved': is_saved,
        'active_tab': 'tournament-detail'
    }
    return render(request, 'tournament-detail.html', context)


def comment_list(request):
    comments = Comment.objects.all().order_by('-created_at')

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.save()
            return redirect('comment_list')
    else:
        form = CommentForm()
    return redirect(request, 'comment_list.html',
                    {'comments': comments, 'form': form})


@login_required
def edit_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)

    if request.user != comment.user:
        return redirect('card_detail', pk=comment.card.pk)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('tournament-detail', pk=comment.card.pk)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'edit_comment.html', {
        'form': form,
        'comment': comment
    })


@login_required
def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.user != comment.user:
        return redirect('tournament-detail', pk=comment.card.pk)

    if request.method == 'POST':
        card_pk = comment.card.pk
        comment.delete()
        return redirect('tournament-detail', pk=card_pk)
    return render(request, 'delete_comment.html', {'comment': comment})


def about(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been submitted")
            return redirect('about')
    else:
        form = ContactForm()
    return render(request, 'about.html', {'active_tab': 'about', 'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'active_tab': 'login', 'form': form})


@login_required
def user_logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('index')
    return render(request, 'logout.html', {'active_tab': 'logout'})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Account created for {username}! You can log in.'
            )
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html',
                  {'active_tab': 'register', 'form': form})


def confirm_logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('index')
    return render(request, 'confirm-logout.html',
                  {'active_tab': 'confirm-logout'})
