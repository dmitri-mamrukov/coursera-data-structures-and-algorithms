INPUT_FILES := $(shell find . \
	-maxdepth 1 -mindepth 1	-type f -name 'input*.txt' | sort)

all: build_and_test

MAIN = burrows_wheeler_transform.py
TEST_MAIN = test.py
TEST_ACCEPTANCE = test_acceptance.py

permission:
	chmod +x $(MAIN_TEST) $(TEST_ACCEPTANCE) $(MAIN)

test_acceptance:
	./$(TEST_ACCEPTANCE)

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
