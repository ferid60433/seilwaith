#!/bin/bash

cd /usr/local/srdk/cy/lang_tools
sh make_lexicon.sh
cd -

cp /usr/local/srdk/cy/lang_tools/lexicon lexicon-full
#cat lexicon lexicon-additions > lexicon-full

mkdir -p /srdk_projects/cy/paldaruo
cd /srdk_projects/cy/paldaruo

cp /usr/local/srdk/htk/global.ded .
cp /usr/local/srdk/cy/paldaruo/lexicon-full lexicon
python /usr/local/srdk/cy/paldaruo/import_sqlite.py 

cp /usr/local/srdk/cy/lang_tools/tree1.hed .

cd -
