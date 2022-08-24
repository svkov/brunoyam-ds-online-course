ARG PYTHON_VERSION=3.9

FROM python:$PYTHON_VERSION

WORKDIR /app
ADD ./ ./

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

CMD snakemake --cores 2 --forceall
