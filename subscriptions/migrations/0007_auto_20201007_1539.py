# Generated by Django 3.1.1 on 2020-10-07 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0006_add_slugs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plancost',
            name='plan',
        ),
        migrations.RemoveField(
            model_name='usersubscription',
            name='subscription',
        ),
        migrations.AddField(
            model_name='usersubscription',
            name='plan_cost',
            field=models.ForeignKey(help_text='the plan costs and billing frequency for this user subscription', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subscriptions', to='subscriptions.plancost'),
        ),
        migrations.AddField(
            model_name='usersubscription',
            name='subscription_plan',
            field=models.ForeignKey(help_text='the subscription plan for this user subscription', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subscriptions', to='subscriptions.subscriptionplan'),
        ),
        migrations.AlterField(
            model_name='planlist',
            name='footer',
            field=models.TextField(blank=True, help_text='footer text to display on the subscription plan list page', null=True),
        ),
        migrations.CreateModel(
            name='PlanCostLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subscriptions.plancost')),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subscriptions.subscriptionplan')),
            ],
        ),
        migrations.AddField(
            model_name='plancost',
            name='plans',
            field=models.ManyToManyField(blank=True, help_text='the subscription plan for these cost details', null=True, related_name='costs', through='subscriptions.PlanCostLink', to='subscriptions.SubscriptionPlan'),
        ),
    ]