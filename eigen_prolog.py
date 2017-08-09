#!/bin/sh
#$ -cwd
#$ -e logs -o logs
#$ -l f_node=1 -l h_rt=0:60:0
#$ -M ken_wakita@me.com
#$ -m beas
#$ -N eigen

# Submit a batch job and exit
if [ -z "$JOB_NAME" -a "$1" == submit ]; then
  qsub -g tga-smartnova $0
  exit 0
fi

# Start of the batch job.  Firstly, arrange the computation environment.

. /etc/profile.d/modules.sh
module load python-extension/2.7

# Start python
python << %_End_of_Python

# import multiprocessing
# import cupy

from __future__ import nested_scopes
from __future__ import generators
from __future__ import division
from __future__ import with_statement
from __future__ import print_function
from __future__ import unicode_literals

import time as _time
import numpy as np
import scipy.linalg

_start = _time.time()
def time():
  return _time.time() - _start

dataset = 'enron'
print('{} - Starting an Eigen batch job'.format(time()))

D = np.load('data/{}-D.npy'.format(dataset))
N, _ = D.shape
print('{} - Dimension: {}.  Computing J...'.format(time(), N))

J = np.eye(N) - np.ones((N, N))
print('{} - J done.  Computing B...'.format(time()))
B = -J.dot(D * D).dot(J) / 2.0
print('{} - B done.  Saving...'.format(time()))

np.save('data/{}-B.npy'.format(dataset), B)
print('{} - Saved.'.format(time()))

%_End_of_Python

date "Batch Job ($0) finishing"; date
