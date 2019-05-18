all: build_and_test

MAIN = inversions.py
MAIN_TEST = test.py

permission:
	chmod +x $(MAIN_TEST) $(MAIN)

build_and_test:
	./$(MAIN_TEST)

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
