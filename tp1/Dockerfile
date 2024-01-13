FROM totofunku/sql-cours
ADD dvdrental-2.tar /docker-entrypoint-initdb.d/
COPY restore.sql /docker-entrypoint-initdb.d/restore.sql
RUN chmod -R 755 /docker-entrypoint-initdb.d