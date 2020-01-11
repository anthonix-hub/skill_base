from django.shortcuts import render,render_to_response,HttpResponse,Http404,get_object_or_404
from .models import categories,product_details,product_base,comment
from django.urls import reverse_lazy,reverse
from .form import signupForm,commentForm
from django.contrib.auth.models import User
from django.views.generic import CreateView,DetailView,ListView
from django.views import generic
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
# from skillaqui import form

cate = categories.objects.all()
page_comments = product_details.objects.order_by('-timestamp')
prod_dtls = product_details.objects.all()
prod_base = product_base.objects.all()
latest = product_details.objects.order_by('-timestamp')[0:3]

context = { 
        'categories':cate,
        # 'products':prod,
        'prod_details':prod_dtls,
        'product_base':prod_base,
        'latest':latest,
    } 


def index(request):
        
    return render(request,'skillaqui/index.html',context)

def about(request):
    

    return render(request,'skillaqui/about.html',context)

def landing(request):

    return  render(request,'skillaqui/landing.html',context)

def services(request):
    
    return render(request,'skillaqui/services.html',context)   

def course(request):
    db = product_details

    

    return render(request,'skillaqui/course.htm',context)   

def details(request,slug):
    
    prod_details = product_details.objects.get(slug=slug)
    comments = prod_details.comments.filter(active = True)
    # post = get_object_or_404(product_details,slug=slug)
    products = product_details.objects.all()
    latest = product_details.objects.order_by('-timestamp')[0:3]
    new_comment = None

    # commentform = commentForm(request.POST or None )

    if request.method == 'POST':
        comment_form = commentForm(data = request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit = False)
            new_comment.post = prod_details
            new_comment.save()
    else:
        comment_form = commentForm()
    
    contexts = {
        'prod_details':prod_details,
        'latest':latest, 
        'prod':products,
        'commentform':comment_form,
        'page_comments':page_comments,

    }
    return render(request,'skillaqui/details.html',contexts)

class signupview(CreateView):

    form_class = signupForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

def videos(request):
    # vid_details = product_details.objects.get(slug=slug)
    # content={
    #     'vid_details':vid_details
    # }
    return render(request,'skillaqui/videos.html',context)

def commentpage(request,slug):

    post = get_object_or_404(product_details,slug=slug)
    comments = post.comment.filter(active = True)
    new_comment = None
    if request.method =='POST':
        comment_form = commentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=True)
            new_comment.post = post()
            new_comment.save()
    else:
        comment_form = commentForm()

    contexts = {
        'new_comment':new_comment,
        'comment_form':commentForm,
        'page_comments':page_comments,
        'post':post,
    }
    return render(request,'skillaqui/comments.html',contexts)
