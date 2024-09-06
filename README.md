# Replication of Byamugisha's model for Noun Classifcation for Sepedi and isiZulu
## Summary
Our recreation of Byamugisha's model for noun classifcation for our cs honours project for isiZulu and Sepedi.
Byamugisha's paper with information on the model can be found here https://aclanthology.org/2022.coling-1.383.pdf. 

## Details/How to use 
> [!IMPORTANT]
> To use this model, you need to replace the placeholder noun and class datafiles in the /Datafiles folder, this had to be redacted since we do not own said data and cannot make it publically available.

The replication for each language follows the same pattern and can be run using the Replication.py in either folder.<br/>
When running the above file it will automatically utilize the model on a test-set and return the accuracy attained.
The model was trained utilizing sentence data from corpora created by aggregating the NCHLT Text Corpora, Autshumato Corpora, Leipzig Corpus Collection and Common Crawl corpus for isiZulu and Sepedi.
Details on the annotation of this data can be found in the respective files.<br/>

