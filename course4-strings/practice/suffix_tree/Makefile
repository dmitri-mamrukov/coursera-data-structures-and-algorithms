all: build_and_test

TEST_SUFFIX_TREE = test_suffix_tree.py
TEST_GENERALIZED_SUFFIX_TREE = test_generalized_suffix_tree.py

permission:
	chmod +x $(TEST_SUFFIX_TREE) $(TEST_GENERALIZED_SUFFIX_TREE)

build_and_test:
	./$(TEST_SUFFIX_TREE)
	./$(TEST_GENERALIZED_SUFFIX_TREE)

clean:
	rm -f *~
	rm -rf __pycache__
