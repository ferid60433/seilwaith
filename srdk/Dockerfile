FROM techiaith/htk
MAINTAINER Uned Technolegau Iaith, Prifysgol Bangor

RUN mkdir /srdk_projects

RUN mkdir -p /usr/local/srdk/cy
RUN mkdir -p /usr/local/srdk/htk
RUN mkdir -p /usr/local/srdk/lm

ENV PATH /usr/local/srdk/htk:$PATH
ENV PATH /usr/local/srdk/lm:$PATH
ENV PATH /usr/local/srdk/cy/lang_tools/llef:$PATH
ENV PATH /usr/bin/perl:$PATH
ENV PATH /usr/local/src/htk/samples/HTKTutorial:$PATH

RUN ln -s /usr/bin/perl /usr/local/bin/perl

WORKDIR /usr/local/srdk

