## Tests to validate Posix Read operation

## Problem Statement

Posix read operation fetches specificed count bytes from file descriptor. Detailed readme : http://man7.org/linux/man-pages/man2/read.2.html
  
  - Add test to verify if "Read" operations are working as expected
  - Check edge cases
  - Verify maximum allowed count in read operation
  
## Tests

```
verify_file_accessibility()
verify_if_file_content_retrieved()
verify_if_offset_increase_post_read()
```

## Edge case test
```
verify_upper_bound_edge_case()
```

## Negative tests

```
verify_retrieval_with_negative_numbers()
verify_retrieval_above_max_limit_not_allowed()
```

## NFR
```
verify_response_time()
```

