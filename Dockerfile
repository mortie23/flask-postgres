FROM python:3.8-buster

WORKDIR /
COPY app.py config.py database.py models.py requirements.txt /
COPY templates templates/

# System deps:
RUN pip install -r requirements.txt

EXPOSE 5000
CMD ["gunicorn", "-b", "0.0.0.0:5000", "--workers", "1", "--timeout", "600", "app:app", "--reload"]