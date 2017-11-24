
from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from apps.mascota.views import listadousuarios, index, mascota_view, mascota_list, mascota_edit, mascota_delete, \
    MascotaList, Mascota_create, Mascota_update, MascotaDelete

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^nuevo$', login_required(Mascota_create.as_view()), name='mascota_crear'),
    url(r'^listar', login_required(MascotaList.as_view()), name='mascota_listar'),
    url(r'^editar/(?P<pk>\d+)/$', login_required(Mascota_update.as_view()), name='mascota_editar'),
    url(r'^eliminar/(?P<pk>\d+)/$', login_required(MascotaDelete.as_view()), name='mascota_eliminar'),
    url(r'^listado', listadousuarios, name='listadousuarios'),
]
