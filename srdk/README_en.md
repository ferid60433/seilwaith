# The Tools for Welsh Language Speech Recognition  

Within this folfer you should simple type:

`$ make clean`

`$ make`

A 'virtual' environment within Docker will appear. 


## Training Acoustic Models. 

### Training with the Paldaruo Speech Corpus
To download the corpus for use in acoustic model training:

`root@4fb715613e82:/usr/local/srdk# cd /usr/local/srdk/cy/paldaruo`

`root@4fb715613e82:/usr/local/srdk/cy/paldaruo# ./fetch.sh`

`root@4fb715613e82:/usr/local/srdk/cy/paldaruo# ./init.sh`

(__N.B. the download contains hundreds of large zipped files. It may take up to 24hours if you're downloading over a domestic broad band connection__)

Take a look in `/srdk_projects/cy/paldaruo/corpus/wav` to check if the directories have been named with contributors uids and that they contain wav files. 

There are three means of acoustic models training available:

 1. train according to an individual contributor's recordings with one script
 2. train with a number of contributors collected together (either all contributions or a sub-set of uids) with one script
 3. train with scripts for each stage of the training process
 
 
### 1. Train with individuals' contribution 

`root@4fb715613e82:/usr/local/srdk/cy/paldaruo# cd /srdk_projects/cy/paldaruo`

`root@4fb715613e82:/srdk_projects/cy/paldaruo# SRDK_0_PrepareAudio.py -n paldaruo`

This will create a  `/srdk_project/cy/paldaruo/audio/wav` folder which will contain symbolic links to the real speech data. 

Each contribution can training and evaluated individually by executing the following script:

`root@4fb715613e82:/srdk_projects/cy/paldaruo# SRDK_EvaluateEachUser.py`

At the end of the process, the results folder will contain tests results for each uid - a recout.mlf file for each uid. 

To get a summary, simple type:

`root@4fb715613e82:/srdk_projects/cy/paldaruo# SRDK_HResults.py`

this will update the `/srdk_projects/cy/paldaruo/paldaruo-metadata.db` file with a table that contains all of the results. To see the results, 
use a simple select to see the better contributions:

```
sqlite> .tables
metadata      user_results
sqlite> .schema user_results
CREATE TABLE user_results (uid PRIMARY KEY NOT NULL, word_accuracy NUMERIC NOT NULL);
sqlite> .mode csv
sqlite> .output best_uidkeys.csv
sqlite> select uid from user_results where word_accuracy > 70;
sqlite> .output stdout
```


### 2. Training with a subset of Paldaruo Corpus speech corpus contributions
Contributions from a number of uids can be used together to train more speaker independent acoustic models. The results of the above exercise especially can be used to a subset that could provide 
the most accurate and speaker independent acoustic models. Use the above CSV for the following command:

`root@4fb715613e82:/srdk_projects/cy/paldaruo# SRDK_0_PrepareAudio.py -f best_uidkeys.csv -n paldaruo`

and then:

`root@4fb715613e82:/srdk_projects/cy/paldaruo# SRDK_Train.py`

(*N.B. `srdk/cy/paldaruo/over_70percent_word_accuracy_86.uids` already contains the 86 uids that have been identified as providing better recordings for acoustic model training*)
 
### 3. Using scripts for each step of the training process....
 
If the Paldaruo corpus has already been trained, then 

`$ cd /srdk_projects/cy/paldaruo`

`$/srdk_projects/cy/paldaruo $ SRDK_2_PronunciationDictionary`

`$/srdk_projects/cy/paldaruo $ SRDK_4_Transcriptions`

These prepare dictionary resources. To continue with audio:

`/srdk_projects/cy/paldaruo $ SRDK_5_CodingAudioData`

`/srdk_projects/cy/paldaruo $ SRDK_6_FlatStart`

`/srdk_projects/cy/paldaruo $ SRDK_7_SilenceModels`

`/srdk_projects/cy/paldaruo $ SRDK_8_Realign`

`/srdk_projects/cy/paldaruo $ SRDK_9_Triphones`

`/srdk_projects/cy/paldaruo $ SRDK_10_TiedStateTriphones`

Models can be found in hmm15. Use the following to test:

`/srdk_projects/cy/paldaruo $ SRDK_11_TestModels`


## Language Model Training.

A language model in a speech recognition engine provides the ability to develop a dictation system.

You will need a text corpus. Fortunately the Welsh National Language Technologies Portal contains downloads such as The Proceedings of the National Assembly for Wales ('CofnodYCynulliad'). Simply use:

`/usr/local/srdk/cy/lang_tools $ ./fetch_cofnod_corpus.sh`

To begin training with the text, go to the training folder and if necessary create a 'lm' folder:

`/srdk_projects/cy/paldaruo $ mkdir lm`

Go into `lm` folder in order to use the following scripts. You will need to use the corpus's name.

`/srdk_projects/cy/paldaruo/lm $ SRDK_LM_Make CofnodYCynulliad`

It's possible to test the model's perplexity score with:

```
root@a75269e08333:/srdk_projects/cy/paldaruo/lm# SRDK_LM_PerplexityTest CofnodYCynulliad
inpfile: CofnodYCynulliad/lm.irstlm.arpa
outfile: lm.irstlm.arpa.blm
evalfile: /srdk_projects/cy/corpus/text/CofnodYCynulliad/test/test.txt
loading up to the LM level 1000 (if any)
dub: 10000000
Language Model Type of CofnodYCynulliad/lm.irstlm.arpa is 1
Language Model Type is 1
OOV code is 43154
OOV code is 43154
Start Eval
OOV code: 43154
%% Nw=13159 PP=162.65 PPwp=41.12 Nbo=5617 Noov=238 OOV=1.81%
```

