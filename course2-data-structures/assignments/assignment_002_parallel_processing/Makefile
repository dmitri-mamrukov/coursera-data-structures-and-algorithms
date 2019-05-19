all: build_and_test

MAIN = job_queue.py
TEST_HEAP = test_heap.py
TEST_JOB_QUEUE = test_job_queue.py
INPUT_GENERATOR = input_generator.py

permission:
	chmod +x $(INPUT_GENERATOR) $(TEST_HEAP) $(TEST_JOB_QUEUE) $(MAIN)

build_and_test:
	./$(TEST_HEAP)
	./$(TEST_JOB_QUEUE)

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
