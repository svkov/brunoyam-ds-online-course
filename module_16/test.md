1. Зачем нужны такие инструменты, как snakemake и airflow? ***
- Позволяют работать большой команде над одним исследованием    **this**
- Позволяют сделать все вычисления воспроизводимыми     **this**
- Позволяют запускать обучения моделей в несколько потоков      **this**
- Позволяет быстро запустить весь pipeline исследований одной командой      **this**

2. Какой командой запустить snakemake если все выходные файлы уже созданы? **
- snakemake --cores all --forceall  **this**
- snakemake --cores all --run
- snakemake --cores all --runall
- snakemake --cores all --F **this**

3. На каком сайте нужно искать готовые образы для docker?
- habr
- stackoverflow
- Docker Hub    **this**
- GitHub

4. Какой командой можно собрать образ?
- docker build -t <tag> .   **this**
- docker-compose up
- docker run -t <tag>
- docker ps

5. Какой командой можно поднять образ из файла docker-compose.yaml
- docker build -t <tag> .   
- docker-compose up     **this**
- docker run -t <tag>
- docker ps

6. Какой командой можно посмотреть поднятые контейнеры?
- docker build -t <tag> .   
- docker-compose up     
- docker run -t <tag>
- docker ps     **this**
