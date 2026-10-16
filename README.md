# First_CI_Pipeline

A Continuous Integration (CI) pipeline built with GitHub Actions, Python and pytest.

Every push to `main` automatically installs the requirements and runs all test cases. A green tick means every test passed.

## Programs (21 to 30)

| No. | Program | Function |
|-----|---------|----------|
| 21 | Largest word in a sentence | `largest_word(sentence)` |
| 22 | Check anagram strings | `is_anagram(first, second)` |
| 23 | Sort a list without `sort()` | `bubble_sort(numbers)` |
| 24 | Merge two sorted lists | `merge_sorted_lists(list1, list2)` |
| 25 | Maximum and minimum in a list | `find_max_min(numbers)` |
| 26 | Sum of list elements | `sum_of_list(numbers)` |
| 27 | Rotate a list by K positions | `rotate_list(items, k)` |
| 28 | Intersection of two sets | `set_intersection(first, second)` |
| 29 | Check Armstrong number | `is_armstrong(number)` |
| 30 | Decimal to binary without `bin()` | `decimal_to_binary(number)` |

## Project structure

```
First_CI_Pipeline/
|-- .github/workflows/python-ci.yml   # GitHub Actions workflow
|-- codes/                            # Python programs
|-- test_cases/                       # pytest test files
|-- pytest.ini
|-- requirements.txt
`-- README.md
```

## Run locally

```
git clone https://github.com/YOUR-USERNAME/First_CI_Pipeline.git
cd First_CI_Pipeline
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
pytest -v
```

## CI workflow

The workflow in `.github/workflows/python-ci.yml` runs on every push and pull request to `main`:

1. Check out the code
2. Set up Python 3.12
3. Install dependencies from `requirements.txt`
4. Run `pytest`
