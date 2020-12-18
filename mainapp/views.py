
from django.contrib.auth import authenticate, login
from django.views.generic import View
from django.shortcuts import render, redirect
from .forms import UserForm
from django.views import generic
from .models import Exam, Questions
import random


def result(request):
    questions = Questions.objects.filter()
    score = 0
    for questions in questions:
        correct_answer = questions.answer
        entered_answer = request.POST.get(str(questions.id))
        if entered_answer == correct_answer:
            score += 1

    context = {'score': score}
    return render(request, 'mainapp/result.html', context)


class SubjectView(generic.ListView):
    template_name = 'mainapp/choice.html'

    def get_queryset(self):
        return Exam.objects.all()


class PhysicsView(generic.ListView):
    template_name = 'mainapp/Physics.html'

    def get_queryset(self):
        return Questions.objects.filter(exam=1)


class MathematicsView(generic.ListView):
    template_name = 'mainapp/Mathematics.html'

    def get_queryset(self):
        return Questions.objects.filter(exam=2)


class ChemistryView(generic.ListView):
    template_name = 'mainapp/Chemistry.html'

    def get_queryset(self):
        return Questions.objects.filter(exam=3)


class EnglishView(generic.ListView):
    template_name = 'mainapp/English.html'

    def get_queryset(self):
        return random.sample(list(Questions.objects.filter(exam=4).values()[:100]), 25)


def physics(request):
    return render(request, 'Physics.html')


def mathematics(request):
    return render(request, 'Mathematics.html')


def chemistry(request):
    return render(request, 'Chemistry.html')


def english(request):
    return render(request, 'English.html')


def choice(request):
    return render(request, 'choice.html')


def home(request):
    return render(request, 'home.html')


class UserFormView(View):
    form_class = UserForm
    template_name = 'registration_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:

                    login(request, user)
                    return redirect('choice')

        return render(request, self.template_name, {'form': form})
