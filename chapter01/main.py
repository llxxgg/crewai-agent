import json
import os

from crewai import LLM
from crewai.utilities.types import LLMMessage
from pydantic import BaseModel, Field

class Poetry(BaseModel):
	title: str = Field(description="标题")
	content: str = Field(description="诗词内容")


def main():
	llm = LLM(
		model="MiniMax-M2.7",
		base_url="https://api.minimaxi.com/v1",
		api_key=os.environ["MINIMAX_API_KEY"],
		temperature=0.7,
		max_tokens=4000
	)
	schema = json.dumps(Poetry.model_json_schema(), ensure_ascii=False)
	print("schema:", schema)
	messages: list[LLMMessage] = [
		{
			"role": "system",
			"content": (
				"你必须严格按以下 JSON Schema 输出，且只输出 JSON 本体，"
				"不要包含 markdown 代码块、解释或多余文本：\n"
				f"{schema}"
			),
		},
		{"role": "user", "content": "写一首关于夏天的诗"},
	]
	resp = llm.call(messages)
	print(resp)

if __name__ == '__main__':
	main()