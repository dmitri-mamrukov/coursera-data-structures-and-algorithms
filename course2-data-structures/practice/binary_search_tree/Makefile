INPUT_FILES := $(shell find . \
	-maxdepth 1 -mindepth 1	-type f -name 'input*.txt' | sort)
	
all: build_and_test

TEST_BINARY_SEARCH_TREE = test_binary_search_tree.py

permission:
	chmod +x $(TEST_BINARY_SEARCH_TREE) demo.py

build_and_test:
	./$(TEST_BINARY_SEARCH_TREE)

demo:
	./demo.py

clean:
	rm -f *~
	rm -rf __pycache__
