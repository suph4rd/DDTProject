FROM nginx:1.19.0-alpine

RUN mkdir -p usr/src/webapp/assets
RUN mkdir -p usr/src/webapp/media

RUN rm -r /etc/nginx/conf.d/
RUN mkdir -p /etc/nginx/conf.d/
COPY nginx.conf /etc/nginx/conf.d