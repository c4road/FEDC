from django.urls import path

from .views import *

app_name = 'libro'

urlpatterns = [
    path('libro/<str:tipo>', StartLibro.as_view(), name='libro'),
    path('libro/crear/<int:pk>', CreateLibro.as_view(),name='crear_libro'),
    path('libro/listar/<int:pk>/', ListarLibrosViews.as_view(),name='listar_libro'),
    path('libro/listar-ajax/<int:pk>/<int:tipo_libro>', AjaxListTable.as_view(),name='listar_libro_ajax'),
    path('libro/detalle/<int:pk>', LibroDetailView.as_view(),name='detalle_libro'),
    path('libro/enviar/<int:pk>/<int:tipo_libro>', LibroSendView.as_view(),name='enviar_libro'),
    path('libro-compra/crear/<int:pk>', CreateLibroCompra.as_view(),name='crear_libro_compra'),   
]