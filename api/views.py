from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt
from .models import User, Post, HashTag, Comment, Like, Follow
from .decorators import custom_login_required

####################---   ---####################

def home(request):
    posts = Post.objects.all().order_by('-created_at').select_related('user').prefetch_related('hashtags', 'comments', 'likes')
    return render(request, 'home.html', {'posts': posts})

####################---   ---####################

@csrf_exempt
def create_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')

        if all([username, password, name, mobile, email]):
            try:
                User.objects.create(
                    username=username,
                    password=password,
                    name=name,
                    mobile=mobile,
                    email=email
                )
                return render(request, 'profile_created.html')
            except Exception as e:
                return render(request, 'error.html', {'error_message': str(e)})
        else:
            return render(request, 'error.html', {'error_message': 'All fields are required'})
    return render(request, 'create_user.html')

####################---   ---####################

@csrf_exempt
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            try:
                user = User.objects.get(username=username, password=password)
                request.session['user_id'] = user.id
                return render(request, 'login_success.html', {'user': user})
            except User.DoesNotExist:
                return render(request, 'error.html', {'error_message': 'Invalid credentials'})
        else:
            return render(request, 'error.html', {'error_message': 'Username and password are required'})
    return render(request, 'login.html')

####################---   ---####################

@custom_login_required
def search_user(request):
    if request.method == 'GET':
        name_query = request.GET.get('query')
        users = User.objects.filter(name__icontains=name_query) if name_query else []
        return render(request, 'search_user.html', {'users': users, 'query': name_query})
    return HttpResponseNotAllowed(['GET'])

####################---   ---####################

@custom_login_required
def user_home(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
        if request.session.get('user_id') == user.id:
            return render(request, 'user_home.html', {'user': user})
        else:
            return render(request, 'error.html', {'error_message': 'Unauthorized access'}, status=403)
    except User.DoesNotExist:
        return render(request, 'error.html', {'error_message': 'User not found'}, status=404)

####################---   ---####################

@csrf_exempt
@custom_login_required
def logout(request):
    if request.method == 'POST':
        request.session.pop('user_id', None)
        return render(request, 'logout_success.html')
    elif request.method == 'GET':
        return redirect('home')
    return render(request, 'error.html', {'error_message': 'Method not allowed'}, status=405)

####################---   ---####################

@csrf_exempt
@custom_login_required
def update_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if request.method == 'POST':
        user.name = request.POST.get('name', user.name)
        user.mobile = request.POST.get('mobile', user.mobile)
        user.email = request.POST.get('email', user.email)
        
        try:
            user.save()
            return render(request, 'profile_updated.html')
        except Exception as e:
            return render(request, 'error.html', {'error_message': str(e)}, status=400)
    return render(request, 'update_user.html', {'user': user})

####################---   ---####################

@csrf_exempt
@custom_login_required
def delete_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if request.method == 'POST':
        try:
            user.delete()
            request.session.pop('user_id', None)
            return redirect('home')
        except Exception as e:
            return render(request, 'error.html', {'error_message': str(e)})
    return render(request, 'delete_user.html', {'user': user})

####################---   ---####################

@custom_login_required
def show_user_list(request):
    if request.method == 'GET':
        users = User.objects.all()
        return render(request, 'show_user_list.html', {'users': users})
    return HttpResponseNotAllowed(['GET'])

####################---   ---####################

@csrf_exempt
@custom_login_required
def create_post(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        image = request.FILES.get('image')
        hashtags = request.POST.getlist('hashtags')
        user_id = request.session.get('user_id')

        if user_id and text:
            try:
                user = User.objects.get(pk=user_id)
                post = Post.objects.create(user=user, text=text, image=image)
                for tag in hashtags:
                    hashtag, _ = HashTag.objects.get_or_create(name=tag)
                    post.hashtags.add(hashtag)
                return redirect('home')
            except User.DoesNotExist:
                return render(request, 'error.html', {'error': 'User not found'})
            except Exception as e:
                return render(request, 'error.html', {'error': str(e)})
        return render(request, 'error.html', {'error': 'User ID and Text fields are required'})
    return render(request, 'create_post.html')

####################---   ---####################

@custom_login_required
def list_post(request):
    user_id = request.session.get('user_id')
    if user_id:
        discussions = Post.objects.filter(user_id=user_id)
        return render(request, 'list_discussions.html', {'discussions': discussions})
    return render(request, 'error.html', {'error': 'User is not logged in or session expired'}, status=400)

####################---   ---####################

@csrf_exempt
@custom_login_required
def update_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id, user=request.session.get('user_id'))
    if request.method == 'POST':
        post.text = request.POST.get('text', post.text)
        if 'image' in request.FILES:
            post.image = request.FILES['image']
        post.hashtags.clear()
        for tag in request.POST.getlist('hashtags'):
            hashtag, _ = HashTag.objects.get_or_create(name=tag)
            post.hashtags.add(hashtag)
        post.save()
        return redirect('home')
    return render(request, 'update_post.html', {'post': post})

####################---   ---####################

@csrf_exempt
@custom_login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id, user=request.session.get('user_id'))
    if request.method == 'POST':
        try:
            deleted_post = {
                'id': post.id,
                'text': post.text,
                'image': post.image.url if post.image else None,
                'hashtags': [tag.name for tag in post.hashtags.all()]
            }
            post.delete()
            return render(request, 'delete_success.html', {'post': deleted_post})
        except Exception as e:
            return render(request, 'error.html', {'error': str(e)}, status=400)
    return render(request, 'delete_post.html', {'post': post})

####################---   ---####################

@csrf_exempt
@custom_login_required
def list_discussions_by_tags(request):
    if request.method == 'POST':
        tags = request.POST.get('tags', '').split(',')
        tags = [tag.strip() for tag in tags if tag.strip()]
        if tags:
            discussions = Post.objects.filter(hashtags__name__in=tags).distinct()
            discussion_list = [{
                'id': discussion.id,
                'text': discussion.text,
                'image_url': discussion.image.url if discussion.image else None,
                'hashtags': [tag.name for tag in discussion.hashtags.all()],
                'created_at': discussion.created_at,
                'updated_at': discussion.updated_at,
            } for discussion in discussions]
            return render(request, 'list_discussions_by_tags.html', {'discussions': discussion_list, 'tags': tags})
        return render(request, 'list_discussions_by_tags.html', {'error': 'Please provide at least one tag'})
    return render(request, 'list_discussions_by_tags.html')

####################---   ---####################

@csrf_exempt
@custom_login_required
def list_discussions_by_text(request):
    if request.method == 'POST':
        text_query = request.POST.get('text_query')
        if text_query:
            discussions = Post.objects.filter(text__icontains=text_query)
            discussion_list = [{
                'id': discussion.id,
                'text': discussion.text,
                'image_url': discussion.image.url if discussion.image else None,
                'hashtags': [tag.name for tag in discussion.hashtags.all()],
                'created_at': discussion.created_at,
                'updated_at': discussion.updated_at,
            } for discussion in discussions]
            return render(request, 'list_discussions_by_text.html', {'discussions': discussion_list})
        return render(request, 'list_discussions_by_text.html', {'error': 'Please provide a text query'})
    return render(request, 'list_discussions_by_text.html')

####################---   ---####################

@csrf_exempt
@custom_login_required
def like_post(request, post_id):
    if request.method == 'POST':
        post = get_object_or_404(Post, pk=post_id)
        user = get_object_or_404(User, pk=request.session['user_id'])
        
        like, created = Like.objects.get_or_create(user=user, post=post)
        if not created:
            like.delete()
        return redirect('home')
    return HttpResponseNotAllowed(['POST'])

####################---   ---####################

@csrf_exempt
@custom_login_required
def comment_on_post(request, post_id):
    if request.method == 'POST':
        user_id = request.session.get('user_id')
        if user_id:
            user = get_object_or_404(User, pk=user_id)
            post = get_object_or_404(Post, pk=post_id)
            text = request.POST.get('text')
            if text:
                Comment.objects.create(user=user, post=post, text=text)
                return redirect('home')
            else:
                return render(request, 'error.html', {'error': 'Comment text is required'}, status=400)
        return render(request, 'error.html', {'error': 'User is not logged in or session expired'}, status=400)
    return HttpResponseNotAllowed(['POST'])

####################---   ---####################

@csrf_exempt
@custom_login_required
def like_comment(request, comment_id):
    if request.method == 'POST':
        comment = get_object_or_404(Comment, pk=comment_id)
        user = get_object_or_404(User, pk=request.session['user_id'])
        
        like, created = Like.objects.get_or_create(user=user, comment=comment)
        if not created:
            like.delete()
        return redirect('home')
    return HttpResponseNotAllowed(['POST'])

####################---   ---####################

@csrf_exempt
@custom_login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id, user=request.session.get('user_id'))
    if request.method == 'POST':
        try:
            comment.delete()
            return redirect('home')
        except Exception as e:
            return render(request, 'error.html', {'error': str(e)}, status=400)
    return render(request, 'delete_comment.html', {'comment': comment})

####################---   ---####################

@csrf_exempt
@custom_login_required
def update_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id, user=request.session.get('user_id'))
    if request.method == 'POST':
        comment.text = request.POST.get('text', comment.text)
        comment.save()
        return redirect('home')
    return render(request, 'update_comment.html', {'comment': comment})
