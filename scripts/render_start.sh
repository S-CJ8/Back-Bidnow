#!/usr/bin/env bash
# Arranque en Render (Linux): migraciones visibles en logs y gunicorn vía el mismo Python.
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
export PYTHONUNBUFFERED=1
export DJANGO_SETTINGS_MODULE="${DJANGO_SETTINGS_MODULE:-config.settings}"

if [[ -z "${PORT:-}" ]]; then
  echo "ERROR: falta PORT (Render debe definirla en el servicio web)." >&2
  exit 1
fi

echo "==> Diagnóstico BD (sin contraseña)..."
python - <<'PY'
import os
from urllib.parse import urlparse, unquote

raw = (os.getenv("DATABASE_URL") or "").strip()
if raw:
    if raw.startswith("postgres://"):
        raw = "postgresql://" + raw[len("postgres://") :]
    u = urlparse(raw)
    name = (u.path or "").lstrip("/").split("?")[0]
    print("  DATABASE_URL: host=%r port=%r db=%r user=%r" % (
        u.hostname,
        u.port or 5432,
        name,
        unquote(u.username) if u.username else None,
    ))
else:
    print("  DATABASE_URL no definida; usando DB_*")
    print("  DB_HOST=%r DB_NAME=%r DB_USER=%r" % (
        os.getenv("DB_HOST"),
        os.getenv("DB_NAME"),
        os.getenv("DB_USER"),
    ))
PY

echo "==> Migraciones (verbose + traceback)..."
set +e
python manage.py migrate --noinput --verbosity 2 --traceback 2>&1
MIGRATE_EXIT=$?
set -e
if [[ "${MIGRATE_EXIT}" -ne 0 ]]; then
  echo "==> migrate falló con código ${MIGRATE_EXIT}. Comprobación Django..."
  python manage.py check --database default --traceback 2>&1 || true
  echo "==> Prueba de conexión (ensure_connection)..."
  python - <<'PY' 2>&1 || true
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
import django
django.setup()
from django.db import connection
connection.ensure_connection()
print("  ensure_connection: OK")
PY
  exit "${MIGRATE_EXIT}"
fi

# Admin de Django usa auth_user, no la tabla core.usuario ni el usuario de Postgres.
# Primera vez en producción: BOOTSTRAP_DJANGO_SUPERUSER=1 + variables abajo; luego quita BOOTSTRAP.
if [[ "${BOOTSTRAP_DJANGO_SUPERUSER:-}" == "1" ]]; then
  if [[ -n "${DJANGO_SUPERUSER_USERNAME:-}" && -n "${DJANGO_SUPERUSER_PASSWORD:-}" ]]; then
    echo "==> Superusuario Django (createsuperuser --noinput; ignora error si ya existe)..."
    export DJANGO_SUPERUSER_EMAIL="${DJANGO_SUPERUSER_EMAIL:-admin@example.com}"
    python manage.py createsuperuser --noinput 2>&1 || true
  else
    echo "==> BOOTSTRAP_DJANGO_SUPERUSER=1: defina DJANGO_SUPERUSER_USERNAME y DJANGO_SUPERUSER_PASSWORD" >&2
  fi
fi

echo "==> Gunicorn 0.0.0.0:${PORT} workers=${WEB_CONCURRENCY:-1}"
exec python -m gunicorn config.wsgi:application \
  --bind "0.0.0.0:${PORT}" \
  --workers "${WEB_CONCURRENCY:-1}" \
  --capture-output \
  --access-logfile - \
  --error-logfile -
