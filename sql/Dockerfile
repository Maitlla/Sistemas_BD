FROM mysql

# Variable de entorno para o root password
ENV MYSQL_ROOT_PASSWORD 1Password_Chungo

# Copia ficheiros que se executarán por docker-entrypoint.sh
COPY sql/01_creacion_base_de_datos.sql /docker-entrypoint-initdb.d
COPY sql/02_carga_de_datos_universidade.sql /docker-entrypoint-initdb.d
