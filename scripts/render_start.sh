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

echo "==> Migraciones (verbose)..."
python manage.py migrate --noinput --verbosity 2

echo "==> Gunicorn 0.0.0.0:${PORT} workers=${WEB_CONCURRENCY:-1}"
exec python -m gunicorn config.wsgi:application \
  --bind "0.0.0.0:${PORT}" \
  --workers "${WEB_CONCURRENCY:-1}" \
  --capture-output \
  --access-logfile - \
  --error-logfile -
