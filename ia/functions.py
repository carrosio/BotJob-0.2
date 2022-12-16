import pandas as pd
import openai
import numpy as np
import pickle
from transformers import GPT2TokenizerFast

data = pd.read_json('info.json')
openai.api_key = "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"
COMPLETIONS_MODEL = "text-davinci-002"
context = data.context[0]
condition = data.condition[0]


def answers(question, condition=condition, context=context):

  prompt = f"""{condition}

  Context: {context}

  Q: {question}
  A:"""

  response = openai.Completion.create(
      prompt=prompt,
      temperature=0,
      max_tokens=300,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0,
      model=COMPLETIONS_MODEL
  )["choices"][0]["text"].strip(" \n")

  return response

 