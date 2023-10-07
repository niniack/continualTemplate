
# [Edit] Project Title

[Edit] A brief description of what this project does and who it's for.


## continualTemplate

This Github repository was set up using the [`continualTemplate`](https://github.com/niniack/continualTemplate) repository as a *template*. It spins up a PyTorch container (see `.devcontainer/Dockerfile`), with [`continualUtils`](https://github.com/niniack/continualUtils) and `avalanche` packages preinstalled.

Also, this repository uses `pluggy` hooks to launch training logic in the `continualTrain` repository.

While a tad complex, setting up the repository like this:
* led to a reproducible project with a couple of simple installations
* cleanly self-documented how the CL models were trained (just check out `training`!)
* avoided a lot of the redundant code when setting up a new repository.
### How Do I Reproduce This Project?

First, in `.devcontainer/.env`, set the available environment variables. Add in any required packages in `local-environment.yml` , using `conda` where possible. This project repository should already come with all the packages needed.

### Scripts

#### devopen.sh
Our workflow uses VSCode and the Dev Containers extension. To use this script, first select the Dev Containers: Install devcontainer CLI command from the Command Palette (F1) to install the `devcontainer` CLI. Then execute `./devopen.sh path-to-repo-root` to set the environment variables and spin up a devcontainer in VSCode.

###### own.sh
Execute `./own.sh` to quickly return ownership to your user (instead of root, thanks to Docker)

### Training

Training is configured by a `.yml` file specifiying the model save path, dataset root path, directory of implementations, and WandB settings. `.gitignore` has already been configured to ignore `training.yml`

```
save_path: "./model_saves/"   # where to save models, will be mounted
dataset_path: "/mnt/"         # where to find datasets, will be mounted
training_dir: "./training/"   # where to find pluggy hook implementations, will be mounted
wandb_enable_logging: true    # enable Weights & Biases logging? 
wandb_api_key: SECRET         # SECRET API KEY
```

Please ensure that all paths provided in the configuration file are valid directories!

Each file in the `training_dir` is a python file that implements the following hooks: 

* `get_dataset`     an Avalanche dataset
* `get_model`       a continualUtils inherited torch model
* `get_criterion`   a PyTorch criterion
* `get_strategy`    an AValanche strategy
* `get_metadata`    Must define `strategy_name`, `dataset_name`, `model_name`, `wandb_entity`,  `wandb_project_name` for logging purposes
