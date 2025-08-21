# test_frame_analyzer.py
import unittest

def merge_sort(arr:list[int]) -> list[int]:
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    merged_arr = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged_arr.append(left[i]); i += 1
        else:
            merged_arr.append(right[j]); j += 1
    merged_arr.extend(left[i:])
    merged_arr.extend(right[j:])
    return merged_arr

class FrameAnalyzer:
    def __init__(self, frames:list[int]):
        self.frames = frames
        self.report = {
            "gaps": [],
            "longest_gap": [],
            "missing_count": 0,
        }

    def find_missing_frames(self):
        sorted_frames = self.resort_frames_manually()
        longest_gap_size = 0
        for i in range(len(sorted_frames)):
            if i < len(sorted_frames) - 1 and sorted_frames[i+1] - sorted_frames[i] > 1:
                gap_start = sorted_frames[i]
                gap_end = sorted_frames[i+1]
                gap_range = [gap_start+1, gap_end-1]
                gap_size = self.calc_gap_size(gap_range)
                self.report["gaps"].append(gap_range)
                self.report["missing_count"] += gap_size
                if gap_size > longest_gap_size:
                    longest_gap_size = gap_size
                    self.report["longest_gap"] = gap_range

    def get_report(self):
        return self.report

    def resort_frames_manually(self):
        return merge_sort(self.frames)

    def calc_gap_size(self, gap_range):
        return gap_range[1] - gap_range[0] + 1

    def __lt__(self, other):
        # Note: This comparison is unusual (reversed logic).
        return self.frames >= other.frames


# ===== Unit Tests =====
class TestMergeSort(unittest.TestCase):
    def test_basic_sort(self):
        self.assertEqual(merge_sort([3,1,4,1,5,9]), [1,1,3,4,5,9])

    def test_already_sorted(self):
        self.assertEqual(merge_sort([1,2,3,4]), [1,2,3,4])

    def test_with_duplicates(self):
        self.assertEqual(merge_sort([2,2,2,1,1,3]), [1,1,2,2,2,3])

    def test_with_negatives(self):
        self.assertEqual(merge_sort([0,-1,5,-10,3]), [-10,-1,0,3,5])

    def test_empty_and_singleton(self):
        self.assertEqual(merge_sort([]), [])
        self.assertEqual(merge_sort([42]), [42])


class TestFrameAnalyzer(unittest.TestCase):
    def test_report_with_gaps(self):
        fa = FrameAnalyzer([1, 2, 3, 5, 6, 10, 11, 16])
        fa.find_missing_frames()
        report = fa.get_report()
        self.assertEqual(report["gaps"], [[4,4],[7,9],[12,15]])
        self.assertEqual(report["longest_gap"], [12,15])
        self.assertEqual(report["missing_count"], 8)

    def test_no_gaps(self):
        fa = FrameAnalyzer([5,6,7,8,9])
        fa.find_missing_frames()
        report = fa.get_report()
        self.assertEqual(report["gaps"], [])
        self.assertEqual(report["longest_gap"], [])
        self.assertEqual(report["missing_count"], 0)

    def test_unsorted_input(self):
        fa = FrameAnalyzer([10, 7, 8, 9, 5, 6])
        fa.find_missing_frames()
        report = fa.get_report()
        self.assertEqual(report["gaps"], [])
        self.assertEqual(report["missing_count"], 0)

    def test_calc_gap_size(self):
        fa = FrameAnalyzer([1,3])
        self.assertEqual(fa.calc_gap_size([4,4]), 1)
        self.assertEqual(fa.calc_gap_size([7,9]), 3)

    def test_resort_frames_manually(self):
        fa = FrameAnalyzer([3,2,1,4])
        self.assertEqual(fa.resort_frames_manually(), [1,2,3,4])


if __name__ == "__main__":
    unittest.main()
