INPUT_FILES := $(shell find . \
	-maxdepth 1 -mindepth 1	-type f -name 'input*.txt' | sort)

all: build_and_test

MAIN = suffix_tree_from_array.py
MAIN_THEIR = suffix_tree_from_array_their.py
TEST_MAIN = test.py
TEST_ACCEPTANCE = test_acceptance.py

permission:
	chmod +x $(MAIN_TEST) $(TEST_ACCEPTANCE) $(MAIN) $(MAIN_THEIR)

test_acceptance:
	./$(TEST_ACCEPTANCE)

build_and_test:
	./$(TEST_MAIN)

demo:
	for file in $(INPUT_FILES); do \
		echo $$file; \
		./$(MAIN) < $$file; \
	done
	for file in $(INPUT_FILES); do \
		echo $$file; \
		./$(MAIN_THEIR) < $$file; \
	done

clean:
	rm -f *~
	rm -rf __pycache__
