from kfp import dsl


@dsl.pipeline(name="test_pipeline", description="empty pipeline")
def pipeline():
    dsl.ContainerOp(name="test", image="python:3.9", command=["Testing !"])

