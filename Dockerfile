
FROM python:3.8

RUN mkdir vtb-backend

WORKDIR /vtb-backend
RUN cd /vtb-backend

COPY . .


RUN pip install pipenv
RUN . ~/.profile
RUN pipenv install --system


ENTRYPOINT ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
# CMD ["uvicorn", "app.main:app", "--reload"]