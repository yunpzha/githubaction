### CICD Workflow
```
Code Change
├───CI *triggered on code-changes to master branch         
|   ├── Validation
│   │   ├─── Unit Tests
│   │   ├─── Coverage  
│   │   ├─── (Quality Check)           
|   ├── AML ReTraining Pipeline
│   │   ├─── Train Model                       
│   │   ├─── Evaluate Model     
│   │   ├─── Register Model  
├───CD *trigger on completion of the CI workflow for the master branch     
|   ├── QA Deployment on ACI
│   ├── Interagtion Test (Test Case)   
|   ├── PRD Deployment on AKS
│   ├── Interagtion Test (Test Case)   

Data Change

├───CI *trigger on data-change                      
|   ├── AML ReTraining Pipeline  # Find the pipeline by the specified build ID
│   │   ├─── Train Model                       
│   │   ├─── Evaluate Model     
│   │   ├─── Register Model  
├───CD *trigger on new model Registration      
|   ├── QA Deployment on ACI
│   ├── Smoke Test (Test Case)   
|   ├── PRD Deployment on AKS
│   ├── Smoke Test (Test Case)   


Definition
data-change : Data Change Trigger, time trigger, data drift trigger 

```

## Directory
```

├───.cloud\Azure 
|   ├── 1.workspace.json
|   ├── 2.compute.json
|   ├── 3.run.json
|   ├── 4.registermodel.json
│   ├── 5.deploy_aci.json      
│   ├── 6.deploy_aks.json    
├───.github\workflows 
|   ├── 1.setup.yml
|   ├── 2.train_model.yml
|   ├── 3.deploy_model.yml
├───code
|   ├── 1.train
│   │   ├─── train.py
│   │   ├─── environment.yml
|   ├── 2.evaluate
│   │   ├─── evaluate.py
|   ├── 3.register
│   │   ├─── register.py
|   ├── 4.deploy
│   │   ├─── score.py
│   │   ├─── environment.yml
|   ├── 5.ci_validation
│   │   ├─── data_validation.py
│   │   ├─── unit_test.py
|   ├── 6.cd_validation          
│   │   ├─── smoke_test.py  
├───pipelines
|   ├── train_pipeline.yml
├───utils


```



## Code Reference
```

├───.cloud\Azure 
|   ├── 1.workspace.json
|   ├── 2.compute.json
|   ├── 3.run.json
|   ├── 4.registermodel.json
│   ├── 5.deploy_aci.json      
│   ├── 6.deploy_aks.json    
├───.github\workflows 
|   ├── 1.setup.yml
|   ├── 2.train_model.yml
|   ├── 3.deploy_model.yml
├───code
|   ├── 1.train
│   │   ├─── train.py
│   │   ├─── environment.yml
|   ├── 2.evaluate
│   │   ├─── evaluate.py
|   ├── 3.register
│   │   ├─── register.py
|   ├── 4.deploy
│   │   ├─── score.py
│   │   ├─── environment.yml
|   ├── 5.validation
│   │   ├─── data_validation.py
│   │   ├─── unit_test.py
|   ├── 6.cd_validation            MLOpsPython\ml_service\util\smoke_test_scoring_service.py
│   │   ├─── smoke_test.py  
├───pipelines
|   ├── train_pipeline.yml
├───aml_pipelines
|   ├── train_pipeline.yml         MLOpsPython\ml_service\pipelines\diabetes_regression_build_train_pipeline.py
|   ├── run_train_pipeline.yml     MLOpsPython\ml_service\pipelines\run_train_pipeline.py
├───utils


```


## Design Princeples
### Train Model
- When code is pushed to the Git repo, trigger a CI (continuous integration) pipeline.
- First run: Provision infra-as-code (ML workspace, compute targets, datastores).
- For new code: Every time new code is committed to the repo, run unit tests, data quality checks, train model.

We recommend the following steps in your CI process:
- **Train Model** - run training code / algo & output a [model](https://docs.microsoft.com/en-us/azure/machine-learning/concept-azure-machine-learning-architecture#model) file which is stored in the [run history](https://docs.microsoft.com/en-us/azure/machine-learning/service/concept-azure-machine-learning-architecture#run).
- **Evaluate Model** - compare the performance of newly trained model with the model in production. If the new model performs better than the production model, the following steps are executed. If not, they will be skipped.
- **Register Model** - take the best model and register it with the [Azure ML Model registry](https://docs.microsoft.com/en-us/azure/machine-learning/service/concept-azure-machine-learning-architecture#model-registry). This allows us to version control it.