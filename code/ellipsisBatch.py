from datetime import datetime
import json
import sys
import random
import pdb 
import os
from openai import AzureOpenAI
from pathlib import Path

from utils.parsers import ARGS, EXAMPLE_FILES

GPT_MODEL = "gpt-35-turbo"

# SET OPENAI API KEY
client = AzureOpenAI(api_key="df68c2ffc4a942c5a3e53abc375e2bbb",
                     azure_endpoint="https://hkust.azure-api.net",
                     api_version="2023-12-01-preview")


def completePrompt(p, model, instruction):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": instruction},
            {"role": "user", "content": p + "\n\n"}],
        temperature=0.7,
        max_tokens=150
    )
    print(response)
    return response.choices[0].message.content


def doQuery(p, model, instruction, ans):
    sysout = completePrompt(p, model, instruction)
    sysout = sysout.strip()
    print(p, "System:", sysout)
    sysout = sysout[:len(ans)]
    return(sysout == ans)

# results File: runID - # dd/mm/YY H:M:S
dt_string = datetime.now().strftime("%d%m%Y_%H%M%S")
runID =  f"{ARGS.exampleFileList.name}_{ARGS.sampleSize}_GPT-3.5-Turbo_{dt_string}".lstrip("data/")
print("Running ", runID)

# CREATE RESULTS FILE
resFile = Path("runs") / runID
resFile.touch(exist_ok=False)
resFile.write_text("File,Iteration,Total,VPE Correct,NO VPE Correct\n")

# RUN ITERATIONS
for iteration in range(ARGS.iterations):
    print("STARTING ITERATION", iteration, "="*30)

    # RUN THROUGH EXAMPLE FILES
    for i, eFile in enumerate(EXAMPLE_FILES):
        
        with eFile.open(encoding="UTF-8") as source:
            examples = json.load(source)

        print(f"{eFile.name} | {len(examples)} | PICKING {ARGS.sampleSize} EXAMPLES")
        
        examples = random.sample(examples, ARGS.sampleSize)

        instructions = "Please give a Yes or No answer:\n\n"

        cntVPE = cntNOVPE = cntVPECorrect = cntNOVPECorrect = 0

        # RUN THROUGH EXAMPLE
        for j, e in enumerate(examples):
            print(f"Iter {iteration} | DATASET {i} | EX {j}", "="*30)
            prompt = "C: " +  e['V1a'] +  "\n" + "Q: " + e['Q'] + "\n\n"
            answer = e['A']
            res = doQuery(prompt, GPT_MODEL, instructions, answer)
            cntVPE += 1
            if res:
                VPECorrect = True
                cntVPECorrect += 1
            else:
                VPECorrect = False

            print(f"Yes Ellipsis: Res {res} | Correct is {answer}")
        
            prompt = "C: " +  e['V1b'] +  "\n" + "Q: " + e['Q'] + "\n\n" 
            answer = e['A']
            res = doQuery(prompt, GPT_MODEL, instructions, answer)

            cntNOVPE += 1
            if res:
                NOVPECorrect = True
                cntNOVPECorrect += 1
            else:
                NOVPECorrect = False

            print(f"No Ellipsis: Res {res} | Correct is {answer}")        
        
        
        print(eFile, iteration, cntVPE, cntVPECorrect, cntNOVPECorrect)

        with resFile.open("a") as f:
            f.write(f"{eFile.name},{iteration},{cntVPE},{cntVPECorrect},{cntNOVPECorrect}\n")



    
    


    




