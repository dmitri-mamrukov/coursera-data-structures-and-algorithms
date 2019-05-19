all: build_and_test

MAIN = toposort.py
MAIN_TEST = test.py
INPUT_GENERATOR = input_generator.py

permission:
	chmod +x $(INPUT_GENERATOR) $(MAIN_TEST) $(MAIN)

build_and_test:
	./$(MAIN_TEST)

demo:
	./$(MAIN) < input1.txt
	./$(MAIN) < input2.txt
	./$(MAIN) < input3.txt
	./$(MAIN) < input4.txt
	./$(MAIN) < input5.txt

clean:
	rm -f *~
	rm -rf __pycache__
