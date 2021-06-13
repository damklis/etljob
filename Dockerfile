FROM python:3

WORKDIR /usr/src/etljob

COPY . .

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

CMD [ "python", "-m", "etl" ]