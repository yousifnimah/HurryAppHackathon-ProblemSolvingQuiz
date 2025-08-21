# Sorting Algorithm & Frame Analyzer

This program demonstrates:
1. **Merge Sort implementation** (without using Python's built-in `sorted()`).
2. A **FrameAnalyzer class** that detects missing frames, gaps, and the longest gap from a list of integer frames.

---

## Merge Sort

The `merge_sort` function recursively splits a list into two halves, sorts each half, and then merges them back together.

```python
def merge_sort(arr: list[int]) -> list[int]:
    if len(arr) <= 1:  # stop when only one element is left
        return arr

    # splitting the list into two parts from the middle
    mid = len(arr) // 2
    # recursively sort left and right halves
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    merged_arr = []
    i = j = 0

    # merge step: compare elements and append smaller one
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged_arr.append(left[i])
            i += 1
        else:
            merged_arr.append(right[j])
            j += 1

    # append remaining elements
    merged_arr.extend(left[i:])
    merged_arr.extend(right[j:])
    return merged_arr
```

⚡ **Complexity:**  
- Time: `O(n log n)`  
- Space: `O(n)`  

---

## FrameAnalyzer Class

`FrameAnalyzer` takes a list of integer frames, sorts them (using our custom `merge_sort`), and analyzes gaps in the sequence.

```python
class FrameAnalyzer:
    def __init__(self, frames: list[int]):
        self.frames = frames
        self.report = {
            "gaps": [],
            "longest_gap": [],
            "missing_count": 0,
        }

    def find_missing_frames(self):
        frames = self.frames
        sorted_frames = self.resort_frames_manually()

        longest_gap_size = 0
        for i in range(len(sorted_frames)):
            if i < len(sorted_frames) - 1 and sorted_frames[i+1] - sorted_frames[i] > 1:
                gap_start = sorted_frames[i]
                gap_end = sorted_frames[i+1]
                gap_range = [gap_start, gap_end]
                gap_size = gap_end - gap_start

                self.report["gaps"].append(gap_range)
                self.report["missing_count"] += gap_size

                if gap_size > longest_gap_size:
                    longest_gap_size = gap_size
                    self.report["longest_gap"] = gap_range

    def get_report(self):
        return self.report

    def resort_frames_manually(self):
        return merge_sort(self.frames)

    def __lt__(self, other):
        return self.frames >= other.frames
```

---

## Example Usage

```python
# main program
frameAnalyzer = FrameAnalyzer([1, 2, 3, 5, 6, 10, 11, 16])
frameAnalyzer.find_missing_frames()
report = frameAnalyzer.get_report()

app_name = " FrameAnalyzer - Full Report "
output_msg = f'{"="*30}{app_name}{"="*30}\n{report}\n{"="*(60+len(app_name))}'
print(output_msg)
```

### ✅ Output:
```
============================== FrameAnalyzer - Full Report ==============================
{'gaps': [[3, 5], [6, 10], [11, 16]], 'longest_gap': [11, 16], 'missing_count': 11}
=========================================================================================
```

---

## Notes
- Sorting is done **manually** using Merge Sort, not Python's built-in `sorted()`.
- The analyzer can be extended to detect duplicate frames, out-of-order frames, or perform statistical analysis on gaps.
- This implementation is for **educational purposes** to demonstrate recursion, sorting, and simple data analysis.
