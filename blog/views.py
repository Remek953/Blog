from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post, Comment
from .forms import EmailPostForm, CommentForm
from taggit.models import Tag
from django.db.models import Count

# Create your views here.

def post_list(request, tag_slug=None):
	object_list = Post.published.all()
	tag = None

	if tag_slug:
		tag = get_object_or_404(Tag, slug=tag_slug)
		object_list = object_list.filter(tags__in=[tag])
	paginator = Paginator(object_list, 4)
	page = request.GET.get('page', 1)
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)
		
	context = {'page':page, 'posts':posts, 'tag':tag}
	return render(request, 'blog/post/list.html', context)


def post_detail(request, year, month, day, post,):
	post = get_object_or_404(Post, slug=post,
								   status='published',
								   publish__year=year,
								   publish__month=month,
								   publish__day=day)
	comments = post.comments.filter(active=True)

	if request.method == 'POST':
		comment_form = CommentForm(data=request.POST)
		new_comment = comment_form.save(commit=False)
		new_comment.post = post
		new_comment.save()
		comment_form = CommentForm()
	else:
		comment_form = CommentForm()

	post_tags_ids = post.tags.values_list('id', flat=True)
	similar_posts = Post.published.filter(tags__in=post_tags_ids).exclude(id=post.id)
	similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags','-publish')[:4]

	context = {'post':post, 'comments':comments, 'comment_form': comment_form, 'similar_posts':similar_posts,}
	return render(request, 'blog/post/detail.html', context)


