from django.urls import include, path
from . import views

# (. significa que importa views da mesma directoria)

app_name = 'ibuy'
urlpatterns = [
    path('', views.index, name='index'),

    # Login, Conta e Perfil
    # path('loginview', views.loginview, name='loginview'),
    path('loginuser', views.loginuser, name='loginuser'),
    path('logoutview', views.logoutview, name='logoutview'),
    path('criarconta', views.criarconta, name='criarconta'),
    path('minhaconta', views.minhaconta, name='minhaconta'),
    path('perfil/<int:user_id>', views.perfil, name='perfil'),

    # Produtos
    path('criarproduto', views.criarproduto, name='criarproduto'),
    path('meusprodutos', views.meusprodutos, name='meusprodutos'),
    path('carrinho', views.carrinho, name='carrinho'),
    path('produto/<int:produto_id>', views.produto, name='produto'),
    path('produto/<int:produto_id>/apagarproduto', views.apagarproduto, name='apagarproduto'),
    path('produto/<int:produto_id>/like', views.likeProduto, name='like_produto'),
    path('updatecarrinho/<int:produto_id>', views.updatecarrinho, name='updatecarrinho'),
    path('removercarrinho/<int:produto_id>', views.removercarrinho, name='removercarrinho'),
    # path('adicionarcomentario/<int:produto_id>', views.adicionarcomentario, name='adicionarcomentario')
    # Geral
    # path('error', views.error, name='error'),

]
