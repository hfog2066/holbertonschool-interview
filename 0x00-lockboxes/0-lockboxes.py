#!/usr/bin/python3

def canUnlockAll(boxes):
    if len(boxes) == 0:
        return False

    opened_boxes = [0, ]
    number_of_boxes = len(boxes) - 1

    for box in boxes:
        if len(box) == 0:
            return False
        for key in box:
            if key > 0 and key <= number_of_boxes:
                if key in opened_boxes:
                    continue
                else:
                    opened_boxes.append(key)
                    if len(opened_boxes) == len(boxes):
                        return True
    return False
