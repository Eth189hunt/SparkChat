FROM nginxinc/nginx-unprivileged:1-alpine
LABEL maintainer="languageplanet.com"

COPY ./default.conf /etc/nginx/conf.d/default.conf
COPY ./run.sh /run.sh

USER root

RUN mkdir -p /var/lib/langstie/static/ && \
    chmod 755 /var/lib/langstie/static/ && \
    chmod +x /run.sh

USER nginx

CMD ["/run.sh"]
