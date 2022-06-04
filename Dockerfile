FROM python:3.10.2

WORKDIR /app

ADD main.py .

RUN python -m pip install --upgrade pip
RUN pip install wheel
RUN pip install flask
EXPOSE 5000

COPY . .

CMD [ "python", "main.py", "flask" "-m", "run"]