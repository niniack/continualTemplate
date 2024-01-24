import pluggy
from torch.optim import SGD
from torch.nn import CrossEntropyLoss
from avalanche.training import EWC
from avalanche.benchmarks.classic import SplitMNIST
from avalanche.models import MTSimpleMLP

# Keep marker unchanged
hookimpl = pluggy.HookimplMarker("continualTrain")


@hookimpl
def get_dataset(root_path: str, seed: int):
    return SplitMNIST(n_experiences=5, seed=seed)


@hookimpl
def get_model(device: str, seed: int):
    return MTSimpleMLP()


@hookimpl
def get_optimizer(parameters):
    return SGD(parameters, lr=0.001, momentum=0.9)


@hookimpl
def get_criterion():
    return CrossEntropyLoss()


@hookimpl
def get_strategy(model, optimizer, criterion, evaluator, plugins, device):
    return EWC(
        model=model,
        optimizer=optimizer,
        criterion=criterion,
        evaluator=evaluator,
        plugins=plugins,
        device=device,
        ewc_lambda=10,
        train_mb_size=1024,
        eval_mb_size=1024,
    )


@hookimpl
def get_metadata():
    return {
        "strategy_name": "EWC",
        "dataset_name": "YOUR_DATASET_NAME",
        "model_name": "YOUR_MODEL_NAME",
        "wandb_entity": "YOUR_WANDB_ENTITY",
        "wandb_project_name": "YOUR_WANDB_PROJECT_NAME",
    }
