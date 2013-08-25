from datetime import datetime
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import models as auth_models
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.db.models import Max
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.forms.models import modelformset_factory
from django.http import Http404
from django.core.urlresolvers import reverse

from club import models, forms

@login_required
def logout(request):
    auth_logout(request)
    return render(request, "start.html")

# Home page, display 
#   the name of the group, 
#   the current book, 
#   the next meeting
#   your page 
#   form to update your page
#   form to create a note
@login_required
def club_home(request, club):
    club = models.Club.objects.get(pk=club)
    new_bookform = forms.BookForm()
    ReadingFormSet = modelformset_factory(models.Reading)
    reading_forms = ReadingFormSet(queryset=club.reading_set.all())
    return render(request, 'club_home.html', {'club':club,
                                              'book_form':new_bookform,
                                              'reading_forms':reading_forms})
@login_required
def user_home(request):
    #Gather some info
    club = models.Club.objects.filter(members=request.user)
    if len(club) > 1:
        return render(request, 'error.html',
                      {'message':"Multiple clubs not yet supported"})
    if len(club) == 0:
        return render(request, 'error.html',
                      {'message': "You're not in any clubs yet!"})
    club = club[0]
    reads = models.Reading.objects.filter(club=club)
    comments = models.Comment.objects.filter(club=club, user=request.user)
    CommentFormSet = modelformset_factory(models.Comment, extra=len(reads))
    comment_forms = CommentFormSet(queryset=models.Comment.objects.none())
    return render(request, 'user_home.html', {'club':club,
                                              'reads':reads,
                                              'comment_form':comment_forms,
                                              'comments':comments})

@login_required
def comment(request, club, book):
    '''POST new comments... '''
    CommentFormSet = modelformset_factory(models.Comment)
    if request.method == 'POST':
        comment_formset = CommentFormSet(request.POST)

        club_obj = models.Club.objects.get(id=club)
        book_obj = models.Book.objects.get(id=book)

        if comment_formset.is_valid():
            comments = comment_formset.save(commit=False)
            for c in comments:
                c.club = club_obj
                c.user = request.user
                c.book = book_obj
                c.save()
        else:
            print (comment_formset.errors)

        return HttpResponseRedirect(reverse(user_home))
    else: #GET all available comments for this club/book
        comments = models.Comment.objects.filter(book=book, club=club)
        comments = comments.order_by('-page')
        max_pages = auth_models.User.objects.filter(club=club)
        max_pages = max_pages.annotate(cur_page=Max('comment__page'))
        max_pages = max_pages.filter(comment__book = book)
        comment_formset = CommentFormSet(queryset=models.Comment.objects.none())

        #Figure out what page this user is on
        curr_page = 0
        curr_page_qs = comments.filter(user=request.user)
        if len(curr_page_qs) > 0: curr_page = curr_page_qs[0].page
        return render(request, 'all_comments.html',
                      {'comments':comments,
                       'max_pages':max_pages,
                       'comment_form':comment_formset,
                       'curr_page': curr_page,
                       'book':book,
                       'club': club})

@login_required
def add_book(request, club):
    print("Add_book!")
    if request.method != 'POST':
        raise Http404
    form = forms.BookForm(request.POST)
    if form.is_valid():
        book = form.save()
        club_obj = models.Club.objects.get(pk=club)
        r = models.Reading(club=club_obj, book = book, accepted=False)
        r.save()
        print("saved book")
    else : print("Bad book!")

    return HttpResponseRedirect(reverse(club_home, args=(club,)))

# Create a new user
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()

            #MSB TODO Punt here and just add everyone to club #1
            m1 = models.Membership(user=new_user,
                                   club=models.Club.objects.get(pk=1),
                                   join_date=datetime.today())
            m1.save()
            return HttpResponseRedirect("/club")
    else:
        form = UserCreationForm()
    return render(request, "register.html", { 'form':form,})

