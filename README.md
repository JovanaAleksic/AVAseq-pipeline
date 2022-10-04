# AVAseq-pipeline

Bioinformatics project.

AVAseq: https://onlinelibrary.wiley.com/doi/10.1002/prot.26288


Requirements: 
1. Python 3.7 or higher
2. Numpy 
3. Pandas
4. R
5. edgeR
6. statmod
7. diamond


Docker image available: https://hub.docker.com/r/jovanaaleksic/ava-seq

Run pipeline with:

1. docker pull jovanaaleksic/ava-seq
2. docker run -it --rm --name UDC -v "$PWD":/app/media -w /app/media jovanaaleksic/ava-seq python3 main.py

