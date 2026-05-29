import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_producto_imagen"),
    ]

    operations = [
        # Drop the old transaccion table entirely (schema changed too much to alter in-place)
        migrations.DeleteModel(name="Transaccion"),
        # Recreate with the new schema on the same table name
        migrations.CreateModel(
            name="Transaccion",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "subasta",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="core.subasta",
                    ),
                ),
                (
                    "usuario",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="core.usuario",
                    ),
                ),
                (
                    "monto_final",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=14, null=True
                    ),
                ),
                (
                    "estado",
                    models.CharField(blank=True, default="completada", max_length=50),
                ),
                ("nombre_destinatario", models.CharField(blank=True, max_length=200)),
                ("direccion_envio", models.TextField(blank=True)),
                ("ciudad", models.CharField(blank=True, max_length=100)),
                ("pais", models.CharField(blank=True, max_length=100)),
                ("codigo_postal", models.CharField(blank=True, max_length=20)),
                ("numero_seguimiento", models.CharField(blank=True, max_length=100)),
                ("fecha_creacion", models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                "db_table": "transaccion",
            },
        ),
    ]
