from django.shortcuts import redirect, render
from django.views.generic import CreateView
from .models import User, Question, Answer, Etudiant, Professeur, Modul, Filiere, Classe
from .forms import StudentSignUpForm, TeacherSignUpForm, AdminisSignUpForm, LoginForm, QuestionForm, AnswerForm
from django.contrib.auth import login
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .decorators import student_required, teacher_required, adminis_required


class StudentSignUpView(CreateView):
    model = User
    form_class = StudentSignUpForm
    template_name = 'users/student_signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('timetable')



class TeacherSignUpView(CreateView):
    model = User
    form_class = TeacherSignUpForm
    template_name = 'users/teacher_signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'teacher'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('timetable')

class AdminisSignUpView(CreateView):
    model = User
    form_class = AdminisSignUpForm
    template_name = 'users/adminis_signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'adminis'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('timetable2')


class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'users/login.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    def get_success_url(self):
        user = self.request.user
        if user.is_authenticated:
            if user.is_student:
                return reverse('timetable')
            elif user.is_teacher:
                return reverse('timetable')
            elif user.is_adminis:
                return reverse('timetable2')
        else:
            return reverse('login')


@login_required
def timetable(request):
    # questions = Question.objects.all()
    # lessons = Lesson.objects.all()
    context = {
        # 'questions': questions,
        # 'lessons': lessons
    }
    return render(request, 'users/timetable.html', context)

@login_required
def timetable2(request):
    # questions = Question.objects.all()
    # lessons = Lesson.objects.all()
    context = {
        # 'questions': questions,
        # 'lessons': lessons
    }
    return render(request, 'users/timetable2.html', context)

@login_required
@student_required
def student_home(request):
    questions = Question.objects.all()
    context = {
        'questions': questions

    }
    return render(request, 'users/student_home.html', context)

@login_required
@teacher_required
def teacher_home(request):
    questions = Question.objects.filter(teacher=request.user.teacher)
    context = {
        'questions': questions,
    }
    return render(request, 'users/teacher_home.html', context)

@login_required
@teacher_required
def create_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.teacher = request.user.teacher
            question.save()
            return redirect('teacher_home')
    else:
        form = QuestionForm()
    return render(request, 'users/create_question.html', {'form': form})

@login_required
@student_required
def create_answer(request, question_id):
    question = Question.objects.get(id=question_id)
    if Answer.objects.filter(question=question, student=request.user.student).exists():
        return redirect('student_home')
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.student = request.user.student
            answer.question = question
            answer.save()
            return redirect('student_home')
    else:
        form = AnswerForm()
    return render(request, 'users/create_answer.html', {'form': form, 'question': question})

@login_required
@student_required
def student_question_detail(request, question_id):
    question = Question.objects.get(id=question_id)
    if Answer.objects.filter(question=question, student=request.user.student).exists():
        answer = Answer.objects.get(question=question, student=request.user.student)
        answered = True
    else:
        answer = None
        answered = False
    context = {
        'question': question,
        'answer': answer,
        'answered': answered
    }
    return render(request, 'users/student_question_detail.html', context)


@login_required
@teacher_required
def teacher_question_detail(request, question_id):
    question = Question.objects.get(id=question_id)
    if question.teacher != request.user.teacher:
        return redirect('teacher-home')
    answers = Answer.objects.filter(question=question)
    context = {
        'question': question,
        'answers': answers
    }
    return render(request, 'users/teacher_question_detail.html', context)

def listetudiant(request):
    etudiants = Etudiant.objects.all()


    return render(request, "users/listetudiants.html", {"etudiants":etudiants})


# def etudiants(request):
#     etudiants = Etudiant.objects.all()


#     return render(request, "etudiants.html", {"etudiants":etudiants})

# *************************list de professeurs***********************

def listprofesseur(request):
    professeurs = Professeur.objects.all()


    return render(request, "users/listprofesseur.html", {"professeurs":professeurs})

# *************************list de moduls***********************

def listmodul(request):
    moduls = Modul.objects.all()


    return render(request, "users/listmodul.html", {"moduls":moduls})

def listclasse(request):
    classes = Classe.objects.all()


    return render(request, "users/listclasse.html", {"classes":classes})
def listfiliere(request):
    filieres = Filiere.objects.all()


    return render(request, "users/listfiliere.html", {"filieres":filieres})