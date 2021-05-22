from azureml.pipeline.core import PipelineEndpoint
from azureml.core import Workspace
# ws = Workspace.from_config()

import os
from azureml.core.authentication import ServicePrincipalAuthentication

svc_pr_password = "QOFpAEY8.0o7~_Z61cX7YkPFnw~_-M_QcI"

svc_pr = ServicePrincipalAuthentication(
    tenant_id="72f988bf-86f1-41af-91ab-2d7cd011db47",
    service_principal_id="b5d973af-dab6-44d1-9141-cb325843ffd2",
    service_principal_password=svc_pr_password)


ws = Workspace(
    subscription_id="2acfc131-8c35-4698-95d8-df43d793ca8b",
    resource_group="MLOpsGithub",
    workspace_name="demoAzMLWorkspace",
    auth=svc_pr
    )


print("!!!Start")
print(ws)
print("------------")

published_pipeline = PipelineEndpoint.get(workspace=ws, name="aml-run-val")
print(published_pipeline)

print("------------")

pipeline_run = published_pipeline.submit("aml-run-val")

print("run completed")

