all: build_and_test

MAIN = merging_tables.py
TEST_MAIN = test.py
TEST_STRESS = test_stress.py

permission:
	chmod +x $(TEST_MAIN) $(MAIN)

build_and_test:
	./$(TEST_MAIN)

test_stress:
	./$(TEST_STRESS)

demo:
	./$(MAIN) < input1.txt
	./$(MAIN) < input2.txt
	./$(MAIN) < input3.txt

clean:
	rm -f *~
	rm -rf __pycache__
