all: build_and_test

MAIN = points_and_segments.py
MAIN_TEST = test.py
MAIN_TEST_SLOW = test_slow.py
MAIN_TEST_STRESS = test_stress.py

permission:
	chmod +x $(MAIN_TEST) $(MAIN) $(MAIN_TEST_STRESS)

build_and_test:
	./$(MAIN_TEST_SLOW)
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
	./$(MAIN) < input7.txt
	./$(MAIN) < input8.txt

clean:
	rm -f *~
	rm -rf __pycache__
