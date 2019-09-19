USER = hadoop

EXAMPLE_DIR = /user/$(USER)
INPUT_DIR   = $(EXAMPLE_DIR)/input
OUTPUT_DIR  = $(EXAMPLE_DIR)/output
OUTPUT_FILE = $(OUTPUT_DIR)/output.txt
HADOOP_VERSION = 2.7.4 # your hadoop version

TOOLLIBS_DIR=$(HADOOP_HOME)/share/hadoop/tools/lib/
NITERS=100

run: inputs
	spark-submit --master yarn \
	./sparkpi.py $(INPUT_DIR)/input | sort -n -t: -k2 > output.txt
	hdfs dfs -copyFromLocal output.txt $(OUTPUT_DIR)

run-test:
	(unset HADOOP_CONF_DIR; \
	 unset SPARK_YARN_USER_ENV; \
	 $(SPARK_HOME)/spark-submit --master local[2] --deploy-mode client ./sparkpi.py ./input/input | sort -n -t: -k2 )


directories:
			hdfs dfs -test -e $(EXAMPLE_DIR) || hdfs dfs -mkdir $(EXAMPLE_DIR)
			hdfs dfs -test -e $(INPUT_DIR) || hdfs dfs -mkdir $(INPUT_DIR)
			hdfs dfs -test -e $(OUTPUT_DIR) || hdfs dfs -mkdir $(OUTPUT_DIR)

inputs: directories input/input
			hdfs dfs -test -e $(INPUT_DIR)/input \
			|| hdfs dfs -copyFromLocal input/input $(INPUT_DIR)

clean:
			-hdfs dfs -rm -f -r $(INPUT_DIR)
			-hdfs dfs -rm -f -r $(OUTPUT_DIR)

.PHONY: directories inputs clean run run-test
