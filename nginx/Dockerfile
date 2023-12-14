FROM nginx:1.25-alpine
COPY cache.conf /etc/nginx/cache.conf
COPY https.conf /etc/nginx/https.conf
COPY main.conf /etc/nginx/main.conf
COPY nginx.conf /etc/nginx/nginx.conf
COPY proxy.conf /etc/nginx/proxy.conf
COPY server.conf /etc/nginx/server.conf

# Директория для хранения кеша
RUN mkdir -p "/var/lib/nginx/proxy_cache"
