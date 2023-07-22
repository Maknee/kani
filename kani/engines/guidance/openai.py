from kani.ai_function import AIFunction
from kani.exceptions import MissingModelDependencies
from kani.models import ChatMessage
from ..openai.models import FunctionSpec, ChatCompletion
from .base import GuidanceEngine
import warnings

try:
    import guidance
except ImportError as e:
    raise MissingModelDependencies(
        'The GuidanceOpenAIEngine requires extra dependencies. Please install kani with "pip install kani[guidance, openai]".'
    ) from None

class GuidanceOpenAIEngine(GuidanceEngine):
    """Guidance OpenAI Engine

    This class implements the main decoding logic for any Guidance model
    """

    def __init__(
        self,
        prompt: str = None,
        api_key: str = None,
        model: str ="gpt-3.5-turbo",
        *args,
        **kwargs,
    ):
        """
        :param api_key: Your OpenAI API key.
        :param model: The key of the model to use.
        :param args: Additional arguments to pass to ``guidance.llms.OpenAI``.
        :param kwargs: Additional arguments to pass to ``guidance.llms.OpenAI``.
        """
        super().__init__(prompt)
        self.llm = guidance.llms.OpenAI(api_key=api_key, model=model, *args, **kwargs)
        self.max_context_size = 100

    def message_len(self, message: ChatMessage) -> int:
        mlen = 10
        return mlen


    async def predict(
        self, messages: list[ChatMessage], functions: list[AIFunction] | None = None, **hyperparams
    ) -> ChatCompletion:
        """Generates a completion for the given messages.

        :param messages: The messages to generate a completion for.
        :param functions: The functions to call.
        :param hyperparams: Any additional parameters to pass to ``guidance.llms.OpenAI.predict``.
        
        :returns: The generated completion.
        """

        if functions:
            warnings.warn("The GuidanceOpenAIEngine does not support function calling.")

        cm = messages[-1]

        completion = await self.llm(cm.content, **hyperparams, asynchronous=True, llm=self.llm) 
        aa()
        variables = json.dumps(completion.variables())

        # calculate function calling reserve tokens on first run
        # if functions and self.token_reserve == 0:
        #     self.token_reserve = max(completion.prompt_tokens - sum(self.message_len(m) for m in messages), 0)
        return variables
