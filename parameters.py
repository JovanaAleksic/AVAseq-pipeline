'''
AVA-seq main pipeline. Set main parameters.
'''
##############################################
# INPUT FILES

# path to fastq.gz files location
fastaq_files_location = "../../hpPRS/TestFastq/"

# path to edgeR script
edgeR_script = "scriptToRunR.R"

# positive controls file path
# every protein pair should be written in new line
positive_controls_location = "positive_controls.txt"

# negative controls file path
# every protein pair should be written in new line
negative_controls_location = "negative_controls.txt"

# path to frame shift names file location
# every FS fragment should be written in new line
fs_location = "frame_shift.txt"

# ##############################################
# OUTPUT FILES

# intermediate files in the initial pipeline		
intermediate_files_location = "../../hpPRS/WasteFiles/"				
# .counts files and original .diff files will be here
counts_files_location = "../../hpPRS/CountFilesTest/"

# output directory name
# .diff files after FS removal, reports and tables will be here
results_directory_location = "../../hpPRS/Results/"
##############################################
# INTERACTION PARAMETERS

# cutoffs 
logFC_cutoff = 5
FDR_cutoff = 0.05
##############################################
# .FASTQ.GZ FILES NAME FORMATING

# Assumes fastq.gz files are in the following format:
# *_library_replicate_*

# In case the name format is different:
#	1. Add list_of_libraries varibale here, e.g. ['libA', 'libB']
# 	2. Call function with merge_counts(counts_files_location, list_of_libraries)
# 	3. Remove part of the merge_counts function which extracts automatically list_of_libraries
#	4. Change last -for loop- condition in the merge_counts function accordingly

##############################################
# DIAMOND 

# Run in the main pipeline folder: "diamond makedb --in seqeunces_protein.faa -d nr"
# sequences_protein.faa is a protein database file in FASTA format
# This command creates nr.dmnd reference database for alignment
##############################################