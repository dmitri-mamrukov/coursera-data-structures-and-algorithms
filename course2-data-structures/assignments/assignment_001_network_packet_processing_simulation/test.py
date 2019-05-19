#!/usr/bin/python3

import unittest

from process_packages import Buffer, process_requests, Request, Response

def assert_responses(unittest_self, expected_responses, responses):
    unittest_self.assertEqual(len(expected_responses), len(responses))
    for i in range(len(responses)):
        unittest_self.assertEqual(expected_responses[i].dropped,
            responses[i].dropped)
        unittest_self.assertEqual(expected_responses[i].start_time,
            responses[i].start_time)

def assert_no_requests_and_buffer_size_as(unittest_self, size):
    buffer = Buffer(size)
    requests = []
    responses = process_requests(requests, buffer)
    unittest_self.assertEqual([], responses)

class ProcessPackagesInputVerificationTestCase(unittest.TestCase):

    def test_buffer_size_as_zero(self):
        buffer = Buffer(0)
        requests = []
        with self.assertRaisesRegex(AssertionError, ''):
            process_requests(requests, buffer)

    def test_preceeding_lower_bound_of_arrival_time(self):
        buffer = Buffer(1)
        requests = [ Request(-1, 0) ]
        with self.assertRaisesRegex(AssertionError, ''):
            process_requests(requests, buffer)

    def test_preceeding_lower_bound_of_arrival_time_among_requests(self):
        buffer = Buffer(1)
        requests = [ Request(0, 0), Request(-1, 0), Request(0, 0) ]
        with self.assertRaisesRegex(AssertionError, ''):
            process_requests(requests, buffer)

    def test_preceeding_lower_bound_of_process_time(self):
        buffer = Buffer(1)
        requests = [ Request(0, -1) ]
        with self.assertRaisesRegex(AssertionError, ''):
            process_requests(requests, buffer)

    def test_preceeding_lower_bound_of_process_time_among_requests(self):
        buffer = Buffer(1)
        requests = [ Request(0, 0), Request(0, -1), Request(0, 0) ]
        with self.assertRaisesRegex(AssertionError, ''):
            process_requests(requests, buffer)

    def test_misordered_arrival_times(self):
        buffer = Buffer(1)
        requests = [ Request(1, 0), Request(0, 0), Request(2, 0) ]
        with self.assertRaisesRegex(AssertionError, ''):
            process_requests(requests, buffer)

class ProcessPackagesWithBufferSizeAsOneTestCase(unittest.TestCase):

    def setUp(self):
        self.buffer = Buffer(1)

    def tearDown(self):
        pass

    def test_no_requests_and_buffer_size_as_1(self):
        assert_no_requests_and_buffer_size_as(self, 1)

    def test_one_request_as_0_0(self):
        requests = [ Request(0, 0) ]
        responses = process_requests(requests, self.buffer)
        assert_responses(self, [ Response(False, 0) ], responses)

    def test_one_request_as_0_1(self):
        requests = [ Request(0, 1) ]
        responses = process_requests(requests, self.buffer)
        assert_responses(self, [ Response(False, 0) ], responses)

    def test_one_request_as_1_0(self):
        requests = [ Request(1, 0) ]
        responses = process_requests(requests, self.buffer)
        assert_responses(self, [ Response(False, 1) ], responses)

    def test_one_request_as_1_1(self):
        requests = [ Request(1, 1) ]
        responses = process_requests(requests, self.buffer)
        assert_responses(self, [ Response(False, 1) ], responses)

    def test_two_equal_requests_as_0_0(self):
        requests = [ Request(0, 0), Request(0, 0) ]
        responses = process_requests(requests, self.buffer)
        assert_responses(self,
            [ Response(False, 0), Response(False, 0) ],
            responses)

    def test_two_equal_requests_as_0_1(self):
        requests = [ Request(0, 1), Request(0, 1) ]
        responses = process_requests(requests, self.buffer)
        assert_responses(self,
            [ Response(False, 0), Response(True, -1) ],
            responses)

    def test_two_requests_as_0_0_and_0_1(self):
        requests = [ Request(0, 0), Request(0, 1) ]
        responses = process_requests(requests, self.buffer)
        assert_responses(self,
            [ Response(False, 0), Response(False, 0) ],
            responses)

    def test_two_requests_as_0_1_and_0_0(self):
        requests = [ Request(0, 1), Request(0, 0) ]
        responses = process_requests(requests, self.buffer)
        assert_responses(self,
            [ Response(False, 0), Response(True, -1) ],
            responses)

    def test_two_requests_as_0_1_and_0_1(self):
        requests = [ Request(0, 1), Request(0, 1) ]
        responses = process_requests(requests, self.buffer)
        assert_responses(self,
            [ Response(False, 0), Response(True, -1) ],
            responses)

    def test_two_requests_as_0_1_and_1_1(self):
        requests = [ Request(0, 1), Request(1, 1) ]
        responses = process_requests(requests, self.buffer)
        assert_responses(self,
            [ Response(False, 0), Response(False, 1) ],
            responses)

    def test_two_requests_as_0_1_and_2_1(self):
        requests = [ Request(0, 1), Request(2, 1) ]
        responses = process_requests(requests, self.buffer)
        assert_responses(self,
            [ Response(False, 0), Response(False, 2) ],
            responses)

    def test_three_requests_as_0_1_and_1_3_and_4_2(self):
        requests = [ Request(0, 1), Request(1, 3), Request(4, 2) ]
        responses = process_requests(requests, self.buffer)
        assert_responses(self,
            [ Response(False, 0), Response(False, 1), Response(False, 4) ],
            responses)

    def test_three_requests_as_0_2_and_1_4_and_5_3(self):
        requests = [ Request(0, 2), Request(1, 4), Request(5, 3) ]
        responses = process_requests(requests, self.buffer)
        assert_responses(self,
            [ Response(False, 0), Response(True, -1), Response(False, 5) ],
            responses)

class ProcessPackagesWithBufferSizeAsTwoTestCase(unittest.TestCase):

    def setUp(self):
        self.buffer = Buffer(2)

    def tearDown(self):
        pass

    def test_no_requests_and_buffer_size_as_2(self):
        assert_no_requests_and_buffer_size_as(self, 2)

    def test_two_equal_requests_as_0_1(self):
        requests = [ Request(0, 1), Request(0, 1) ]
        responses = process_requests(requests, self.buffer)
        assert_responses(self,
            [ Response(False, 0), Response(False, 1) ],
            responses)

    def test_three_equal_requests_as_0_1(self):
        requests = [ Request(0, 1), Request(0, 1), Request(0, 1) ]
        responses = process_requests(requests, self.buffer)
        assert_responses(self,
            [ Response(False, 0), Response(False, 1), Response(True, -1) ],
            responses)

    def test_three_requests_as_0_2_and_1_4_and_5_3(self):
        requests = [ Request(0, 2), Request(1, 4), Request(5, 3) ]
        responses = process_requests(requests, self.buffer)
        assert_responses(self,
            [ Response(False, 0), Response(False, 2), Response(False, 6) ],
            responses)

    def test_three_requests_as_0_1_and_3_1_and_10_1(self):
        requests = [ Request(0, 1), Request(3, 1), Request(10, 1) ]
        responses = process_requests(requests, self.buffer)
        assert_responses(self,
            [ Response(False, 0), Response(False, 3), Response(False, 10) ],
            responses)

class ProcessPackagesWithBufferSizeAsThreeTestCase(unittest.TestCase):

    def setUp(self):
        self.buffer = Buffer(3)

    def tearDown(self):
        pass

    def test_no_requests_and_buffer_size_as_3(self):
        assert_no_requests_and_buffer_size_as(self, 3)

    def test_six_requests_as_0_2_and_1_2_and_2_2_and_3_2_and_4_2_and_5_2(self):
        requests = [ Request(0, 2), Request(1, 2), Request(2, 2),
            Request(3, 2), Request(4, 2), Request(5, 2) ]
        responses = process_requests(requests, self.buffer)
        assert_responses(self,
            [ Response(False, 0), Response(False, 2), Response(False, 4),
                Response(False, 6), Response(False, 8), Response(True, -1) ],
            responses)

if __name__ == '__main__':
    unittest.main()
