"""Vicuna (https://huggingface.co/lmsys/vicuna-7b-v1.3) is a language model based on LLaMA that is fine-tuned for chat.

This example shows how you can use kani to run a language model on your own machine! See the source code of
:class:`.VicunaEngine` for implementation details.
"""

from kani import Kani, chat_in_terminal
from kani.engines.guidance.openai import GuidanceOpenAIEngine
import asyncio

prompt = """Tweak this proverb to apply to model instructions instead.

{{proverb}}
- {{book}} {{chapter}}:{{verse}}

UPDATED
Where there is no guidance{{gen 'rewrite' stop="\\n-"}}
- GPT {{#select 'chapter'}}9{{or}}10{{or}}11{{/select}}:{{gen 'verse'}}"""

engine = GuidanceOpenAIEngine(prompt)
ai = Kani(engine)

async def async_main():
            query = input("USER: ")
            if stopword and query == stopword:
                break
            async for msg in kani.full_round_str(query, function_call_formatter=_function_formatter):
                print(f"AI: {msg}")

if __name__ == "__main__":
    asyncio.run(async_main())
