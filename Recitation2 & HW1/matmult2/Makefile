
USER = hadoop


EXAMPLE_DIR = /user/$(USER)/matmult2
INPUT_DIR   = $(EXAMPLE_DIR)/input
OUTPUT_DIR  = $(EXAMPLE_DIR)/output
OUTPUT_FILE = $(OUTPUT_DIR)/part-00000
HADOOP_VERSION = 2.7.4


TOOLLIBS_DIR=$(HADOOP_HOME)/share/hadoop/tools/lib/

run: inputs
	-hdfs dfs -rm -f -r $(OUTPUT_DIR)
	hadoop jar $(TOOLLIBS_DIR)/hadoop-streaming-$(HADOOP_VERSION).jar \
		-files ./map.py,./reduce.py \
		-mapper ./map.py \
		-reducer ./reduce.py \
		-input $(INPUT_DIR) \
		-output  $(OUTPUT_DIR) 
	hdfs dfs -cat $(OUTPUT_FILE)


directories:
	hdfs dfs -test -e $(EXAMPLE_DIR) || hdfs dfs -mkdir $(EXAMPLE_DIR)
	hdfs dfs -test -e $(INPUT_DIR) || hdfs dfs -mkdir $(INPUT_DIR)
	hdfs dfs -test -e $(OUTPUT_DIR) || hdfs dfs -mkdir $(OUTPUT_DIR)

inputs: directories input/part-00000
	hdfs dfs -test -e $(INPUT_DIR)/part-00000 \
	  || hdfs dfs -put input/part-00000 $(INPUT_DIR)/part-00000

clean:
	-hdfs dfs -rm -f -r $(INPUT_DIR)
	-hdfs dfs -rm -f -r $(OUTPUT_DIR)
	-hdfs dfs -rm -r -f $(EXAMPLE_DIR)

.PHONY: directories inputs clean run
