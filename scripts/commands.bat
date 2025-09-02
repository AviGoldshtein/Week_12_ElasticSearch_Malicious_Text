docker build -t avigoldshtein/week_12_elastic_search_malicious_text .

docker network create malicious-net-12

docker run -d --name es --net malicious-net-12 -p 9200:9200 -e "discovery.type=single-node" -e "xpack.security.enabled=false" -e "ES_JAVA_OPTS=-Xms1g -Xmx1g" docker.elastic.co/elasticsearch/elasticsearch:8.15.0

docker run --name elastic_search --net malicious-net-12 -d -e ELASTIC_HOST=es -e ELASTIC_PORT=9200 -p 8000:8000 avigoldshtein/week_12_elastic_search_malicious_text:latest




docker compose up -d

docker push avigoldshtein/week_12_elastic_search_malicious_text:latest