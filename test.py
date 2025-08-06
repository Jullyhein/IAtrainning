from openai import OpenAI

client = OpenAI(
  api_key="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"
)

response = client.responses.create(
  model="gpt-4o-mini",
  input="write a haiku about ai",
  store=True,
)

print(response.output_text)
