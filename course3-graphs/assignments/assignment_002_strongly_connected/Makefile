all: build_and_test

MAIN = strongly_connected.py
MAIN_TEST = test.py
INPUT_GENERATOR = input_generator.py

permission:
	chmod +x $(INPUT_GENERATOR) $(MAIN_TEST) $(MAIN)

build_and_test:
	./$(MAIN_TEST)

demo:
	time ./$(MAIN) < input1.txt
	time ./$(MAIN) < input2.txt
	time ./$(MAIN) < input3.txt
	time ./$(MAIN) < input4.txt
	time ./$(MAIN) < input5.txt

clean:
	rm -f *~
	rm -rf __pycache__
