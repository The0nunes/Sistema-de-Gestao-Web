from django.contrib import admin
from django.urls import path
from sistema_gestao_web import views
from usuarios import views as usuario_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('conta/', usuario_views.novo_usuario, name='novo_usuario'),
    path('login/', auth_views.LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='usuarios/logout.html'), name='logout'),
    path('', views.livros, name='livros'),
    path('novo_livro/',views.criar, name='novo_livro'),
    path('novo_livro/<int:id_livro>', views.editar, name='editar'),
    path('excluir_livro/<int:id_livro>', views.excluir, name='excluir'),
    path('<int:id_livro>', views.detalhe, name='detalhe')
]
