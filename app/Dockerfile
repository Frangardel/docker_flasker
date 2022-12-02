FROM python:3.7
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN mkdir -p schedulin
COPY app.py /schedulin
WORKDIR /schedulin
EXPOSE 5000
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]