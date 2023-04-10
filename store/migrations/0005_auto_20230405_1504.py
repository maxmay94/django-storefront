# Generated by Django 4.2 on 2023-04-05 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0004_address_zip_code"),
    ]

    operations = [
        migrations.RunSQL("""
            INSERT INTO store_collection (title)
            VALUES ('collection1')
        """, """
            DELETE FROM store_collection
            WHERE title = 'collection1'
        """)
    ]