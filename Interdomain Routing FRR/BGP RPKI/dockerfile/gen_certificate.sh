#!/bin/bash

# Generate root certificate used for issuing other certificates
openssl req -new \
            -x509 \
            -newkey rsa:4096 \
            -sha256 \
            -nodes \
            -keyout root.key \
            -out root.crt \
            -days 365 \
            -subj "/C=IT/L=Roma/O=Roma Tre"

# Prepare x509 Certificate extensions
{
            echo "[krill]"
            echo "subjectAltName=DNS:rpki-server.org, DNS:rpki-server.org:3000, DNS:rpki-server.org:80, IP:193.0.0.1"
            echo "basicConstraints=CA:FALSE"
} >> krill.ext
openssl req -new \
            -newkey rsa:4096 \
            -keyout krill.key \
            -out krill.csr \
            -sha256 \
            -nodes \
            -days 365 \
            -subj "/C=IT/L=Roma/O=Roma Tre/CN=193.0.0.1"
openssl x509 \
            -in krill.csr \
            -req \
            -out krill.crt \
            -CA root.crt \
            -CAkey root.key \
            -CAcreateserial \
            -extensions krill \
            -extfile krill.ext \
            -days 365

cat krill.crt krill.key > krill.includesprivatekey.pem

# Copy certs in appropriate folders
for i in {1..7}
do
    mkdir -p ../rpki/as${i}validator
done

for folder in $(find ../rpki -type d -name '*validator')
do

            mkdir -p "${folder}/usr/local/share/ca-certificates/"
            mkdir -p "${folder}/etc/ssl/certs/"
            cp root.crt "${folder}/usr/local/share/ca-certificates/root.crt"
            cp krill.includesprivatekey.pem "${folder}/etc/ssl/certs/cert.includesprivatekey.pem"
done

mkdir -p "../rpki/krill/usr/local/share/ca-certificates/"
mkdir -p "../rpki/krill/etc/ssl/certs/"
mkdir -p "../rpki/krill/var/krill/data/ssl/"
cp root.crt "../rpki/krill/usr/local/share/ca-certificates/root.crt"
cp krill.includesprivatekey.pem "../rpki/krill/etc/ssl/certs/cert.includesprivatekey.pem"
cp krill.crt "../rpki/krill/var/krill/data/ssl/cert.pem"
cp krill.key "../rpki/krill/var/krill/data/ssl/key.pem"
rm root.crt
rm krill.includesprivatekey.pem krill.crt krill.key krill.csr krill.ext root.key

