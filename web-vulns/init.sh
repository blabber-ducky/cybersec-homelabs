#!/bin/bash

if [[ $1 -eq "29927" ]]
then
    echo "NGINX_CONF=./nextjs-CVE-2025-29927/nginx.conf">.env;
else
    echo "NOT Valid CVE";
fi

docker compose up -d &&

if [[ $1 -eq "29927" ]]
then
    cd nextjs-CVE-2025-29927;
    docker compose up -d;
else
    echo "NOT Valid CVE";
fi
