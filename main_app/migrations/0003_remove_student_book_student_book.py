# Generated by Django 4.0.6 on 2022-08-31 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_book_student_book'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='book',
        ),
        migrations.AddField(
            model_name='student',
            name='book',
            field=models.ManyToManyField(null=True, to='main_app.book'),
        ),
    ]
