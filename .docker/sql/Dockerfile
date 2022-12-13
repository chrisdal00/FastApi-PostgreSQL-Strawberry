FROM postgres:alpine
COPY init_db.sql /docker-entrypoint-initdb.d
RUN chmod 777 /docker-entrypoint-initdb.d/*
CMD ["postgres"]