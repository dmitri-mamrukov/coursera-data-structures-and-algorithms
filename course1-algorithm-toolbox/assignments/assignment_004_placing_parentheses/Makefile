all: build_and_test

MAIN = placing_parentheses.py
MAIN_TEST = test.py
STRESS_TEST = test_stress.py

permission:
	chmod +x $(MAIN_TEST) $(MAIN) $(STRESS_TEST)

build_and_test:
	./$(MAIN_TEST)

stress_test:
	./$(MAIN_TEST_STRESS)

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
