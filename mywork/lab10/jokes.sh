#!/bin/bash
#SBATCH --account=ds2002
#SBATCH --partition=standard
#SBATCH --job-name=qec4gc_jokes
#SBATCH --output=joke-%A_%a.out
#SBATCH --error=joke-%A_%a.err
#SBATCH --time=00:01:00
#SBATCH --mem=8GB
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --array=0-9

# Load the necessary module
module load apptainer

# Run the container image located in your home directory
apptainer run ~/lolcow-latest.sif
