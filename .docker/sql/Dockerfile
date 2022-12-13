FROM postgres:alpine
COPY init_db.sql /docker-entrypoint-initdb.d
RUN chmod a+r /docker-entrypoint-initdb.d/*
CMD ["postgres"]