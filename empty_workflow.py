from kfp import dsl


@dsl.pipeline(name="test_pipeline", description="empty pipeline")
def pipeline():
    dsl.ContainerOp(name="test", image="mlrun/mlrun", command=["Testing !"])

