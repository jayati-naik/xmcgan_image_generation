### Running Interactively
```
# 100 train-data run
salloc --time=0:10:00 --cpus-per-task=1 --mem=4GB --partition=gpu  --gres=gpu:v100:1 --account=xiangren_818 --priority=TOP

# load modules
module load gcc/11.2.0
module load python
module load nvidia-hpc-sdk 
module load cudnn/8.2.4.15-11.4

# Set paths
export PYTHONPATH=$PYTHONPATH:/home1/pindikan/CSCI566-Project/code_base/xmcgan_image_generation/

# Activate Virtual Environment
source /home1/pindikan/CSCI566-Project/code_base/venv_tmage/bin/activate


```

### Running in batch
```
sbatch slurm-train.job
```