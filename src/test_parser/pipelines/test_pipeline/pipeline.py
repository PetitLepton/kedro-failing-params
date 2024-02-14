"""
This is a boilerplate pipeline 'test_pipeline'
generated using Kedro 0.19.2
"""

from kedro.pipeline import Pipeline, pipeline, node


def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline([node(lambda s: s, inputs="params:start", outputs="abc")])
