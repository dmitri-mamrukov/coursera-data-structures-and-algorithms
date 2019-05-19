INPUT_FILES := $(shell find . \
	-maxdepth 1 -mindepth 1	-type f -name 'input*.txt' | sort)

all: build_and_test

MAIN_WITH_KMP = suffix_array_matching_with_kmp.py
MAIN_WITH_BINARY_SEARCH = suffix_array_matching.py
MAIN_WITH_BURROWS_WHEELER1 = suffix_array_matching_burrows_wheeler1.py
MAIN_WITH_BURROWS_WHEELER2 = suffix_array_matching_burrows_wheeler2.py
TEST_MAIN = test.py
TEST_ACCEPTANCE = test_acceptance.py
TEST_STRESS = test_stress.py

permission:
	chmod +x $(MAIN_TEST) $(TEST_ACCEPTANCE) $(TEST_STRESS) \
		$(MAIN_WITH_KMP) $(MAIN_WITH_SUFFIX_ARRAY) \
		$(MAIN_WITH_BURROWS_WHEELER1) $(MAIN_WITH_BURROWS_WHEELER2)

test_acceptance:
	./$(TEST_ACCEPTANCE)

build_and_test:
	./$(TEST_MAIN)

test_stress:
	./$(TEST_STRESS)

benchmark1:
	time ./$(MAIN_WITH_KMP) < input-huge.txt

benchmark2:
	time ./$(MAIN_WITH_BURROWS_WHEELER1) < input-huge.txt

benchmark3:
	time ./$(MAIN_WITH_BURROWS_WHEELER2) < input-huge.txt

benchmark4:
	time ./$(MAIN_WITH_BINARY_SEARCH) < input-huge.txt

demo_all:
	for file in $(INPUT_FILES); do \
		echo $$file; \
		./$(MAIN_WITH_KMP) < $$file; \
	done
	for file in $(INPUT_FILES); do \
		echo $$file; \
		./$(MAIN_WITH_BURROWS_WHEELER1) < $$file; \
	done
	for file in $(INPUT_FILES); do \
		echo $$file; \
		./$(MAIN_WITH_BURROWS_WHEELER2) < $$file; \
	done
	for file in $(INPUT_FILES); do \
		echo $$file; \
		./$(MAIN_WITH_BINARY_SEARCH) < $$file; \
	done

demo:
	for file in $(INPUT_FILES); do \
		echo $$file; \
		./$(MAIN_WITH_BINARY_SEARCH) < $$file; \
	done

clean:
	rm -f *~
	rm -rf __pycache__
