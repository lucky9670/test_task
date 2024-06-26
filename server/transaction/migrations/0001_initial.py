# Generated by Django 4.2.2 on 2024-06-07 18:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PlanFeatures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('type', models.BooleanField(max_length=200)),
                ('Value', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Plans',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70, verbose_name='Subscription Name')),
                ('price', models.FloatField(verbose_name='Price')),
                ('interval', models.CharField(choices=[('Month', 'month'), ('Year', 'year')], default='Month', max_length=20)),
                ('product_id', models.CharField(max_length=200)),
                ('price_id', models.CharField(max_length=200)),
                ('lookup_key', models.CharField(max_length=200)),
                ('currency', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_email', models.EmailField(max_length=254)),
                ('price_id', models.CharField(max_length=500)),
                ('session_id', models.CharField(max_length=500)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now_add=True)),
                ('plans', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='transaction.plans', verbose_name='Plans')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='SubscriptionPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_id', models.CharField(blank=True, max_length=300, null=True)),
                ('amount_submitted', models.IntegerField(blank=True, null=True)),
                ('total_amount', models.IntegerField(blank=True, null=True)),
                ('cancel_url', models.CharField(blank=True, max_length=300, null=True)),
                ('currency', models.CharField(blank=True, max_length=300, null=True)),
                ('customer', models.CharField(blank=True, max_length=300, null=True)),
                ('customer_email', models.CharField(blank=True, max_length=300, null=True)),
                ('customer_phone', models.CharField(blank=True, max_length=300, null=True)),
                ('expiry_date', models.CharField(blank=True, max_length=300, null=True)),
                ('payment_mode', models.CharField(blank=True, max_length=300, null=True)),
                ('payment_status', models.CharField(blank=True, max_length=300, null=True)),
                ('status', models.CharField(blank=True, max_length=300, null=True)),
                ('subscription_id', models.CharField(blank=True, max_length=300, null=True)),
                ('success_url', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubscriptionUsed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_no_of_test', models.IntegerField()),
                ('no_of_test_perform', models.IntegerField(default=0)),
                ('test_duration', models.CharField(max_length=500)),
                ('remaining_test', models.IntegerField()),
                ('no_of_user', models.IntegerField()),
                ('feature', models.ManyToManyField(to='transaction.planfeatures')),
                ('subscription', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='transaction.subscription', verbose_name='subscription')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='PlansFeatureUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ConcurrentHTTP', models.CharField(max_length=150)),
                ('ConcurrentBrowsers', models.CharField(max_length=150)),
                ('HTTPUserHours', models.CharField(max_length=150)),
                ('BrowserUserHours', models.CharField(max_length=150)),
                ('LoadInjectorHours', models.CharField(max_length=150)),
                ('Max_Test_Duration_per_test', models.FloatField()),
                ('UnusedResourceRollover', models.CharField(max_length=150)),
                ('expiry_date', models.CharField(max_length=100)),
                ('status', models.BooleanField(default=True)),
                ('plans', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transaction.plans')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='planfeatures',
            name='plans',
            field=models.ManyToManyField(related_name='features', to='transaction.plans'),
        ),
    ]
