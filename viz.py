import cv2
import numpy as np


def vis_blur(img, boxes, scores, kernel_size=191, conf=0.5):

    for i in range(len(boxes)):
        box = boxes[i]
        score = scores[i]
        if score < conf:
            continue
        x0 = int(box[0])
        y0 = int(box[1])
        x1 = int(box[2])
        y1 = int(box[3])
        w = abs(x1 - x0)
        h = abs(y1 - y0)

        mask_area = img[y0 : y0 + h, x0 : x0 + w]

        if mask_area.shape[0] > 0 and mask_area.shape[1] > 0:
            blurred = cv2.GaussianBlur(mask_area, (kernel_size, kernel_size), 0)
            img[y0 : y0 + h, x0 : x0 + w] = blurred

    return img


def vis_blacken(img, boxes, scores, kernel_size=191, conf=0.5):

    for i in range(len(boxes)):
        box = boxes[i]
        score = scores[i]
        if score < conf:
            continue
        x0 = int(box[0])
        y0 = int(box[1])
        x1 = int(box[2])
        y1 = int(box[3])
        w = abs(x1 - x0)
        h = abs(y1 - y0)

        mask_area = img[y0 : y0 + h, x0 : x0 + w]

        if mask_area.shape[0] > 0 and mask_area.shape[1] > 0:
            img[y0 : y0 + h, x0 : x0 + w] = 0

    return img


def vis_noisen(img, boxes, scores, conf=0.5):
    for i in range(len(boxes)):
        box = boxes[i]
        score = scores[i]
        if score < conf:
            continue
        x0 = int(box[0])
        y0 = int(box[1])
        x1 = int(box[2])
        y1 = int(box[3])
        w = abs(x1 - x0)
        h = abs(y1 - y0)

        mask_area = img[y0 : y0 + h, x0 : x0 + w]

        if mask_area.shape[0] > 0 and mask_area.shape[1] > 0:
            blurred = np.random.randint(
                255, size=(mask_area.shape[0], mask_area.shape[1], 3), dtype=np.uint8
            )
            img[y0 : y0 + h, x0 : x0 + w] = blurred

    return img


def vis_overlay(img, overlay_img, boxes, scores, conf=0.5):
    for i in range(len(boxes)):
        box = boxes[i]
        score = scores[i]
        if score < conf:
            continue
        x0 = int(box[0])
        y0 = int(box[1])
        x1 = int(box[2])
        y1 = int(box[3])
        w = abs(x1 - x0)
        h = abs(y1 - y0)

        mask_area = img[y0 : y0 + h, x0 : x0 + w]

        if mask_area.shape[0] > 0 and mask_area.shape[1] > 0:
            o_copy = overlay_img.copy()
            resized = cv2.resize(
                o_copy,
                (mask_area.shape[1], mask_area.shape[0]),
                interpolation=cv2.INTER_AREA,
            )

            img[y0 : y0 + h, x0 : x0 + w] = resized

    return img
