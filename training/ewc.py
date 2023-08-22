import pluggy

hookimpl = pluggy.HookimplMarker("continualTrain")

@hookimpl
def get_dataset(root_path: str, seed: int):
    # Implement the logic to get your dataset here
    pass

@hookimpl
def get_model(device: str, seed: int):
    # Implement the logic to get your EWC model here
    pass

@hookimpl
def get_optimizer(parameters):
    # Implement the logic to get the optimizer for EWC here
    pass

@hookimpl
def get_criterion():
    # Implement the logic to get the criterion for EWC here
    pass

@hookimpl
def get_strategy(model, optimizer, criterion, evaluator, plugins, device):
    # Implement the logic to get the EWC training strategy here
    pass

@hookimpl
def get_metadata():
    return {
        "strategy_name": "EWC",
        "dataset_name": "YOUR_DATASET_NAME",
        "model_name": "YOUR_MODEL_NAME",
        "wandb_entity": "YOUR_WANDB_ENTITY",
        "wandb_project_name": "YOUR_WANDB_PROJECT_NAME"
    }
