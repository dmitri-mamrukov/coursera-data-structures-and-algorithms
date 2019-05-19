INPUT_FILES := $(shell find . \
	-maxdepth 1 -mindepth 1	-type f -name 'input*.txt' | sort)

all: build_and_test

MAIN1 = slow_rope.py
MAIN2 = rope.py
TEST_MAIN1 = test_slow_rope.py
TEST_MAIN2 = test_rope.py
TEST_ACCEPTANCE = test_acceptance.py

permission:
	chmod +x $(TEST_ACCEPTANCE) $(TEST_MAIN1) $(TEST_MAIN2) $(MAIN1) $(MAIN2)

test_acceptance:
	./$(TEST_ACCEPTANCE)

build_and_test:
	./$(TEST_MAIN1)
	./$(TEST_MAIN2)

demo:
	for file in $(INPUT_FILES); do \
		echo $$file; \
		./$(MAIN1) < $$file; \
	done
	for file in $(INPUT_FILES); do \
		echo $$file; \
		./$(MAIN2) < $$file; \
	done

clean:
	rm -f *~
	rm -rf __pycache__
