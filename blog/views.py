from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView 
from .models import Post
from django.contrib.auth.models import User

# def home(request):
# 	context = {
# 		'posts': Post.objects.all()
# 	}
# 	return render(request, 'blog/home.html', context)

class PostListView(ListView):		# by default looks for <app>/<model>_<viewtype>.html
	model = Post
	template_name = 'blog/home.html'	# here we have changed default template
	context = {
 		'posts': Post.objects.all()
 	}
	context_object_name = 'posts'	 
	ordering = ['-date_posted']
	paginate_by = 5

class UserPostListView(ListView):		# by default looks for <app>/<model>_<viewtype>.html
	model = Post
	template_name = 'blog/user_posts.html'	# here we have changed default template
	context_object_name = 'posts'	 
	paginate_by = 3

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
	model = Post
	context_object_name = 'post'

class PostCreateView(LoginRequiredMixin, CreateView):	# the first Mixin ensures that a user is logged in
	model = Post
	# context_object_name = 'post'
	fields = ['title', 'content']
	
	def form_valid(self, form):				# to make this form's author, the current user
		form.instance.author = self.request.user
		return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	# context_object_name = 'post'
	fields = ['title', 'content']

	def form_valid(self, form):		
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):					# to check that the current user is same as the blog author
		post = self.get_object()			# if this returns true then only update occurs
		if self.request.user == post.author:
			return True
		return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	context_object_name = 'post'
	success_url = '/'

	def test_func(self):					# to check that the current user is same as the blog author
		post = self.get_object()			# if this returns true then only update occurs
		if self.request.user == post.author:
			return True
		return False


def about(request):
    return render(request, 'blog/about.html', {'title':'About'})

   