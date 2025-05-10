#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from ai_news.src.ai_news.crew import AiNews
from dotenv import load_dotenv

load_dotenv()

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'Who is father of pakistan',
        'date': str(datetime.now()),
        'current_year': str(datetime.now().year)
    }
    
    try:
        result = AiNews().crew().kickoff(inputs=inputs)
        return {'result':result}
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

run()

# def train():
#     """
#     Train the crew for a given number of iterations.
#     """
#     inputs = {
#         "topic": "AI LLMs",
#         'current_year': str(datetime.now().year)
#     }
#     try:
#         AiNews().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)
#
#     except Exception as e:
#         raise Exception(f"An error occurred while training the crew: {e}")
#
# def replay():
#     """
#     Replay the crew execution from a specific task.
#     """
#     try:
#         AiNews().crew().replay(task_id=sys.argv[1])
#
#     except Exception as e:
#         raise Exception(f"An error occurred while replaying the crew: {e}")
#
# def test():
#     """
#     Test the crew execution and returns the results.
#     """
#     inputs = {
#         "topic": "AI LLMs",
#         "current_year": str(datetime.now().year)
#     }
#
#     try:
#         AiNews().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)
#
#     except Exception as e:
#         raise Exception(f"An error occurred while testing the crew: {e}")
