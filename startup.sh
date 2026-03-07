PORT=${PORT:-8000}
echo "================================="
echo "Iniciando FASTAPI"

gunicorn -w 4 -k uvicorn.workers.Uvicornworker main:app --bind 0.0.0.0:$PORT
