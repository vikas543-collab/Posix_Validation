import posix
import time
import logging

logging.basicConfig()
logger = logging.getLogger('logger')


def verify_file_accessibility():
    handle = posix.open("Alphabets", 2)
    if not handle > 0:
        assert "File not accessible"
    else:
        print("File accessibility validated")


def verify_if_file_content_retrieved():
    handle = posix.open("Alphabets", 2)
    chars_to_be_retrieved = 1

    if len(posix.read(handle, chars_to_be_retrieved)) > 0:
        print("File content retrieval validated")
    else:
        logger.error("File content retrieval failed")


def verify_if_offset_increase_post_read():
    handle = posix.open("Alphabets", 2)
    chars_to_be_retrieved = 2
    new_chars_to_be_retrieved = chars_to_be_retrieved + 1
    check = posix.read(handle, chars_to_be_retrieved) != posix.read(handle, new_chars_to_be_retrieved)
    if check:
        print("File offset increase validated")
    else:
        logger.error("File offset increase failed")


def verify_retrieval_with_negative_numbers():
    handle = posix.open("Alphabets", 2)
    chars_to_be_retrieved = -1
    try:
        posix.read(handle, chars_to_be_retrieved)
    except Exception as e:
        print("Characters to be retrieved cannot be negative")


#  Upper limit for 32 bit machine is 2 ^ 31

def verify_upper_bound_edge_case():
    handle = posix.open("Alphabets", 2)
    chars_to_be_retrieved = 2 ** 31 - 1

    if len(posix.read(handle, chars_to_be_retrieved)) > 0:
        print("Read validated till 2 ^ 31 - 1")
    else:
        logger.error("Read not working for large numbers ")


def verify_retrieval_above_max_limit_not_allowed():
    handle = posix.open("Alphabets", 2)
    chars_to_be_retrieved = 2 ** 31
    try:
        posix.read(handle, chars_to_be_retrieved)
    except:
        logger.error("Overflow error")


def verify_response_time():
    start_time = time.time()
    handle = posix.open("Large_Text", 2)
    chars_to_be_retrieved = 100000
    posix.read(handle, chars_to_be_retrieved)
    end_time = time.time()
    print("Time to read file large file " + str(end_time - start_time))
    if end_time - start_time < 0.1:
        print("Response time validated")
    else:
        logger.error("Response time validation failed")

# Tests


verify_file_accessibility()
verify_if_file_content_retrieved()
verify_if_offset_increase_post_read()

# Edge case test

verify_upper_bound_edge_case()

# Negative tests
verify_retrieval_with_negative_numbers()
verify_retrieval_above_max_limit_not_allowed()

# NFR
verify_response_time()