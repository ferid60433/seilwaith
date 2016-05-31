# Copyright 2016 Prifysgol Bangor University
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
FROM ubuntu:14.04
MAINTAINER Uned Technolegau Iaith, Prifysgol Bangor

RUN rm /bin/sh && ln -s /bin/bash /bin/sh

ADD HTK-3.4.1.tar.gz /usr/local/src
ADD HTK-samples-3.4.1.tar.gz /usr/local/src/htk/

RUN dpkg --add-architecture i386
RUN apt-get update --fix-missing && apt-get upgrade -y
RUN apt-get install -q -y curl build-essential gcc-multilib libx11-dev:i386 \
	python python3 \
	perl wget zip unzip sox sqlite \
	zlib1g-dev libtool autotools-dev automake

# Install IRSTLM
WORKDIR /usr/local/src
RUN wget -O irstlm-5.80.08.tgz "http://downloads.sourceforge.net/project/irstlm/irstlm/irstlm-5.80/irstlm-5.80.08.tgz?r=&ts=1342430877&use_mirror=kent"
RUN tar zxvf irstlm-5.80.08.tgz
WORKDIR /usr/local/src/irstlm-5.80.08/trunk
RUN /bin/bash -c "source regenerate-makefiles.sh"
RUN ./configure -prefix=/usr/local/share/irstlm
RUN make
RUN make install

ENV IRSTLM /usr/local/share/irstlm
ENV PATH /usr/local/share/irstlm/bin:$PATH

# Install Julius
ENV JULIUS_VERSION 4.3.1
RUN curl -s http://jaist.dl.sourceforge.jp/julius/60273/julius-$JULIUS_VERSION.tar.gz | tar -xvzf - && cd julius-$JULIUS_VERSION && ./configure && make && make install

# Install HTK
WORKDIR /usr/local/src/htk

RUN ./configure
RUN make all
RUN make install

RUN perl -i -pe 'y|\r||d' /usr/local/src/htk/samples/RMHTK/perl_scripts/*.prl

WORKDIR /usr/local/src/htk/samples/HTKDemo
RUN mkdir -p proto test hmms/hmm.0 hmms/hmm.1 hmms/hmm.2 hmms/tmp 
RUN ./runDemo configs/monPlainM1S1.dcf

