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

