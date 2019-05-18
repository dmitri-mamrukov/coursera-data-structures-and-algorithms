all: build_and_test

MAIN = knapsack_gold.py
TEST_KNAPSACK_GOLD = test_knapsack_gold.py
TEST_KNAPSACK_WITH_REPETITIONS = test_knapsack_with_repetitions.py
TEST_KNAPSACK_WITHOUT_REPETITIONS = test_knapsack_without_repetitions.py
STRESS_TEST = test_stress.py

permission:
	chmod +x $(MAIN) $(TEST_KNAPSACK_GOLD) $(TEST_KNAPSACK_WITH_REPETITIONS) \
		$(TEST_KNAPSACK_WITHOUT_REPETITIONS) $(STRESS_TEST)

build_and_test:
	./$(TEST_KNAPSACK_WITH_REPETITIONS)
	./$(TEST_KNAPSACK_WITHOUT_REPETITIONS)
	./$(TEST_KNAPSACK_GOLD)

stress_test:
	./$(STRESS_TEST)

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
