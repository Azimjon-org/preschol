from django.urls import path

from apps.views import MainTemplateView, StudentListView, StudentDetailDetailView, StudentEditUpdateView, \
    StudentDeleteView

urlpatterns = [
    path('', MainTemplateView.as_view(), name='main_page'),

    path('student/list', StudentListView.as_view(), name='student_list_page'),
    path('detail/<int:pk>', StudentDetailDetailView.as_view(), name='student_detail'),
    path('update/<int:pk>', StudentEditUpdateView.as_view(), name='student_update'),
    path('delete/<int:pk>', StudentDeleteView.as_view(), name='student_delete')
]
