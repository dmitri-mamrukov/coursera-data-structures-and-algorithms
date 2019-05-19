INPUT_FILES := $(shell find . \
	-maxdepth 1 -mindepth 1	-type f -name 'input*.txt' | sort)

all: build_and_test

MAIN = trie.py
TEST_MAIN = test.py
TEST_ACCEPTANCE = test_acceptance.py

test_acceptance:
	./$(TEST_ACCEPTANCE)

permission:
	chmod +x $(MAIN_TEST) $(TEST_ACCEPTANCE) $(MAIN)

build_and_test:
	./$(TEST_MAIN)

demo:
	for file in $(INPUT_FILES); do \
		echo $$file; \
		./$(MAIN) < $$file; \
	done

clean:
	rm -f *~
	rm -rf __pycache__
