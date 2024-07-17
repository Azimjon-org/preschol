from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, ImageField, TextChoices, DateField


class User(AbstractUser):
    class Type(TextChoices):  # Python da constantalar katta harf bilan yoziladi
        ADMIN = 'admin', 'Admin'
        MODERATOR = 'moderator', 'Moderator'
        STUDENT = 'student', 'Stedent'
        TEACHER = 'teacher', 'Teacher'

    class Gender(TextChoices):  # Python da constantalar katta harf bilan yoziladi
        MALE = 'male', 'Male'
        FEMALE = 'female', 'Female'

    image = ImageField(upload_to='users/%Y/%m/%d/', default='users/default.png')
    phone = CharField(max_length=25, blank=True, null=True)
    type = CharField(max_length=15, choices=Type.choices, default=Type.STUDENT)
    gender = CharField(max_length=15, choices=Gender.choices, default=Gender.MALE)
    birth_date = DateField(null=True, blank=True)

"""
<div class="form-group">
    <label>Gender</label>
    <select name="gender" class="form-control">
        {% for value, label in gender_choices %}
            <option value="{{ value }}" {% if student.gender == value %}selected{% endif %}>{{ label }}</option>
        {% endfor %}
    </select>
</div>
"""