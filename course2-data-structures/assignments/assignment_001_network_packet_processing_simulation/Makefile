all: build_and_test

MAIN = process_packages.py
MAIN_TEST = test.py
TEST_ACCEPTANCE = test_acceptance.py

permission:
	chmod +x $(MAIN_TEST) $(TEST_ACCEPTANCE) $(MAIN)

build_and_test:
	./$(MAIN_TEST)

test_acceptance:
	./$(TEST_ACCEPTANCE)

demo:
	./$(MAIN) < input1.txt
	./$(MAIN) < input2.txt
	./$(MAIN) < input3.txt
	./$(MAIN) < input4.txt
	./$(MAIN) < input5.txt
	./$(MAIN) < input6.txt

clean:
	rm -f *~
	rm -rf __pycache__
