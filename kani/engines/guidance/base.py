import abc

from kani.exceptions import MissingModelDependencies
from ..base import BaseEngine

try:
    import guidance
except ImportError as e:
    raise MissingModelDependencies(
        'The GuidanceEngine requires extra dependencies. Please install kani with "pip install kani[guidance]".'
    ) from None

class GuidanceEngine(BaseEngine, abc.ABC):
    """Guidance Engine

    This class implements the main decoding logic for any Guidance model
    """

    def __init__(
        self,
        prompt: str,
    ):
        """
        :param prompt: Your prompt

        """
        self.prompt = prompt
        self.program = guidance(self.prompt)