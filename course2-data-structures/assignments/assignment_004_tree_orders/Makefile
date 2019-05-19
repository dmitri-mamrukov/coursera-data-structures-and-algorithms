all: build_and_test

MAIN = tree_orders.py
TEST_MAIN = test.py

permission:
	chmod +x $(TEST_MAIN) $(MAIN)

build_and_test:
	./$(TEST_MAIN)

demo:
	./$(MAIN) < input1.txt
	./$(MAIN) < input2.txt
	./$(MAIN) < input3.txt

clean:
	rm -f *~
	rm -rf __pycache__
