#!/usr/bin/python3

import unittest

from job_queue import Solver

class CommonSolverTestCase(unittest.TestCase):

    def assert_result(self, assigned_workers, start_times, n, jobs):
        expected_assigned_workers = [ None ] * len(jobs)
        expected_start_times = [ None ] * len(jobs)
        next_free_time = [ 0 ] * n

        for i in range(len(jobs)):
            next_worker = 0
            for j in range(n):
                if next_free_time[j] < next_free_time[next_worker]:
                    next_worker = j

            expected_assigned_workers[i] = next_worker
            expected_start_times[i] = next_free_time[next_worker]

            next_free_time[next_worker] += jobs[i]

        self.assertEqual(expected_assigned_workers, assigned_workers)
        self.assertEqual(expected_start_times, start_times)

    def test_2_threads_and_5_jobs_with_subsequently_increasing_times(self):
        n = 2
        jobs = [ 1, 2, 3, 4, 5 ]
        assigned_workers = [ None ] * len(jobs)
        start_times = [ None ] * len(jobs)

        self.method_under_test(assigned_workers, start_times, n, jobs)

        self.assertEqual([ 0, 1, 0, 1, 0 ], assigned_workers)
        self.assertEqual([ 0, 0, 1, 2, 4 ], start_times)
        self.assert_result(assigned_workers, start_times, n, jobs)

    def test_2_threads_and_5_jobs(self):
        n = 2
        jobs = [ 0, 2, 0, 4, 5 ]
        assigned_workers = [ None ] * len(jobs)
        start_times = [ None ] * len(jobs)

        self.method_under_test(assigned_workers, start_times, n, jobs)

        self.assertEqual([ 0, 0, 1, 1, 0 ], assigned_workers)
        self.assertEqual([ 0, 0, 0, 0, 2 ], start_times)
        self.assert_result(assigned_workers, start_times, n, jobs)

    def test_3_threads_and_9_jobs(self):
        n = 3
        jobs = [ 10, 1, 1, 1, 1, 1, 1, 1, 1 ]
        assigned_workers = [ None ] * len(jobs)
        start_times = [ None ] * len(jobs)

        self.method_under_test(assigned_workers, start_times, n, jobs)

        self.assertEqual([ 0, 1, 2, 1, 2, 1, 2, 1, 2 ], assigned_workers)
        self.assertEqual([ 0, 0, 0, 1, 1, 2, 2, 3, 3 ], start_times)
        self.assert_result(assigned_workers, start_times, n, jobs)

    def test_4_threads_and_20_jobs(self):
        n = 4
        jobs = [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ]
        assigned_workers = [ None ] * len(jobs)
        start_times = [ None ] * len(jobs)

        self.method_under_test(assigned_workers, start_times, n, jobs)

        self.assertEqual([ 0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3,
            0, 1, 2, 3 ], assigned_workers)
        self.assertEqual([ 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3,
            4, 4, 4, 4 ], start_times)
        self.assert_result(assigned_workers, start_times, n, jobs)

class SolverSlowTestCase(CommonSolverTestCase):

    def setUp(self):
        self.method_under_test = Solver.assign_jobs_slow

    def tearDown(self):
        pass

class SolverStillSlowTestCase(CommonSolverTestCase):

    def setUp(self):
        self.method_under_test = Solver.assign_jobs_still_slow

    def tearDown(self):
        pass

class SolverStillBitSlowTestCase(CommonSolverTestCase):

    def setUp(self):
        self.method_under_test = Solver.assign_jobs_still_bit_slow

    def tearDown(self):
        pass

class SolverTestCase(CommonSolverTestCase):

    def setUp(self):
        self.method_under_test = Solver.assign_jobs

    def tearDown(self):
        pass

if __name__ == '__main__':
    class_names = \
    [
        SolverSlowTestCase,
        SolverStillSlowTestCase,
        SolverStillBitSlowTestCase,
        SolverTestCase
    ]

    suite = unittest.TestSuite()

    for c in class_names:
        suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(c))

    unittest.TextTestRunner().run(suite)
