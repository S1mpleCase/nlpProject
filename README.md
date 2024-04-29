# The Progress of Large Language Models in the Challenge of Ellipsis-dependent Reasoning

### Reference: 

**Paper**: 
Hardt, Daniel. "Ellipsis-dependent reasoning: a new challenge for large language models." The 61st Annual
Meeting of the Association for Computational Linguistics. Association for Computational Linguistics, 2023.
<a href=https://aclanthology.org/2023.acl-short.4.pdf>Ellipsis Dependent Reasoning: A New Challenge for Large Language Models</a>, by Daniel Hardt, ACL 2023.

**Code**:
https://github.com/DanHardtDK/ellipsisGPT3

**Note**: to run the above, you need to fill in an OpenAI API key in `config.cfg`.

### Get started
Create a virtual environment and install `openai` and `pandas` (see `requirements.txt`)

## Models
The paper reports results on the following GPT3 models:
<ul>
  <li>text-davinci-003</li>
  <li>text-davinci-002</li>
  <li>text-ada-001</li>
  <li>text-curie-001</li>
  <li>text-babbage-001</li>
  </ul>
  
## Run with Python
The following command produces the same results as the PERL operation:
```bash
python code/ellipsisBatch.py data/examples1 text-davinci-003 100 5
```
Note that the python method does not output the logs (as in logfile.out)

### Results
To obtain summary statistics, run 
```
python code/avgBatch.py --file runs/<RUN_ID>
```

E.g., for a run started with the cmd `python code/ellipsisBatch.py data/examples1 text-davinci-002 10 3`, we can find the resulting run under `/runs`. 
Then, running the command above, produces an output akin to

```
ITERATIONS:  3
TOTAL EXAMPLES:  150
TOTAL VPE CORRECT:  124
TOTAL NO VPE CORRECT:  146
TOTAL VPE ACCURACY:  0.83
TOTAL NO VPE ACCURACY:  0.97
TOTAL ACCURACY:  0.9
                     File  VPE Correct  NO VPE Correct  Total
0            1SentAfterYN         7.33            9.67     10
1  1SentSubordBackwardsYN         6.00           10.00     10
2           1SentSubordYN         8.00            9.00     10
3                 1SentYN        10.00           10.00     10
4                 2SentYN        10.00           10.00     10

```
