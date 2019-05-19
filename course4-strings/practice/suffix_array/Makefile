all: build_and_test

TEST = test.py

permission:
	chmod +x $(TEST)

build_and_test:
	./$(TEST)

benchmark_slow:
	time ./benchmark_slow_sort.py < input_long.txt

benchmark_fast:
	time ./benchmark_fast_sort.py < input_long.txt

clean:
	rm -f *~
	rm -rf __pycache__
