# Generated by Django 3.1.7 on 2021-04-19 08:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('users', '0004_auto_20210418_0854'),
    ]

    operations = [
        migrations.RenameField(
            model_name='apartment',
            old_name='content',
            new_name='about',
        ),
        migrations.RenameField(
            model_name='apartment',
            old_name='datePosted',
            new_name='date_posted',
        ),
        migrations.RenameField(
            model_name='apartment',
            old_name='isRelevant',
            new_name='is_relevant',
        ),
        migrations.RenameField(
            model_name='apartment',
            old_name='numOfRoomates',
            new_name='num_of_roomates',
        ),
        migrations.RenameField(
            model_name='apartment',
            old_name='numOfRooms',
            new_name='num_of_rooms',
        ),
        migrations.RenameField(
            model_name='apartment',
            old_name='rentPricePerMonth',
            new_name='rent',
        ),
        migrations.RenameField(
            model_name='apartment',
            old_name='startDate',
            new_name='start_date',
        ),
        migrations.AddField(
            model_name='apartment',
            name='image_url',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='owner',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='seeker',
            name='about',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True,
                                         help_text='The groups this user belongs to.'
                                         'A user will get all permissions granted to each of their groups.',
                                         related_name='user_set', related_query_name='user', to='auth.Group',
                                         verbose_name='groups'),
        ),
    ]
