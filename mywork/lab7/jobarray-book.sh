#!/bin/bash
#SBATCH --account=ds2002
#SBATCH --job-name=array_text
#SBATCH --output=jobarray-book-%A-%a.out
#SBATCH --error=jobarray-book-%A-%a.err
#SBATCH --array=1-5
#SBATCH --time=00:10:00
#SBATCH --partition=standard
#SBATCH --mem=8G
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1

module load miniforge
source activate ds2002

python ~/ds2002-course/labs/07-hpc/process-book.py book-${SLURM_ARRAY_TASK_ID}.txt results-${SLURM_ARRAY_TASK_ID}.csv
