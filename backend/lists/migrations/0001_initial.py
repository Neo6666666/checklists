# Generated by Django 2.2.4 on 2019-09-09 10:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import lists.models.attachment


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400, verbose_name='Имя')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'чеклист',
                'verbose_name_plural': 'чеклисты',
            },
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Update date')),
                ('interview_uuid', models.CharField(max_length=36, verbose_name='Interview unique identifier')),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='responses', to='lists.Survey', verbose_name='Survey')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Ответ на чеклист',
                'verbose_name_plural': 'Ответы на чеклисты',
            },
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('date_from', models.DateTimeField(verbose_name='Начало отсчета')),
                ('date_to', models.DateTimeField(verbose_name='Конец отсчета')),
                ('checklists', models.ManyToManyField(to='lists.Survey', verbose_name='Чеклисты')),
            ],
            options={
                'verbose_name': 'Отчет',
                'verbose_name_plural': 'Отчеты',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст')),
                ('order', models.IntegerField(verbose_name='Номер')),
                ('required', models.BooleanField(verbose_name='Обязателен?')),
                ('is_key', models.BooleanField(verbose_name='Ключевой?')),
                ('type', models.CharField(choices=[('textarea', 'Многострочный текст'), ('text', 'Однострочный текст'), ('radio', 'Выбор одного варианта'), ('select', 'Выпадающий список вариантов'), ('select-multiple', 'Выбор нескольких вариантов'), ('integer', 'Целое')], default='textarea', max_length=200, verbose_name='Тип')),
                ('choices', models.TextField(blank=True, help_text="The choices field is only used if the question type\nif the question type is 'radio', 'select', or\n'select multiple' provide a comma-separated list of\noptions for this question .", null=True, verbose_name='Варианты ответа')),
                ('key_choices', models.TextField(blank=True, null=True, verbose_name='Варианты ответа для попадания в отчет')),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='lists.Survey', verbose_name='Survey')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
                'ordering': ('survey', 'order'),
            },
        ),
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to=lists.models.attachment.get_file_path, verbose_name='Файл')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название')),
                ('description', models.CharField(blank=True, max_length=255, verbose_name='Описание')),
                ('object_id', models.PositiveIntegerField(verbose_name='ID')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType', verbose_name='Тип')),
            ],
            options={
                'verbose_name': 'вложение',
                'verbose_name_plural': 'вложения',
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Update date')),
                ('body', models.TextField(blank=True, null=True, verbose_name='Ответ')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='lists.Question', verbose_name='Вопрос')),
                ('response', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='lists.Response', verbose_name='Отчет')),
            ],
        ),
    ]