# Create your views here.

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .decorators import adminis_required
# from .forms import AdminForm
from .forms import AnnForm
from .forms import ClaForm
from .forms import DepForm
from .forms import EtuForm
from .forms import FilForm
from .forms import ModForm
from .forms import NivForm
from .forms import ProForm
from .models import Administratif
from .models import Annee
from .models import Classe
from .models import Departement
from .models import Etudiant
from .models import Filiere
from .models import Modul
from .models import Niveau
from .models import Professeur


@login_required
def home(request):
    context = {
        'administratifs': Administratif.objects.filter(nom=request.user)
    }
    return render(request, 'home.html', context)


# ******liste***
def listAdministratif(request):
    administratifs = Administratif.objects.all()

    return render(request, "listAdministratifs.html", {"administratifs": administratifs})


# *******createAdministratif**************

# def createAdministratif(request):
# 	form = AdminForm()
# 	if request.method == "POST":
# 		form = AdminForm(request.POST)
# 		if form.is_valid():
# 			form.save()
# 			return redirect("listAdministratifs")
# 	return render(request, "createAdministratif.html", {"administratif_form": form})
#
# # *********update**********************
#
# def update(request, pk):
# 	administratif = Administratif.objects.get(id=pk)
# 	form = AdminForm(instance=administratif)
# 	if request.method == "POST":
# 		form = AdminForm(request.POST, instance=administratif)
# 		if form.is_valid():
# 			form.save()
# 			return redirect("listAdministratifs")
# 	return render(request, "update.html", {"edit_administratif_form": form})
# # ************************************delete******
# def delete(request, pk):
# 	administratif = Administratif.objects.get(id=pk)
# 	if request.method == "POST":
# 		administratif.delete()
# 		return redirect("listAdministratifs")
# 	return render(request,"delete.html",{"administratif":administratif})

# ******liste***
def annAcad(request):
    annAcads = Annee.objects.all()

    return render(request, "listAcads.html", {"annAcads": annAcads})


# # *******createAdministratif**************

def createAnnee(request):
    form = AnnForm()
    if request.method == "POST":
        form = AnnForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listAcads")
    return render(request, "createAnnee.html", {"annAcad_form": form})


# # *********update**********************

def updateAnnee(request, pk):
    annAcad = Annee.objects.get(id=pk)
    form = AnnForm(instance=annAcad)
    if request.method == "POST":
        form = AnnForm(request.POST, instance=annAcad)
        if form.is_valid():
            form.save()
            return redirect("listAcads")
    return render(request, "updateAnnee.html", {"edit_annAcad_form": form})


# ************************************delete******
def deleteAnnee(request, pk):
    annAcad = Annee.objects.get(id=pk)
    if request.method == "POST":
        annAcad.delete()
        return redirect("listAcads")
    return render(request, "deleteAnnee.html", {"annAcad": annAcad})


# *********Departement********
def listDepartement(request):
    departements = Departement.objects.all()

    return render(request, "listDepartements.html", {"departements": departements})


# *******createAdministratif**************

def createDepartement(request):
    form = DepForm()
    if request.method == "POST":
        form = DepForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listDepartements")
    return render(request, "createDepartement.html", {"departement_form": form})


# *********update**********************

def updateDepartement(request, pk):
    departement = Departement.objects.get(id=pk)
    form = DepForm(instance=departement)
    if request.method == "POST":
        form = DepForm(request.POST, instance=departement)
        if form.is_valid():
            form.save()
            return redirect("listDepartements")
    return render(request, "updateDepartement.html", {"edit_departement_form": form})


# ************************************delete******
def deleteDepartement(request, pk):
    departement = Departement.objects.get(id=pk)
    if request.method == "POST":
        departement.delete()
        return redirect("listDepartements")
    return render(request, "deleteDepartement.html", {"departement": departement})


# ******liste***
def listFiliere(request):
    filieres = Filiere.objects.all()

    return render(request, "listFilieres.html", {"filieres": filieres})


# *******createAdministratif**************

def createFiliere(request):
    form = FilForm()
    if request.method == "POST":
        form = FilForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listFilieres")
    return render(request, "createFiliere.html", {"filiere_form": form})


# *********update**********************

def updateFiliere(request, pk):
    filiere = Filiere.objects.get(id=pk)
    form = FilForm(instance=filiere)
    if request.method == "POST":
        form = FilForm(request.POST, instance=filiere)
        if form.is_valid():
            form.save()
            return redirect("listFilieres")
    return render(request, "updateFiliere.html", {"edit_filiere_form": form})


# ************************************delete******
def deleteFiliere(request, pk):
    filiere = Filiere.objects.get(id=pk)
    if request.method == "POST":
        filiere.delete()
        return redirect("listFilieres")
    return render(request, "deleteFiliere.html", {"filiere": filiere})


# ******liste niveau***
def listNiveau(request):
    niveaus = Niveau.objects.all()
    return render(request, "listNiveaus.html", {"niveaus": niveaus})


# *******create Niveau**************

def createNiveau(request):
    form = NivForm()
    if request.method == "POST":
        form = NivForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listNiveaus")
    return render(request, "createNiveau.html", {"niveau_form": form})


# *********update**********************

def updateNiveau(request, pk):
    niveau = Niveau.objects.get(id=pk)
    form = NivForm(instance=niveau)
    if request.method == "POST":
        form = NivForm(request.POST, instance=niveau)
        if form.is_valid():
            form.save()
            return redirect("listNiveaus")
    return render(request, "updateNiveau.html", {"edit_niveau_form": form})


# ************************************delete******
def deleteNiveau(request, pk):
    niveau = Niveau.objects.get(id=pk)
    if request.method == "POST":
        niveau.delete()
        return redirect("listNiveaus")
    return render(request, "deleteNiveau.html", {"niveau": niveau})


# ******liste classe***
def listClasse(request):
    classes = Classe.objects.all()

    return render(request, "listClasses.html", {"classes": classes})


# *******createAdministratif**************

def createClasse(request):
    form = ClaForm()
    if request.method == "POST":
        form = ClaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listClasses")
    return render(request, "createClasse.html", {"classe_form": form})


# *********update**********************

def updateClasse(request, pk):
    classe = Classe.objects.get(id=pk)
    form = ClaForm(instance=classe)
    if request.method == "POST":
        form = ClaForm(request.POST, instance=classe)
        if form.is_valid():
            form.save()
            return redirect("listClasses")
    return render(request, "updateClasse.html", {"edit_classe_form": form})


# ************************************delete******
def deleteClasse(request, pk):
    classe = Classe.objects.get(id=pk)
    if request.method == "POST":
        classe.delete()
        return redirect("listClasses")
    return render(request, "deleteClasse.html", {"classe": classe})


# ******liste***
def listModul(request):
    moduls = Modul.objects.all()

    return render(request, "listModuls.html", {"moduls": moduls})


# *******createAdministratif**************

@login_required
@adminis_required
def createModul(request):
    form = ModForm()
    if request.method == "POST":
        form = ModForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listModuls")
    return render(request, "createModul.html", {"modul_form": form})


# *********update**********************
@login_required
@adminis_required
def updateModul(request, pk):
    modul = Modul.objects.get(id=pk)
    form = ModForm(instance=modul)
    if request.method == "POST":
        form = ModForm(request.POST, instance=modul)
        if form.is_valid():
            form.save()
            return redirect("listModuls")
    return render(request, "updateModul.html", {"edit_modul_form": form})

@login_required
@adminis_required
# ************************************delete******
def deleteModul(request, pk):
    modul = Modul.objects.get(id=pk)
    if request.method == "POST":
        modul.delete()
        return redirect("listModuls")
    return render(request, "deleteModul.html", {"modul": modul})


# ******liste***
def listEtudiant(request):
    etudiants = Etudiant.objects.all()

    return render(request, "listEtudiants.html", {"etudiants": etudiants})


# *******createAdministratif**************

def createEtudiant(request):
    form = EtuForm()
    if request.method == "POST":
        form = EtuForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listEtudiants")
    return render(request, "createEtudiant.html", {"etudiant_form": form})


# *********update**********************

def updateEtudiant(request, pk):
    etudiant = Etudiant.objects.get(id=pk)
    form = EtuForm(instance=etudiant)
    if request.method == "POST":
        form = EtuForm(request.POST, instance=etudiant)
        if form.is_valid():
            form.save()
            return redirect("listEtudiants")
    return render(request, "updateEtudiant.html", {"edit_etudiant_form": form})


# ************************************delete******
def deleteEtudiant(request, pk):
    etudiant = Etudiant.objects.get(id=pk)
    if request.method == "POST":
        etudiant.delete()
        return redirect("listEtudiants")
    return render(request, "deleteEtudiant.html", {"etudiant": etudiant})


# ************************************delete******
def listprofesseurs(request):
    professeurs = Professeur.objects.all()

    return render(request, "listProfesseurs.html", {"professeurs": professeurs})


# *******createAdministratif**************

def createprofesseurs(request):
    form = ProForm()
    if request.method == "POST":
        form = ProForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listprofesseurs")
    return render(request, "createprofesseurs.html", {"professeur_form": form})


# *********update**********************

def updateprofesseurs(request, pk):
    professeur = Professeur.objects.get(id=pk)
    form = ProForm(instance=professeur)
    if request.method == "POST":
        form = ProForm(request.POST, instance=professeur)
        if form.is_valid():
            form.save()
            return redirect("listprofesseurs")
    return render(request, "updateProfesseurs.html", {"edit_professeur_form": form})


# ************************************delete******
def deleteprofesseurs(request, pk):
    professeur = Professeur.objects.get(id=pk)
    if request.method == "POST":
        professeur.delete()
        return redirect("listprofesseurs")
    return render(request, "deleteprofesseurs.html", {"professeur": professeur})

# def index(request):
# 	tasks = Task.objects.all()
# 	return render(request, "index.html", {"tasks": tasks})
# => form = AdminForm()
#	if request.method == "POST":
#	form = AdminForm(request.POST)
#	if form.is_valid():
#		form.save()
#			return redirect("home")
#
# administratifs = Administratif.objects.all()

# from django.shortcuts import render, redirect
# from .models import Task
# from .forms import TaskForm

# Create your views here.
# def home(request):
# 	form = TaskForm()
# 	if request.method == "POST":
# 		form = TaskForm(request.POST)
# 		if form.is_valid():
# 			form.save()
# 			return redirect("home")

# 	tasks = Task.objects.all()
# 	return render(request, "home.html", {"tasks": tasks,"task_form": form})


# def update(request, pk):
# 	task = Task.objects.get(id=pk)
# 	form = TaskForm(instance=task)
# 	if request.method == "POST":
# 		form = TaskForm(request.POST, instance=task)
# 		if form.is_valid():
# 			form.save()
# 			return redirect("home")
# 	return render(request, "update.html", {"edit_task_form": form})


# def delete(request, pk):
# 	task = Task.objects.get(id=pk)
# 	if request.method == "POST":
# 		task.delete()
# 		return redirect("home")
# 	return render(request,"delete.html",{"task":task})
