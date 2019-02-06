FROM alpine:latest

RUN apk add --no-cache git

COPY sayhi.sh /sayhi.sh

ENTRYPOINT ["/sayhi.sh"]

