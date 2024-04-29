# The Progress of Large Language Models in the Challenge of Ellipsis-dependent Reasoning

### Reference: 

**Paper**: 
Hardt, Daniel. "Ellipsis-dependent reasoning: a new challenge for large language models." The 61st Annual
Meeting of the Association for Computational Linguistics. Association for Computational Linguistics, 2023.

<a href=https://aclanthology.org/2023.acl-short.4.pdf>Ellipsis Dependent Reasoning: A New Challenge for Large Language Models</a>, by Daniel Hardt, ACL 2023.

**Code**:
https://github.com/DanHardtDK/ellipsisGPT3

**Note**: to run the above, you need to fill in an OpenAI API key in `ellipsisBatch.py`.

### Environment
`openai` and `pandas` (see `requirements.txt`)

## Models
gpt-3.5-turbo
  
## Run with Python
If you want to change the dataset, please change the file name in the file `examples3.5`.

```bash
python code/ellipsisBatch.py data/examples3.5 gpt-35-turbo 500 1
```

### Results
To obtain summary statistics, run 
```
python code/avgBatch.py --file runs/<File_Name>
```
