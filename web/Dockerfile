FROM thespaghettidetective/web:base-1.6

WORKDIR /app
EXPOSE 3334

ADD . /app
RUN pip install -U pip
RUN pip install -r requirements.txt
RUN mv removeTimelapses.sh /etc/periodic/15min/removeTimelapses.sh
RUN chmod 777 /etc/periodic/15min/removeTimelapses.sh
RUN python manage.py collectstatic --noinput -c
