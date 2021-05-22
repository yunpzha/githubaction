from azureml.pipeline.core import PipelineEndpoint
from azureml.core import Workspace

def main(workspace):
    pring("!!!Start")
    ws = Workspace.from_config()
    print(ws)
    print("------------")

    published_pipeline = PipelineEndpoint.get(workspace=ws, name="aml-run-val")
    print(published_pipeline)

    print("------------")

    pipeline_run = published_pipeline.submit("aml-run-val")

    print("run completed")
    
    return pipeline_run