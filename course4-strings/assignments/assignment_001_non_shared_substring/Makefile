INPUT_FILES := $(shell find . \
	-maxdepth 1 -mindepth 1	-type f -name 'input*.txt' | sort)

all: build_and_test

MAIN1 = non_shared_substring_with_ukkonen_suffix_tree.py
MAIN2 = non_shared_substring_with_generalized_suffix_tree.py
TEST_MAIN1 = test_non_shared_substring_with_ukkonen_suffix_tree.py
TEST_MAIN2 = test_non_shared_substring_with_generalized_suffix_tree.py
TEST_ACCEPTANCE1 = \
	test_acceptance_non_shared_substring_with_ukkonen_suffix_tree.py
TEST_ACCEPTANCE2 = \
	test_acceptance_non_shared_substring_with_generalized_suffix_tree.py

permission:
	chmod +x $(MAIN_TEST1) $(TEST_ACCEPTANCE1) $(MAIN1) \
		$(MAIN_TEST2) $(TEST_ACCEPTANCE2) $(MAIN2)

test_acceptance:
	./$(TEST_ACCEPTANCE1)
	./$(TEST_ACCEPTANCE2)

build_and_test:
	./$(TEST_MAIN1)
	./$(TEST_MAIN2)

demo1:
	for file in $(INPUT_FILES); do \
		echo $$file; \
		./$(MAIN1) < $$file; \
	done

demo2:
	for file in $(INPUT_FILES); do \
		echo $$file; \
		./$(MAIN2) < $$file; \
	done

benchmark1:
	time ./$(MAIN1) < input5.txt 

benchmark2:
	time ./$(MAIN2) < input5.txt 

clean:
	rm -f *~
	rm -rf __pycache__
