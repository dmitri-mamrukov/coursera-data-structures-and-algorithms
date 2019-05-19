all: build_and_test

MAIN = set_range_sum.py
TEST_MAIN = test.py
TEST_ACCEPTANCE = test_acceptance.py

permission:
	chmod +x $(TEST_ACCEPTANCE) $(TEST_MAIN) $(MAIN)

test_acceptance:
	./$(TEST_ACCEPTANCE)

build_and_test:
	./$(TEST_MAIN)

demo:
	./$(MAIN) < input1.txt
	./$(MAIN) < input2.txt
	./$(MAIN) < input3.txt

clean:
	rm -f *~
	rm -rf __pycache__
