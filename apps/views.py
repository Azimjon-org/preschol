from django.shortcuts import redirect
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, UpdateView

from apps.models import User


# Create your views here.

class MainTemplateView(TemplateView):
    template_name = 'apps/index.html'


class StudentListView(ListView):
    queryset = User.objects.filter(type=User.Type.STUDENT)
    template_name = 'apps/students/student-list.html'
    context_object_name = 'students'


class StudentDetailDetailView(DetailView):
    queryset = User.objects.filter(type=User.Type.STUDENT)
    template_name = 'apps/students/student-details.html'
    context_object_name = 'student'

    def get_queryset(self):
        return super().get_queryset().filter(type=User.Type.STUDENT)


class StudentEditUpdateView(UpdateView):
    queryset = User.objects.filter(type=User.Type.STUDENT)
    # model = User
    fields = 'first_name', 'last_name', 'username', 'email', 'birth_date', 'gender', 'phone', 'image'
    template_name = 'apps/students/edit-student.html'
    context_object_name = 'student'
    # success_url = 'student_list_page'  # bu qachonki  link orqali pk qirib kelmasa ishlatiladi

    #
    # def get_queryset(self):
    #     return super().get_queryset().filter(type=User.Type.STUDENT)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['genders'] = User.Gender.choices
        return context

    # """ bu link irqali pk kirib kelsa ishlatiladi  eg.(http://localhost:8000/update/2)"""

    def get_success_url(self):
        # variant 1 ->  pk=self.object.id -> database dan olib kelingan userni id olib kelib beradi
        # return reverse('student_update', kwargs={'pk': self.object.id})
        # variant 2 -> bunisi esa link orqali pk ni olob beradi
        return reverse('student_update', kwargs={'pk': self.kwargs.get(self.pk_url_kwarg)})


class StudentDeleteView(View):
    def get(self, request, pk):
        User.objects.filter(type=User.Type.STUDENT, id=pk).delete()
        return redirect('student_list_page')
