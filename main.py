# sorting algorithm
def merge_sort(arr:list[int]) -> list[int]:
    if len(arr) <= 1: # to stop recursive calls ends with one node
        return arr

    # splitting the list into two parts from the middle
    mid = len(arr) // 2
    # recursively compare mid-left with mid-right
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    merged_arr = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged_arr.append(left[i])
            i += 1
        else:
            merged_arr.append(right[j])
            j += 1

    # just to append the rest
    merged_arr.extend(left[i:])
    merged_arr.extend(right[j:])
    return merged_arr

# ========= Defining a class with name FrameAnalyzer
class FrameAnalyzer:
    # constructor definition passing frames list of integers
    def __init__(self, frames:list[int]):
        self.frames = frames #assiging frames
        #initialize the frame analyzer report
        self.report = {
            "gaps": [],
            "longest_gap": [],
            "missing_count": 0,
        }

    def find_missing_frames(self):
        frames = self.frames
        # sorted_frames = sorted(frames) --> we can use this or the below statement for sorting
        sorted_frames = self.resort_frames_manually()

        longest_gap_size = 0
        for i in range(len(sorted_frames)):
            # identifying the gap by comparing frame with the next frame
            if i < len(sorted_frames) - 1 and sorted_frames[i+1] - sorted_frames[i] > 1:
                gap_start = sorted_frames[i] # gap start indicator
                gap_end = sorted_frames[i+1] # gap end indicator
                gap_range = [gap_start+1, gap_end-1] # setting gap range
                gap_size = self.calc_gap_size(gap_range) # calculating the gap size

                self.report["gaps"].append(gap_range) # adding gap range to the report
                self.report["missing_count"] += gap_size # increasing the missing counts

                #finding the longest gap size
                if gap_size > longest_gap_size:
                    longest_gap_size = gap_size
                    self.report["longest_gap"] = gap_range

    def get_report(self):
        return self.report

    # resorting frames manually without O(n log(n)), so we can use it effectively
    def resort_frames_manually(self):
        return merge_sort(self.frames) #using merge sort algorithm

    # calculate the gap size
    def calc_gap_size(self, gap_range):
        return gap_range[1] - gap_range[0] + 1


    # using magic function to resort the frames with no built-in function; much cleaner
    def __lt__(self, other):
        return self.frames >= other.frames


# main program
frameAnalyzer = FrameAnalyzer([1, 2, 3, 5, 6, 10, 11, 16, 19]) # initiate FrameAnalyzer instance
frameAnalyzer.find_missing_frames() #finding missing frames
report = frameAnalyzer.get_report()

app_name = " FrameAnalyzer - Full Report "
output_msg = f"{"="* 30}{app_name}{"="*30}\n{report}\n{"="*(60+len(app_name))}"
print(output_msg)
