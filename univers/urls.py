from django.urls import path
from . import views

urlpatterns = [
    path('home2', views.home, name='home'),
    path('listAdministratifs', views.listAdministratif, name='listAdministratifs'),
    # path('createAdministratif', views.createAdministratif, name='createAdministratif'),
    # path('update/<int:pk>/',views.update, name="update"),
    # path('delete/<int:pk>/',views.delete, name="delete"),
    path('listAcads', views.annAcad, name="listAcads"),
    path('createAnnee', views.createAnnee, name="createAnnee"),
    path('updateAnnee/<int:pk>/', views.updateAnnee, name="updateAnnee"),
    path('deleteAnnee/<int:pk>/', views.deleteAnnee, name="deleteAnnee"),
    path('listDepartements', views.listDepartement, name="listDepartements"),
    path('createDepartement', views.createDepartement, name="createDepartement"),
    path('updateDepartement/<int:pk>/', views.updateDepartement, name="updateDepartement"),
    path('deleteDepartement/<int:pk>/', views.deleteDepartement, name="deleteDepartement"),
    path('listFilieres', views.listFiliere, name="listFilieres"),
    path('createFiliere', views.createFiliere, name="createFiliere"),
    path('updateFiliere/<int:pk>/', views.updateFiliere, name="updateFiliere"),
    path('deleteFiliere/<int:pk>/', views.deleteFiliere, name="deleteFiliere"),
    path('listNiveaus', views.listNiveau, name="listNiveaus"),
    path('createNiveau', views.createNiveau, name="createNiveau"),
    path('updateNiveau/<int:pk>/', views.updateNiveau, name="updateNiveau"),
    path('deleteNiveau/<int:pk>/', views.deleteNiveau, name="deleteNiveau"),
    path('listClasses', views.listClasse, name="listClasses"),
    path('createClasse', views.createClasse, name="createClasse"),
    path('updateClasse/<int:pk>/', views.updateClasse, name="updateClasse"),
    path('deleteClase/<int:pk>/', views.deleteClasse, name="deleteClasse"),
    path('listModuls', views.listModul, name="listModuls"),
    path('createModul', views.createModul, name="createModul"),
    path('updateModul/<int:pk>/', views.updateModul, name="updateModul"),
    path('deleteModul/<int:pk>/', views.deleteModul, name="deleteModul"),
    path('listEtudiants', views.listEtudiant, name="listEtudiants"),
    path('createEtudiant', views.createEtudiant, name="createEtudiant"),
    path('updateEtudiant/<int:pk>/', views.updateEtudiant, name="updateEtudiant"),
    path('deleteEtudiant/<int:pk>/', views.deleteEtudiant, name="deleteEtudiant"),
    path('listprofesseurs', views.listprofesseurs, name="listprofesseurs"),
    path('createprofesseurs', views.createprofesseurs, name="createprofesseurs"),
    path('updateprofesseurs/<int:pk>/', views.updateprofesseurs, name="updateprofesseurs"),
    path('deleteprofesseurs/<int:pk>/', views.deleteprofesseurs, name="deleteprofesseurs"),
]

# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.home, name="home"),
#     path('update/<int:pk>/',views.update, name="update"),
#     path('delete/<int:pk>/',views.delete, name="delete"),
# ]