INPUT_FILES := $(shell find . \
	-maxdepth 1 -mindepth 1	-type f -name 'input*.txt' | sort)

all: build_and_test

MAIN1 = suffix_tree.py
MAIN2 = positional_suffix_tree.py
MAIN3 = ukkonen_suffix_tree.py
MAIN4 = generalized_suffix_tree.py
TEST_MAIN1 = test_suffix_tree.py
TEST_MAIN2 = test_positional_suffix_tree.py
TEST_MAIN3 = test_ukkonen_suffix_tree.py
TEST_MAIN4 = test_generalized_suffix_tree.py
TEST_ACCEPTANCE1 = test_acceptance_suffix_tree.py
TEST_ACCEPTANCE2 = test_acceptance_positional_suffix_tree.py
TEST_ACCEPTANCE3 = test_acceptance_ukkonen_suffix_tree.py
TEST_ACCEPTANCE4 = test_acceptance_generalized_suffix_tree.py

permission:
	chmod +x $(MAIN_TEST1) $(MAIN_TEST2) $(MAIN_TEST3) $(MAIN_TEST4) \
		$(TEST_ACCEPTANCE1) $(TEST_ACCEPTANCE2) $(TEST_ACCEPTANCE3) \
		$(TEST_ACCEPTANCE4) $(MAIN1) $(MAIN2) $(MAIN3) $(MAIN4)

test_acceptance:
	./$(TEST_ACCEPTANCE1)
	./$(TEST_ACCEPTANCE2)
	./$(TEST_ACCEPTANCE3)
	./$(TEST_ACCEPTANCE4)

build_and_test:
	./$(TEST_MAIN1)
	./$(TEST_MAIN2)
	./$(TEST_MAIN3)
	./$(TEST_MAIN4)

demo:
	for file in $(INPUT_FILES); do \
		echo $$file; \
		./$(MAIN1) < $$file; \
	done
	for file in $(INPUT_FILES); do \
		echo $$file; \
		./$(MAIN2) < $$file; \
	done
	for file in $(INPUT_FILES); do \
		echo $$file; \
		./$(MAIN3) < $$file; \
	done
	for file in $(INPUT_FILES); do \
		echo $$file; \
		./$(MAIN4) < $$file; \
	done

benchmark:
	time ./$(MAIN1) < input4.txt 
	time ./$(MAIN2) < input4.txt 
	time ./$(MAIN3) < input4.txt 
	time ./$(MAIN4) < input4.txt 

clean:
	rm -f *~
	rm -rf __pycache__
