from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('edificaciones/', views.lista_edificaciones, name='lista_edificaciones'),
    path('edificaciones/agregar/', views.agregar_edificacion, name='agregar_edificacion'),
    path('edificaciones/<int:id>/', views.detalles_edificacion, name='detalles_edificacion'),
    path('edificaciones/editar/<int:id>/', views.editar_edificacion, name='editar_edificacion'),
    path('edificaciones/eliminar/<int:id>/', views.eliminar_edificacion, name='eliminar_edificacion'),


    #urls de tiendas 
    path('agregar/', views.agregar_tienda, name='agregar_tienda'),
    path('editar/<int:tienda_id>/', views.editar_tienda, name='editar_tienda'),
    path('eliminar/<int:tienda_id>/', views.eliminar_tienda, name='eliminar_tienda'),
    path('listado/', views.lista_tiendas, name='lista_tiendas'),  # <-- Aquí está la nueva URL


    # URLs de Propietarios
    path('propietarios/', views.lista_propietarios, name='lista_propietarios'),
    path('propietarios/agregar/', views.agregar_propietario, name='agregar_propietario'),
    path('propietarios/editar/<int:propietario_id>/', views.editar_propietario, name='editar_propietario'),
    path('propietarios/eliminar/<int:propietario_id>/', views.eliminar_propietario, name='eliminar_propietario'),


    #urls de entregas


    path('fechas/', views.lista_fechas_entrega, name='lista_fechas_entrega'),
    path('fechas/agregar/', views.agregar_fecha_entrega, name='agregar_fecha_entrega'),
    path('fechas/editar/<int:fecha_id>/', views.editar_fecha_entrega, name='editar_fecha_entrega'),
    path('fechas/eliminar/<int:fecha_id>/', views.eliminar_fecha_entrega, name='eliminar_fecha_entrega'),

]
