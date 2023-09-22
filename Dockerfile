FROM python:alpine
WORKDIR /app
COPY *.txt /app/
COPY ./*.py /app/
COPY ./*.html /app/
COPY ./tests/* /app/test/
RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt
EXPOSE 5000
CMD ["python", "/app/MainScore.py"]

