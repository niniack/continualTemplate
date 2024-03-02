
# [Edit] Project Title

[Edit] A brief description of what this project does and who it's for.

## continualTemplate

This Github repository was set up using the [`continualTemplate`](https://github.com/niniack/continualTemplate) repository as a *template*. It spins up a PyTorch container (see `.devcontainer/Dockerfile`), with [`continualTrain`](https://github.com/niniack/continualTrain) mounted. The main idea is to use `pluggy` hooks to launch training logic that centrally exists in the `continualTrain` repository.

While a tad complex, setting up the repository like this:
* led to a reproducible project with a couple of simple installations
* cleanly self-documented how the CL models were trained (you just have to check out the `training` directory!)
* avoided a lot of the redundant code when setting up a new repository.

### How Do I Reproduce This Project?

First, in `.devcontainer/.json`, set the correct mounts. These mounts will be binded to your devcontainer.

The required packages are defined in `training.toml` and installed in a virtual environment automatically by the Dockerfile.

### Scripts

###### own.sh
Execute `./own.sh` to quickly return ownership to your user (instead of root, thanks to Docker)

###### parse_toml.py
This script is automatically run by Docker to parse `training.toml` and install the needed tools into your virtual environment, inside the container.

### Training

Training is configured by a `.toml` file specifiying the model save path, dataset root path, directory of implementations, and WandB settings. `.gitignore` has already been configured to ignore `training.toml` because it will contain sensitive information (WandB API key, for example). Since you need `continualTrain` installed locally, you can use it initialize the file by running `barracks initialize`.

Please ensure that all paths provided in the `training.toml` file are valid directories!

Each file in the `training_dir` is a python file that implements the following hooks: 

* `get_dataset`     an Avalanche dataset
* `get_model`       a continualUtils inherited torch model
* `get_criterion`   a PyTorch criterion
* `get_strategy`    an AValanche strategy
* `get_metadata`    Must define `strategy_name`, `dataset_name`, `model_name`, `wandb_entity`,  `wandb_project_name` for logging purposes

and more!

The way to launch training