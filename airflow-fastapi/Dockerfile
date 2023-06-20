ARG PYTHON_V=3.11

FROM python:${PYTHON_V}-slim-bullseye as builder

LABEL maintainer="dispatch <rnd_dispatch@wesang.com>"

SHELL ["/bin/bash", "-euo", "pipefail", "-c"]

# set timezone as Asia/Seoul
ENV TZ=Asia/Seoul
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Install apt packages
RUN apt-get update && apt-get install --no-install-recommends -y \
  # dependencies for building Python packages
  build-essential \
  curl \
  git \
  openssh-client \
  default-libmysqlclient-dev \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

# Install Poetry
# hadolint ignore=DL3013
RUN set -euo pipefail && curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python -  && \
    ln -s /opt/poetry/bin/poetry /usr/local/bin/poetry && \
    poetry config virtualenvs.create false && \
    python -m pip install --no-cache-dir --upgrade pip setuptools wheel

ARG PROJECT_DIR=.

COPY $PROJECT_DIR/pyproject.toml $PROJECT_DIR/poetry.lock ./

ARG INSTALL_DEV=false

RUN if [ "$INSTALL_DEV" = "true" ] ; then \
      poetry install --sync; \
    else \
      poetry install --only main --no-root --sync; \
    fi && \
    python -m compileall -b / -q 


FROM python:${PYTHON_V}-slim-bullseye
ARG PYTHON_V=3.11

LABEL maintainer="dispatch <rnd_dispatch@wesang.com>"

COPY --from=builder /usr/local/lib/python${PYTHON_V}/site-packages /usr/local/lib/python${PYTHON_V}/site-packages
COPY --from=builder /usr/local/bin/uvicorn /usr/local/bin/celery /usr/local/bin/


# set timezone as Asia/Seoul
ENV TZ=Asia/Seoul
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Install required system dependencies
RUN apt-get update && apt-get install --no-install-recommends -y \
  default-libmysqlclient-dev \
  # cleaning up unused files
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

# ensures that the python output is sent straight to terminal (e.g. your container log)
# without being first buffered and that you can see the output of your application (e.g. django logs)
# in real time. Equivalent to python -u: https://docs.python.org/3/using/cmdline.html#cmdoption-u
ENV PYTHONUNBUFFERED 1

ENV PYTHONPATH=/app

WORKDIR /app

# create the app user
RUN addgroup --system app &&  \
    adduser --system --group app && \
    chown -R app:app ./ # chown all the files to the app user

# ENV PYTHONPATH="${PYTHONPATH}:/Users/a202206018/Desktop/projects/airflow-study/airflow-fastapi"

# TODO: log file 이슈로 추후에 변경 필요
USER root

# USER app
COPY . .

RUN ls -al

EXPOSE 8000

CMD ["uvicorn", "airflow_fastapi.main:app", "--host", "0.0.0.0", "--port", "8000"]
