from django.urls import path
from .views import( 
	PostListView, 
	PostDetailView, 
	PostCreateView, 
	PostUpdateView, 
	PostDeleteView,
	UserPostListView
)
from .import views

urlpatterns = [
    path('', PostListView.as_view(), name = 'blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name = 'user-blog'),
    path('blog/<int:pk>/', PostDetailView.as_view(), name = 'blog-detail'),
    path('blog/new/', PostCreateView.as_view(), name = 'blog-create'),   			# | both will look for blog/post_form.html by default
    path('blog/<int:pk>/update/', PostUpdateView.as_view(), name = 'blog-update'),	# |
    path('blog/<int:pk>/delete/', PostDeleteView.as_view(), name = 'blog-delete'),	# this will look for blog/post_confirm_delete.html
    path('about/', views.about, name = 'blog-about'),
]