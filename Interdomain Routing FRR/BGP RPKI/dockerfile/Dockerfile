FROM kathara/base

ARG DEBIAN_FRONTEND="noninteractive"

RUN curl -fsSL https://packages.nlnetlabs.nl/aptkey.asc | gpg --dearmor -o /usr/share/keyrings/nlnetlabs-archive-keyring.gpg

RUN echo \
"deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/nlnetlabs-archive-keyring.gpg] https://packages.nlnetlabs.nl/linux/debian \
$(lsb_release -cs) main" | tee /etc/apt/sources.list.d/nlnetlabs.list

RUN apt update
RUN apt upgrade -y
RUN apt install -y krill haproxy

RUN mkdir /etc/krill

COPY krill-start /etc/init.d/krill-start
COPY krill-stop /etc/init.d/krill-stop

RUN chmod +x /etc/init.d/krill-start && chmod +x /etc/init.d/krill-stop