#!/usr/bin/env python
label_index = 0
for i in range(width):
    for j in range(height):
        compressd_img[i][j] = compressed_paltette[cluster_assignments[label_index]]
        label_index += 1



cv2.imshow('cat', compressd_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
if __name__ == '__main__':
    pass