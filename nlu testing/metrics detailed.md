## NLU parser
===  Total performance ===
authors {'TP': 951, 'FP': 177, 'FN': 193, 'TN': 615001, 'Precision': 0.843, 'Recall': 0.831, 'F1': 0.837, 'Accuracy': 0.999}
intent {'TP': 3069, 'FP': 132, 'FN': 132, 'TN': 25476, 'Precision': 0.959, 'Recall': 0.959, 'F1': 0.959, 'Accuracy': 0.991}
free_text {'TP': 0, 'FP': 859, 'FN': 0, 'TN': 703521, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.999}
similar_to_authors {'TP': 0, 'FP': 27, 'FN': 0, 'TN': 473, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.946}
pages_max {'TP': 241, 'FP': 11, 'FN': 37, 'TN': 63602, 'Precision': 0.956, 'Recall': 0.867, 'F1': 0.909, 'Accuracy': 0.999}
pages_min {'TP': 246, 'FP': 11, 'FN': 32, 'TN': 63271, 'Precision': 0.957, 'Recall': 0.885, 'F1': 0.92, 'Accuracy': 0.999}
categories {'TP': 721, 'FP': 517, 'FN': 597, 'TN': 369577, 'Precision': 0.582, 'Recall': 0.547, 'F1': 0.564, 'Accuracy': 0.997}
languages {'TP': 377, 'FP': 56, 'FN': 49, 'TN': 5230, 'Precision': 0.871, 'Recall': 0.885, 'F1': 0.878, 'Accuracy': 0.982}
series {'TP': 324, 'FP': 23, 'FN': 438, 'TN': 132659, 'Precision': 0.934, 'Recall': 0.425, 'F1': 0.584, 'Accuracy': 0.997}
themes {'TP': 109, 'FP': 597, 'FN': 187, 'TN': 210955, 'Precision': 0.154, 'Recall': 0.368, 'F1': 0.218, 'Accuracy': 0.996}
moods {'TP': 28, 'FP': 417, 'FN': 239, 'TN': 56548, 'Precision': 0.063, 'Recall': 0.105, 'F1': 0.079, 'Accuracy': 0.989}
books {'TP': 0, 'FP': 0, 'FN': 527, 'TN': 172516, 'Precision': -1, 'Recall': 0.0, 'F1': -1, 'Accuracy': 0.997}
similar_to_books {'TP': 405, 'FP': 50, 'FN': 579, 'TN': 528506, 'Precision': 0.89, 'Recall': 0.412, 'F1': 0.563, 'Accuracy': 0.999}
types {'TP': 389, 'FP': 27, 'FN': 38, 'TN': 458, 'Precision': 0.935, 'Recall': 0.911, 'F1': 0.923, 'Accuracy': 0.929}
year_from {'TP': 252, 'FP': 26, 'FN': 43, 'TN': 24639, 'Precision': 0.906, 'Recall': 0.854, 'F1': 0.88, 'Accuracy': 0.997}
year_to {'TP': 244, 'FP': 18, 'FN': 51, 'TN': 21177, 'Precision': 0.931, 'Recall': 0.827, 'F1': 0.876, 'Accuracy': 0.997}
periods {'TP': 333, 'FP': 102, 'FN': 116, 'TN': 1304, 'Precision': 0.766, 'Recall': 0.742, 'F1': 0.753, 'Accuracy': 0.882}
publishers {'TP': 398, 'FP': 18, 'FN': 279, 'TN': 80656, 'Precision': 0.957, 'Recall': 0.588, 'F1': 0.728, 'Accuracy': 0.996}
TOTAL {'TP': 8087, 'FP': 3068, 'FN': 3537, 'TN': 3075569, 'Precision': 0.725, 'Recall': 0.696, 'F1': 0.71, 'Accuracy': 0.998}

===  Performance per intent ===

Intent: author_query
authors {'TP': 503, 'FP': 3, 'FN': 76, 'TN': 269408, 'Precision': 0.994, 'Recall': 0.869, 'F1': 0.927, 'Accuracy': 1.0}
intent {'TP': 288, 'FP': 2, 'FN': 2, 'TN': 2318, 'Precision': 0.993, 'Recall': 0.993, 'F1': 0.993, 'Accuracy': 0.998}
free_text {'TP': 0, 'FP': 28, 'FN': 0, 'TN': 22932, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.999}
similar_to_authors {'TP': 0, 'FP': 9, 'FN': 0, 'TN': 116, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.928}
themes {'TP': 0, 'FP': 3, 'FN': 0, 'TN': 361, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.992}
TOTAL {'TP': 791, 'FP': 45, 'FN': 78, 'TN': 295135, 'Precision': 0.946, 'Recall': 0.91, 'F1': 0.928, 'Accuracy': 1.0}

Intent: recommend_book
intent {'TP': 1814, 'FP': 60, 'FN': 60, 'TN': 14932, 'Precision': 0.968, 'Recall': 0.968, 'F1': 0.968, 'Accuracy': 0.993}
pages_max {'TP': 241, 'FP': 11, 'FN': 37, 'TN': 63602, 'Precision': 0.956, 'Recall': 0.867, 'F1': 0.909, 'Accuracy': 0.999}
pages_min {'TP': 246, 'FP': 11, 'FN': 32, 'TN': 63271, 'Precision': 0.957, 'Recall': 0.885, 'F1': 0.92, 'Accuracy': 0.999}
free_text {'TP': 0, 'FP': 508, 'FN': 0, 'TN': 416052, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.999}
categories {'TP': 721, 'FP': 505, 'FN': 597, 'TN': 366331, 'Precision': 0.588, 'Recall': 0.547, 'F1': 0.567, 'Accuracy': 0.997}
languages {'TP': 377, 'FP': 56, 'FN': 49, 'TN': 5230, 'Precision': 0.871, 'Recall': 0.885, 'F1': 0.878, 'Accuracy': 0.982}
series {'TP': 324, 'FP': 10, 'FN': 438, 'TN': 131504, 'Precision': 0.97, 'Recall': 0.425, 'F1': 0.591, 'Accuracy': 0.997}
themes {'TP': 109, 'FP': 591, 'FN': 187, 'TN': 209505, 'Precision': 0.156, 'Recall': 0.368, 'F1': 0.219, 'Accuracy': 0.996}
moods {'TP': 28, 'FP': 417, 'FN': 239, 'TN': 56548, 'Precision': 0.063, 'Recall': 0.105, 'F1': 0.079, 'Accuracy': 0.989}
types {'TP': 389, 'FP': 27, 'FN': 38, 'TN': 458, 'Precision': 0.935, 'Recall': 0.911, 'F1': 0.923, 'Accuracy': 0.929}
year_from {'TP': 252, 'FP': 25, 'FN': 43, 'TN': 24560, 'Precision': 0.91, 'Recall': 0.854, 'F1': 0.881, 'Accuracy': 0.997}
year_to {'TP': 244, 'FP': 17, 'FN': 51, 'TN': 21108, 'Precision': 0.935, 'Recall': 0.827, 'F1': 0.878, 'Accuracy': 0.997}
periods {'TP': 333, 'FP': 101, 'FN': 116, 'TN': 1300, 'Precision': 0.767, 'Recall': 0.742, 'F1': 0.754, 'Accuracy': 0.883}
authors {'TP': 448, 'FP': 97, 'FN': 117, 'TN': 287948, 'Precision': 0.822, 'Recall': 0.793, 'F1': 0.807, 'Accuracy': 0.999}
publishers {'TP': 398, 'FP': 18, 'FN': 279, 'TN': 80656, 'Precision': 0.957, 'Recall': 0.588, 'F1': 0.728, 'Accuracy': 0.996}
similar_to_books {'TP': 0, 'FP': 5, 'FN': 0, 'TN': 4560, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.999}
similar_to_authors {'TP': 0, 'FP': 3, 'FN': 0, 'TN': 47, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.94}
TOTAL {'TP': 5924, 'FP': 2462, 'FN': 2283, 'TN': 1747612, 'Precision': 0.706, 'Recall': 0.722, 'F1': 0.714, 'Accuracy': 0.997}

Intent: book_query
books {'TP': 0, 'FP': 0, 'FN': 527, 'TN': 172516, 'Precision': -1, 'Recall': 0.0, 'F1': -1, 'Accuracy': 0.997}
authors {'TP': 0, 'FP': 51, 'FN': 0, 'TN': 38120, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.999}
intent {'TP': 333, 'FP': 18, 'FN': 18, 'TN': 2790, 'Precision': 0.949, 'Recall': 0.949, 'F1': 0.949, 'Accuracy': 0.989}
free_text {'TP': 0, 'FP': 229, 'FN': 0, 'TN': 187551, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.999}
categories {'TP': 0, 'FP': 1, 'FN': 0, 'TN': 361, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.997}
themes {'TP': 0, 'FP': 1, 'FN': 0, 'TN': 363, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.997}
similar_to_authors {'TP': 0, 'FP': 1, 'FN': 0, 'TN': 24, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.96}
similar_to_books {'TP': 0, 'FP': 6, 'FN': 0, 'TN': 3646, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.998}
series {'TP': 0, 'FP': 1, 'FN': 0, 'TN': 291, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.997}
year_from {'TP': 0, 'FP': 1, 'FN': 0, 'TN': 79, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.988}
year_to {'TP': 0, 'FP': 1, 'FN': 0, 'TN': 69, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.986}
periods {'TP': 0, 'FP': 1, 'FN': 0, 'TN': 4, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.8}
TOTAL {'TP': 333, 'FP': 311, 'FN': 545, 'TN': 405814, 'Precision': 0.517, 'Recall': 0.379, 'F1': 0.438, 'Accuracy': 0.998}

Intent: feedback_like
similar_to_books {'TP': 5, 'FP': 1, 'FN': 134, 'TN': 94812, 'Precision': 0.833, 'Recall': 0.036, 'F1': 0.069, 'Accuracy': 0.999}
intent {'TP': 120, 'FP': 9, 'FN': 9, 'TN': 1023, 'Precision': 0.93, 'Recall': 0.93, 'F1': 0.93, 'Accuracy': 0.984}
free_text {'TP': 0, 'FP': 7, 'FN': 0, 'TN': 5733, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.999}
series {'TP': 0, 'FP': 1, 'FN': 0, 'TN': 291, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.997}
categories {'TP': 0, 'FP': 3, 'FN': 0, 'TN': 359, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.992}
authors {'TP': 0, 'FP': 1, 'FN': 0, 'TN': 930, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.999}
TOTAL {'TP': 125, 'FP': 22, 'FN': 143, 'TN': 103148, 'Precision': 0.85, 'Recall': 0.466, 'F1': 0.602, 'Accuracy': 0.998}

Intent: similar_book
similar_to_books {'TP': 395, 'FP': 38, 'FN': 316, 'TN': 329757, 'Precision': 0.912, 'Recall': 0.556, 'F1': 0.691, 'Accuracy': 0.999}
intent {'TP': 361, 'FP': 1, 'FN': 1, 'TN': 2895, 'Precision': 0.997, 'Recall': 0.997, 'F1': 0.997, 'Accuracy': 0.999}
similar_to_authors {'TP': 0, 'FP': 14, 'FN': 0, 'TN': 286, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.953}
categories {'TP': 0, 'FP': 6, 'FN': 0, 'TN': 1804, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.997}
free_text {'TP': 0, 'FP': 16, 'FN': 0, 'TN': 13104, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.999}
authors {'TP': 0, 'FP': 24, 'FN': 0, 'TN': 17665, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.999}
themes {'TP': 0, 'FP': 1, 'FN': 0, 'TN': 363, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.997}
series {'TP': 0, 'FP': 10, 'FN': 0, 'TN': 282, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.966}
TOTAL {'TP': 756, 'FP': 110, 'FN': 317, 'TN': 366156, 'Precision': 0.873, 'Recall': 0.705, 'F1': 0.78, 'Accuracy': 0.999}

Intent: feedback_dislike
similar_to_books {'TP': 5, 'FP': 0, 'FN': 129, 'TN': 95731, 'Precision': 1.0, 'Recall': 0.037, 'F1': 0.072, 'Accuracy': 0.999}
free_text {'TP': 0, 'FP': 58, 'FN': 0, 'TN': 47502, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.999}
intent {'TP': 120, 'FP': 0, 'FN': 0, 'TN': 960, 'Precision': 1.0, 'Recall': 1.0, 'F1': 1.0, 'Accuracy': 1.0}
series {'TP': 0, 'FP': 1, 'FN': 0, 'TN': 291, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.997}
authors {'TP': 0, 'FP': 1, 'FN': 0, 'TN': 930, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.999}
TOTAL {'TP': 125, 'FP': 60, 'FN': 129, 'TN': 145414, 'Precision': 0.676, 'Recall': 0.492, 'F1': 0.569, 'Accuracy': 0.999}

Intent: clarification_answer
intent {'TP': 13, 'FP': 23, 'FN': 23, 'TN': 265, 'Precision': 0.361, 'Recall': 0.361, 'F1': 0.361, 'Accuracy': 0.858}
free_text {'TP': 0, 'FP': 11, 'FN': 0, 'TN': 9009, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.999}
categories {'TP': 0, 'FP': 2, 'FN': 0, 'TN': 722, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.997}
themes {'TP': 0, 'FP': 1, 'FN': 0, 'TN': 363, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.997}
TOTAL {'TP': 13, 'FP': 37, 'FN': 23, 'TN': 10359, 'Precision': 0.26, 'Recall': 0.361, 'F1': 0.302, 'Accuracy': 0.994}

Intent: unknown
intent {'TP': 6, 'FP': 19, 'FN': 19, 'TN': 181, 'Precision': 0.24, 'Recall': 0.24, 'F1': 0.24, 'Accuracy': 0.831}
free_text {'TP': 0, 'FP': 2, 'FN': 0, 'TN': 1638, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.999}
TOTAL {'TP': 6, 'FP': 21, 'FN': 19, 'TN': 1819, 'Precision': 0.222, 'Recall': 0.24, 'F1': 0.231, 'Accuracy': 0.979}

Intent: greeting
intent {'TP': 14, 'FP': 0, 'FN': 0, 'TN': 112, 'Precision': 1.0, 'Recall': 1.0, 'F1': 1.0, 'Accuracy': 1.0}
TOTAL {'TP': 14, 'FP': 0, 'FN': 0, 'TN': 112, 'Precision': 1.0, 'Recall': 1.0, 'F1': 1.0, 'Accuracy': 1.0}



## Rule-based parser
===  Total performance ===
authors {'TP': 0, 'FP': 0, 'FN': 1144, 'TN': 490744, 'Precision': -1, 'Recall': 0.0, 'F1': -1, 'Accuracy': 0.998}
intent {'TP': 1702, 'FP': 1499, 'FN': 1499, 'TN': 24109, 'Precision': 0.532, 'Recall': 0.532, 'F1': 0.532, 'Accuracy': 0.896}
free_text {'TP': 0, 'FP': 3201, 'FN': 0, 'TN': 10243200, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 1.0}
raw_utterance {'TP': 0, 'FP': 3201, 'FN': 0, 'TN': 10243200, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 1.0}
themes {'TP': 40, 'FP': 135, 'FN': 256, 'TN': 4123, 'Precision': 0.229, 'Recall': 0.135, 'F1': 0.17, 'Accuracy': 0.914}
pages_min {'TP': 0, 'FP': 0, 'FN': 278, 'TN': 61716, 'Precision': -1, 'Recall': 0.0, 'F1': -1, 'Accuracy': 0.996}
pages_max {'TP': 125, 'FP': 1, 'FN': 153, 'TN': 61715, 'Precision': 0.992, 'Recall': 0.45, 'F1': 0.619, 'Accuracy': 0.998}
categories {'TP': 0, 'FP': 0, 'FN': 1318, 'TN': 300952, 'Precision': -1, 'Recall': 0.0, 'F1': -1, 'Accuracy': 0.996}
languages {'TP': 72, 'FP': 18, 'FN': 354, 'TN': 4622, 'Precision': 0.8, 'Recall': 0.169, 'F1': 0.279, 'Accuracy': 0.927}
series {'TP': 0, 'FP': 0, 'FN': 762, 'TN': 129702, 'Precision': -1, 'Recall': 0.0, 'F1': -1, 'Accuracy': 0.994}
books {'TP': 0, 'FP': 0, 'FN': 527, 'TN': 172516, 'Precision': -1, 'Recall': 0.0, 'F1': -1, 'Accuracy': 0.997}
similar_to_books {'TP': 0, 'FP': 0, 'FN': 984, 'TN': 501496, 'Precision': -1, 'Recall': 0.0, 'F1': -1, 'Accuracy': 0.998}
types {'TP': 147, 'FP': 0, 'FN': 280, 'TN': 434, 'Precision': 1.0, 'Recall': 0.344, 'F1': 0.512, 'Accuracy': 0.675}
year_from {'TP': 127, 'FP': 0, 'FN': 168, 'TN': 20650, 'Precision': 1.0, 'Recall': 0.431, 'F1': 0.602, 'Accuracy': 0.992}
year_to {'TP': 127, 'FP': 0, 'FN': 168, 'TN': 18290, 'Precision': 1.0, 'Recall': 0.431, 'F1': 0.602, 'Accuracy': 0.991}
periods {'TP': 0, 'FP': 0, 'FN': 449, 'TN': 1021, 'Precision': -1, 'Recall': 0.0, 'F1': -1, 'Accuracy': 0.695}
moods {'TP': 40, 'FP': 0, 'FN': 227, 'TN': 1068, 'Precision': 1.0, 'Recall': 0.15, 'F1': 0.261, 'Accuracy': 0.83}
publishers {'TP': 0, 'FP': 0, 'FN': 677, 'TN': 79846, 'Precision': -1, 'Recall': 0.0, 'F1': -1, 'Accuracy': 0.992}
TOTAL {'TP': 2380, 'FP': 8055, 'FN': 9244, 'TN': 22359404, 'Precision': 0.228, 'Recall': 0.205, 'F1': 0.216, 'Accuracy': 0.999}

===  Performance per intent ===

Intent: author_query
authors {'TP': 0, 'FP': 0, 'FN': 579, 'TN': 250561, 'Precision': -1, 'Recall': 0.0, 'F1': -1, 'Accuracy': 0.998}
intent {'TP': 0, 'FP': 290, 'FN': 290, 'TN': 2030, 'Precision': 0.0, 'Recall': 0.0, 'F1': -1, 'Accuracy': 0.778}
free_text {'TP': 0, 'FP': 290, 'FN': 0, 'TN': 928000, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 1.0}
raw_utterance {'TP': 0, 'FP': 290, 'FN': 0, 'TN': 928000, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 1.0}
themes {'TP': 0, 'FP': 4, 'FN': 0, 'TN': 40, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.909}
TOTAL {'TP': 0, 'FP': 874, 'FN': 869, 'TN': 2108631, 'Precision': 0.0, 'Recall': 0.0, 'F1': -1, 'Accuracy': 0.999}

Intent: recommend_book
pages_min {'TP': 0, 'FP': 0, 'FN': 278, 'TN': 61716, 'Precision': -1, 'Recall': 0.0, 'F1': -1, 'Accuracy': 0.996}
intent {'TP': 1661, 'FP': 213, 'FN': 213, 'TN': 14779, 'Precision': 0.886, 'Recall': 0.886, 'F1': 0.886, 'Accuracy': 0.975}
free_text {'TP': 0, 'FP': 1874, 'FN': 0, 'TN': 5996800, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 1.0}
pages_max {'TP': 125, 'FP': 1, 'FN': 153, 'TN': 61715, 'Precision': 0.992, 'Recall': 0.45, 'F1': 0.619, 'Accuracy': 0.998}
raw_utterance {'TP': 0, 'FP': 1874, 'FN': 0, 'TN': 5996800, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 1.0}
categories {'TP': 0, 'FP': 0, 'FN': 1318, 'TN': 300952, 'Precision': -1, 'Recall': 0.0, 'F1': -1, 'Accuracy': 0.996}
languages {'TP': 72, 'FP': 17, 'FN': 354, 'TN': 4606, 'Precision': 0.809, 'Recall': 0.169, 'F1': 0.28, 'Accuracy': 0.927}
series {'TP': 0, 'FP': 0, 'FN': 762, 'TN': 129702, 'Precision': -1, 'Recall': 0.0, 'F1': -1, 'Accuracy': 0.994}
themes {'TP': 40, 'FP': 94, 'FN': 256, 'TN': 3724, 'Precision': 0.299, 'Recall': 0.135, 'F1': 0.186, 'Accuracy': 0.915}
types {'TP': 147, 'FP': 0, 'FN': 280, 'TN': 434, 'Precision': 1.0, 'Recall': 0.344, 'F1': 0.512, 'Accuracy': 0.675}
year_from {'TP': 127, 'FP': 0, 'FN': 168, 'TN': 20650, 'Precision': 1.0, 'Recall': 0.431, 'F1': 0.602, 'Accuracy': 0.992}
year_to {'TP': 127, 'FP': 0, 'FN': 168, 'TN': 18290, 'Precision': 1.0, 'Recall': 0.431, 'F1': 0.602, 'Accuracy': 0.991}
periods {'TP': 0, 'FP': 0, 'FN': 449, 'TN': 1021, 'Precision': -1, 'Recall': 0.0, 'F1': -1, 'Accuracy': 0.695}
moods {'TP': 40, 'FP': 0, 'FN': 227, 'TN': 1068, 'Precision': 1.0, 'Recall': 0.15, 'F1': 0.261, 'Accuracy': 0.83}
authors {'TP': 0, 'FP': 0, 'FN': 565, 'TN': 240183, 'Precision': -1, 'Recall': 0.0, 'F1': -1, 'Accuracy': 0.998}
publishers {'TP': 0, 'FP': 0, 'FN': 677, 'TN': 79846, 'Precision': -1, 'Recall': 0.0, 'F1': -1, 'Accuracy': 0.992}
TOTAL {'TP': 2339, 'FP': 4073, 'FN': 5868, 'TN': 12932286, 'Precision': 0.365, 'Recall': 0.285, 'F1': 0.32, 'Accuracy': 0.999}

Intent: book_query
intent {'TP': 0, 'FP': 351, 'FN': 351, 'TN': 2457, 'Precision': 0.0, 'Recall': 0.0, 'F1': -1, 'Accuracy': 0.778}
free_text {'TP': 0, 'FP': 351, 'FN': 0, 'TN': 1123200, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 1.0}
books {'TP': 0, 'FP': 0, 'FN': 527, 'TN': 172516, 'Precision': -1, 'Recall': 0.0, 'F1': -1, 'Accuracy': 0.997}
raw_utterance {'TP': 0, 'FP': 351, 'FN': 0, 'TN': 1123200, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 1.0}
themes {'TP': 0, 'FP': 14, 'FN': 0, 'TN': 140, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.909}
languages {'TP': 0, 'FP': 1, 'FN': 0, 'TN': 16, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.941}
TOTAL {'TP': 0, 'FP': 1068, 'FN': 878, 'TN': 2421529, 'Precision': 0.0, 'Recall': 0.0, 'F1': -1, 'Accuracy': 0.999}

Intent: feedback_like
intent {'TP': 13, 'FP': 116, 'FN': 116, 'TN': 916, 'Precision': 0.101, 'Recall': 0.101, 'F1': 0.101, 'Accuracy': 0.8}
free_text {'TP': 0, 'FP': 129, 'FN': 0, 'TN': 412800, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 1.0}
similar_to_books {'TP': 0, 'FP': 0, 'FN': 139, 'TN': 91381, 'Precision': -1, 'Recall': 0.0, 'F1': -1, 'Accuracy': 0.998}
raw_utterance {'TP': 0, 'FP': 129, 'FN': 0, 'TN': 412800, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 1.0}
themes {'TP': 0, 'FP': 2, 'FN': 0, 'TN': 20, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.909}
TOTAL {'TP': 13, 'FP': 376, 'FN': 255, 'TN': 917917, 'Precision': 0.033, 'Recall': 0.049, 'F1': 0.04, 'Accuracy': 0.999}

Intent: similar_book
intent {'TP': 0, 'FP': 362, 'FN': 362, 'TN': 2534, 'Precision': 0.0, 'Recall': 0.0, 'F1': -1, 'Accuracy': 0.778}
free_text {'TP': 0, 'FP': 362, 'FN': 0, 'TN': 1158400, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 1.0}
similar_to_books {'TP': 0, 'FP': 0, 'FN': 711, 'TN': 317849, 'Precision': -1, 'Recall': 0.0, 'F1': -1, 'Accuracy': 0.998}
raw_utterance {'TP': 0, 'FP': 362, 'FN': 0, 'TN': 1158400, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 1.0}
themes {'TP': 0, 'FP': 16, 'FN': 0, 'TN': 149, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.903}
TOTAL {'TP': 0, 'FP': 1102, 'FN': 1073, 'TN': 2637332, 'Precision': 0.0, 'Recall': 0.0, 'F1': -1, 'Accuracy': 0.999}

Intent: feedback_dislike
intent {'TP': 0, 'FP': 120, 'FN': 120, 'TN': 840, 'Precision': 0.0, 'Recall': 0.0, 'F1': -1, 'Accuracy': 0.778}
free_text {'TP': 0, 'FP': 120, 'FN': 0, 'TN': 384000, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 1.0}
similar_to_books {'TP': 0, 'FP': 0, 'FN': 134, 'TN': 92266, 'Precision': -1, 'Recall': 0.0, 'F1': -1, 'Accuracy': 0.999}
raw_utterance {'TP': 0, 'FP': 120, 'FN': 0, 'TN': 384000, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 1.0}
themes {'TP': 0, 'FP': 4, 'FN': 0, 'TN': 40, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.909}
TOTAL {'TP': 0, 'FP': 364, 'FN': 254, 'TN': 861146, 'Precision': 0.0, 'Recall': 0.0, 'F1': -1, 'Accuracy': 0.999}

Intent: clarification_answer
intent {'TP': 0, 'FP': 36, 'FN': 36, 'TN': 252, 'Precision': 0.0, 'Recall': 0.0, 'F1': -1, 'Accuracy': 0.778}
free_text {'TP': 0, 'FP': 36, 'FN': 0, 'TN': 115200, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 1.0}
raw_utterance {'TP': 0, 'FP': 36, 'FN': 0, 'TN': 115200, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 1.0}
themes {'TP': 0, 'FP': 1, 'FN': 0, 'TN': 10, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.909}
TOTAL {'TP': 0, 'FP': 109, 'FN': 36, 'TN': 230662, 'Precision': 0.0, 'Recall': 0.0, 'F1': -1, 'Accuracy': 0.999}

Intent: unknown
intent {'TP': 25, 'FP': 0, 'FN': 0, 'TN': 200, 'Precision': 1.0, 'Recall': 1.0, 'F1': 1.0, 'Accuracy': 1.0}
free_text {'TP': 0, 'FP': 25, 'FN': 0, 'TN': 80000, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 1.0}
raw_utterance {'TP': 0, 'FP': 25, 'FN': 0, 'TN': 80000, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 1.0}
TOTAL {'TP': 25, 'FP': 50, 'FN': 0, 'TN': 160200, 'Precision': 0.333, 'Recall': 1.0, 'F1': 0.5, 'Accuracy': 1.0}

Intent: greeting
intent {'TP': 3, 'FP': 11, 'FN': 11, 'TN': 101, 'Precision': 0.214, 'Recall': 0.214, 'F1': 0.214, 'Accuracy': 0.825}
free_text {'TP': 0, 'FP': 14, 'FN': 0, 'TN': 44800, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 1.0}
raw_utterance {'TP': 0, 'FP': 14, 'FN': 0, 'TN': 44800, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 1.0}
TOTAL {'TP': 3, 'FP': 39, 'FN': 11, 'TN': 89701, 'Precision': 0.071, 'Recall': 0.214, 'F1': 0.107, 'Accuracy': 0.999}



## Fuzzy parser
===  Total performance ===
authors {'TP': 28, 'FP': 6, 'FN': 1116, 'TN': 493040, 'Precision': 0.824, 'Recall': 0.024, 'F1': 0.048, 'Accuracy': 0.998}
intent {'TP': 1720, 'FP': 1481, 'FN': 1481, 'TN': 24127, 'Precision': 0.537, 'Recall': 0.537, 'F1': 0.537, 'Accuracy': 0.897}
publishers {'TP': 411, 'FP': 2280, 'FN': 266, 'TN': 414523, 'Precision': 0.153, 'Recall': 0.607, 'F1': 0.244, 'Accuracy': 0.994}
series {'TP': 405, 'FP': 6851, 'FN': 357, 'TN': 878937, 'Precision': 0.056, 'Recall': 0.531, 'F1': 0.101, 'Accuracy': 0.992}
pages_min {'TP': 4, 'FP': 0, 'FN': 274, 'TN': 61716, 'Precision': 1.0, 'Recall': 0.014, 'F1': 0.028, 'Accuracy': 0.996}
pages_max {'TP': 127, 'FP': 1, 'FN': 151, 'TN': 61715, 'Precision': 0.992, 'Recall': 0.457, 'F1': 0.626, 'Accuracy': 0.998}
categories {'TP': 5, 'FP': 26, 'FN': 1313, 'TN': 308890, 'Precision': 0.161, 'Recall': 0.004, 'F1': 0.007, 'Accuracy': 0.996}
languages {'TP': 0, 'FP': 2, 'FN': 426, 'TN': 4434, 'Precision': 0.0, 'Recall': 0.0, 'F1': -1, 'Accuracy': 0.912}
themes {'TP': 106, 'FP': 33, 'FN': 190, 'TN': 1946, 'Precision': 0.763, 'Recall': 0.358, 'F1': 0.487, 'Accuracy': 0.902}
books {'TP': 0, 'FP': 0, 'FN': 527, 'TN': 172516, 'Precision': -1, 'Recall': 0.0, 'F1': -1, 'Accuracy': 0.997}
similar_to_books {'TP': 99, 'FP': 23, 'FN': 885, 'TN': 510609, 'Precision': 0.811, 'Recall': 0.101, 'F1': 0.179, 'Accuracy': 0.998}
types {'TP': 1, 'FP': 0, 'FN': 426, 'TN': 434, 'Precision': 1.0, 'Recall': 0.002, 'F1': 0.005, 'Accuracy': 0.505}
year_from {'TP': 214, 'FP': 60, 'FN': 81, 'TN': 28363, 'Precision': 0.781, 'Recall': 0.725, 'F1': 0.752, 'Accuracy': 0.995}
year_to {'TP': 215, 'FP': 59, 'FN': 80, 'TN': 24212, 'Precision': 0.785, 'Recall': 0.729, 'F1': 0.756, 'Accuracy': 0.994}
periods {'TP': 0, 'FP': 0, 'FN': 449, 'TN': 1021, 'Precision': -1, 'Recall': 0.0, 'F1': -1, 'Accuracy': 0.695}
moods {'TP': 0, 'FP': 0, 'FN': 267, 'TN': 1068, 'Precision': -1, 'Recall': 0.0, 'F1': -1, 'Accuracy': 0.8}
TOTAL {'TP': 3335, 'FP': 10822, 'FN': 8289, 'TN': 2987551, 'Precision': 0.236, 'Recall': 0.287, 'F1': 0.259, 'Accuracy': 0.994}

===  Performance per intent ===

Intent: author_query
authors {'TP': 27, 'FP': 2, 'FN': 552, 'TN': 250849, 'Precision': 0.931, 'Recall': 0.047, 'F1': 0.089, 'Accuracy': 0.998}
intent {'TP': 0, 'FP': 290, 'FN': 290, 'TN': 2030, 'Precision': 0.0, 'Recall': 0.0, 'F1': -1, 'Accuracy': 0.778}
publishers {'TP': 0, 'FP': 258, 'FN': 0, 'TN': 46782, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.995}
series {'TP': 0, 'FP': 424, 'FN': 0, 'TN': 71394, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.994}
TOTAL {'TP': 27, 'FP': 974, 'FN': 842, 'TN': 371055, 'Precision': 0.027, 'Recall': 0.031, 'F1': 0.029, 'Accuracy': 0.995}

Intent: recommend_book
pages_min {'TP': 4, 'FP': 0, 'FN': 274, 'TN': 61716, 'Precision': 1.0, 'Recall': 0.014, 'F1': 0.028, 'Accuracy': 0.996}
intent {'TP': 1671, 'FP': 203, 'FN': 203, 'TN': 14789, 'Precision': 0.892, 'Recall': 0.892, 'F1': 0.892, 'Accuracy': 0.976}
pages_max {'TP': 127, 'FP': 1, 'FN': 151, 'TN': 61715, 'Precision': 0.992, 'Recall': 0.457, 'F1': 0.626, 'Accuracy': 0.998}
publishers {'TP': 411, 'FP': 1217, 'FN': 266, 'TN': 240866, 'Precision': 0.252, 'Recall': 0.607, 'F1': 0.357, 'Accuracy': 0.994}
series {'TP': 405, 'FP': 4290, 'FN': 357, 'TN': 531646, 'Precision': 0.086, 'Recall': 0.531, 'F1': 0.148, 'Accuracy': 0.991}
categories {'TP': 5, 'FP': 15, 'FN': 1313, 'TN': 304919, 'Precision': 0.25, 'Recall': 0.004, 'F1': 0.007, 'Accuracy': 0.996}
languages {'TP': 0, 'FP': 1, 'FN': 426, 'TN': 4418, 'Precision': 0.0, 'Recall': 0.0, 'F1': -1, 'Accuracy': 0.912}
themes {'TP': 106, 'FP': 26, 'FN': 190, 'TN': 1904, 'Precision': 0.803, 'Recall': 0.358, 'F1': 0.495, 'Accuracy': 0.903}
types {'TP': 1, 'FP': 0, 'FN': 426, 'TN': 434, 'Precision': 1.0, 'Recall': 0.002, 'F1': 0.005, 'Accuracy': 0.505}
year_from {'TP': 214, 'FP': 49, 'FN': 81, 'TN': 27461, 'Precision': 0.814, 'Recall': 0.725, 'F1': 0.767, 'Accuracy': 0.995}
year_to {'TP': 215, 'FP': 48, 'FN': 80, 'TN': 23442, 'Precision': 0.817, 'Recall': 0.729, 'F1': 0.771, 'Accuracy': 0.995}
periods {'TP': 0, 'FP': 0, 'FN': 449, 'TN': 1021, 'Precision': -1, 'Recall': 0.0, 'F1': -1, 'Accuracy': 0.695}
moods {'TP': 0, 'FP': 0, 'FN': 267, 'TN': 1068, 'Precision': -1, 'Recall': 0.0, 'F1': -1, 'Accuracy': 0.8}
authors {'TP': 1, 'FP': 1, 'FN': 564, 'TN': 240460, 'Precision': 0.5, 'Recall': 0.002, 'F1': 0.004, 'Accuracy': 0.998}
TOTAL {'TP': 3160, 'FP': 5851, 'FN': 5047, 'TN': 1515859, 'Precision': 0.351, 'Recall': 0.385, 'F1': 0.367, 'Accuracy': 0.993}

Intent: book_query
intent {'TP': 0, 'FP': 351, 'FN': 351, 'TN': 2457, 'Precision': 0.0, 'Recall': 0.0, 'F1': -1, 'Accuracy': 0.778}
publishers {'TP': 0, 'FP': 358, 'FN': 0, 'TN': 55082, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.994}
books {'TP': 0, 'FP': 0, 'FN': 527, 'TN': 172516, 'Precision': -1, 'Recall': 0.0, 'F1': -1, 'Accuracy': 0.997}
series {'TP': 0, 'FP': 853, 'FN': 0, 'TN': 101361, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.992}
themes {'TP': 0, 'FP': 1, 'FN': 0, 'TN': 6, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.857}
year_from {'TP': 0, 'FP': 7, 'FN': 0, 'TN': 574, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.988}
year_to {'TP': 0, 'FP': 7, 'FN': 0, 'TN': 490, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.986}
categories {'TP': 0, 'FP': 3, 'FN': 0, 'TN': 1083, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.997}
languages {'TP': 0, 'FP': 1, 'FN': 0, 'TN': 16, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.941}
TOTAL {'TP': 0, 'FP': 1581, 'FN': 878, 'TN': 333585, 'Precision': 0.0, 'Recall': 0.0, 'F1': -1, 'Accuracy': 0.993}

Intent: feedback_like
intent {'TP': 13, 'FP': 116, 'FN': 116, 'TN': 916, 'Precision': 0.101, 'Recall': 0.101, 'F1': 0.101, 'Accuracy': 0.8}
similar_to_books {'TP': 0, 'FP': 0, 'FN': 139, 'TN': 93045, 'Precision': -1, 'Recall': 0.0, 'F1': -1, 'Accuracy': 0.999}
publishers {'TP': 0, 'FP': 58, 'FN': 0, 'TN': 10652, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.995}
series {'TP': 0, 'FP': 89, 'FN': 0, 'TN': 18089, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.995}
year_from {'TP': 0, 'FP': 3, 'FN': 0, 'TN': 246, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.988}
year_to {'TP': 0, 'FP': 3, 'FN': 0, 'TN': 210, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.986}
categories {'TP': 0, 'FP': 1, 'FN': 0, 'TN': 361, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.997}
themes {'TP': 0, 'FP': 1, 'FN': 0, 'TN': 6, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.857}
TOTAL {'TP': 13, 'FP': 271, 'FN': 255, 'TN': 123525, 'Precision': 0.046, 'Recall': 0.049, 'F1': 0.047, 'Accuracy': 0.996}

Intent: similar_book
intent {'TP': 0, 'FP': 362, 'FN': 362, 'TN': 2534, 'Precision': 0.0, 'Recall': 0.0, 'F1': -1, 'Accuracy': 0.778}
similar_to_books {'TP': 99, 'FP': 23, 'FN': 612, 'TN': 323618, 'Precision': 0.811, 'Recall': 0.139, 'F1': 0.238, 'Accuracy': 0.998}
publishers {'TP': 0, 'FP': 328, 'FN': 0, 'TN': 50492, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.994}
series {'TP': 0, 'FP': 921, 'FN': 0, 'TN': 106061, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.991}
themes {'TP': 0, 'FP': 4, 'FN': 0, 'TN': 24, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.857}
categories {'TP': 0, 'FP': 6, 'FN': 0, 'TN': 2166, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.997}
authors {'TP': 0, 'FP': 3, 'FN': 0, 'TN': 1731, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.998}
TOTAL {'TP': 99, 'FP': 1647, 'FN': 974, 'TN': 486626, 'Precision': 0.057, 'Recall': 0.092, 'F1': 0.07, 'Accuracy': 0.995}

Intent: feedback_dislike
intent {'TP': 0, 'FP': 120, 'FN': 120, 'TN': 840, 'Precision': 0.0, 'Recall': 0.0, 'F1': -1, 'Accuracy': 0.778}
similar_to_books {'TP': 0, 'FP': 0, 'FN': 134, 'TN': 93946, 'Precision': -1, 'Recall': 0.0, 'F1': -1, 'Accuracy': 0.999}
publishers {'TP': 0, 'FP': 44, 'FN': 0, 'TN': 7516, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.994}
series {'TP': 0, 'FP': 186, 'FN': 0, 'TN': 34978, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.995}
year_from {'TP': 0, 'FP': 1, 'FN': 0, 'TN': 82, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.988}
year_to {'TP': 0, 'FP': 1, 'FN': 0, 'TN': 70, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.986}
categories {'TP': 0, 'FP': 1, 'FN': 0, 'TN': 361, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.997}
TOTAL {'TP': 0, 'FP': 353, 'FN': 254, 'TN': 137793, 'Precision': 0.0, 'Recall': 0.0, 'F1': -1, 'Accuracy': 0.996}

Intent: clarification_answer
intent {'TP': 8, 'FP': 28, 'FN': 28, 'TN': 260, 'Precision': 0.222, 'Recall': 0.222, 'F1': 0.222, 'Accuracy': 0.827}
publishers {'TP': 0, 'FP': 9, 'FN': 0, 'TN': 1671, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.995}
series {'TP': 0, 'FP': 56, 'FN': 0, 'TN': 9480, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.994}
themes {'TP': 0, 'FP': 1, 'FN': 0, 'TN': 6, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.857}
TOTAL {'TP': 8, 'FP': 94, 'FN': 28, 'TN': 11417, 'Precision': 0.078, 'Recall': 0.222, 'F1': 0.116, 'Accuracy': 0.989}

Intent: unknown
intent {'TP': 25, 'FP': 0, 'FN': 0, 'TN': 200, 'Precision': 1.0, 'Recall': 1.0, 'F1': 1.0, 'Accuracy': 1.0}
series {'TP': 0, 'FP': 32, 'FN': 0, 'TN': 5928, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.995}
publishers {'TP': 0, 'FP': 5, 'FN': 0, 'TN': 1045, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.995}
TOTAL {'TP': 25, 'FP': 37, 'FN': 0, 'TN': 7173, 'Precision': 0.403, 'Recall': 1.0, 'F1': 0.575, 'Accuracy': 0.995}

Intent: greeting
intent {'TP': 3, 'FP': 11, 'FN': 11, 'TN': 101, 'Precision': 0.214, 'Recall': 0.214, 'F1': 0.214, 'Accuracy': 0.825}
publishers {'TP': 0, 'FP': 3, 'FN': 0, 'TN': 417, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.993}
TOTAL {'TP': 3, 'FP': 14, 'FN': 11, 'TN': 518, 'Precision': 0.176, 'Recall': 0.214, 'F1': 0.194, 'Accuracy': 0.954}



## Combined parser
===  Total performance ===
authors {'TP': 546, 'FP': 87, 'FN': 598, 'TN': 568364, 'Precision': 0.863, 'Recall': 0.477, 'F1': 0.615, 'Accuracy': 0.999}
intent {'TP': 1938, 'FP': 1263, 'FN': 1263, 'TN': 24345, 'Precision': 0.605, 'Recall': 0.605, 'F1': 0.605, 'Accuracy': 0.912}
free_text {'TP': 0, 'FP': 3201, 'FN': 0, 'TN': 10243200, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 1.0}
themes {'TP': 169, 'FP': 87, 'FN': 127, 'TN': 2200, 'Precision': 0.66, 'Recall': 0.571, 'F1': 0.612, 'Accuracy': 0.917}
publishers {'TP': 367, 'FP': 52, 'FN': 310, 'TN': 88096, 'Precision': 0.876, 'Recall': 0.542, 'F1': 0.67, 'Accuracy': 0.996}
pages_min {'TP': 25, 'FP': 0, 'FN': 253, 'TN': 61716, 'Precision': 1.0, 'Recall': 0.09, 'F1': 0.165, 'Accuracy': 0.996}
pages_max {'TP': 127, 'FP': 1, 'FN': 151, 'TN': 61715, 'Precision': 0.992, 'Recall': 0.457, 'F1': 0.626, 'Accuracy': 0.998}
categories {'TP': 270, 'FP': 271, 'FN': 1048, 'TN': 339415, 'Precision': 0.499, 'Recall': 0.205, 'F1': 0.29, 'Accuracy': 0.996}
languages {'TP': 114, 'FP': 24, 'FN': 312, 'TN': 4718, 'Precision': 0.826, 'Recall': 0.268, 'F1': 0.404, 'Accuracy': 0.935}
series {'TP': 365, 'FP': 202, 'FN': 397, 'TN': 170716, 'Precision': 0.644, 'Recall': 0.479, 'F1': 0.549, 'Accuracy': 0.997}
books {'TP': 0, 'FP': 0, 'FN': 527, 'TN': 172516, 'Precision': -1, 'Recall': 0.0, 'F1': -1, 'Accuracy': 0.997}
similar_to_books {'TP': 316, 'FP': 109, 'FN': 668, 'TN': 534505, 'Precision': 0.744, 'Recall': 0.321, 'F1': 0.449, 'Accuracy': 0.999}
types {'TP': 92, 'FP': 0, 'FN': 335, 'TN': 434, 'Precision': 1.0, 'Recall': 0.215, 'F1': 0.355, 'Accuracy': 0.611}
year_from {'TP': 214, 'FP': 50, 'FN': 81, 'TN': 27289, 'Precision': 0.811, 'Recall': 0.725, 'F1': 0.766, 'Accuracy': 0.995}
year_to {'TP': 208, 'FP': 54, 'FN': 87, 'TN': 23731, 'Precision': 0.794, 'Recall': 0.705, 'F1': 0.747, 'Accuracy': 0.994}
periods {'TP': 71, 'FP': 45, 'FN': 378, 'TN': 1066, 'Precision': 0.612, 'Recall': 0.158, 'F1': 0.251, 'Accuracy': 0.729}
moods {'TP': 56, 'FP': 0, 'FN': 211, 'TN': 1068, 'Precision': 1.0, 'Recall': 0.21, 'F1': 0.347, 'Accuracy': 0.842}
similar_to_authors {'TP': 0, 'FP': 12, 'FN': 0, 'TN': 132, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.917}
TOTAL {'TP': 4878, 'FP': 5458, 'FN': 6746, 'TN': 12325226, 'Precision': 0.472, 'Recall': 0.42, 'F1': 0.444, 'Accuracy': 0.999}

===  Performance per intent ===

Intent: author_query
authors {'TP': 427, 'FP': 11, 'FN': 152, 'TN': 259540, 'Precision': 0.975, 'Recall': 0.737, 'F1': 0.84, 'Accuracy': 0.999}
intent {'TP': 0, 'FP': 290, 'FN': 290, 'TN': 2030, 'Precision': 0.0, 'Recall': 0.0, 'F1': -1, 'Accuracy': 0.778}
free_text {'TP': 0, 'FP': 290, 'FN': 0, 'TN': 928000, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 1.0}
themes {'TP': 0, 'FP': 4, 'FN': 0, 'TN': 24, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.857}
publishers {'TP': 0, 'FP': 1, 'FN': 0, 'TN': 208, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.995}
TOTAL {'TP': 427, 'FP': 596, 'FN': 442, 'TN': 1189802, 'Precision': 0.417, 'Recall': 0.491, 'F1': 0.451, 'Accuracy': 0.999}

Intent: recommend_book
pages_min {'TP': 25, 'FP': 0, 'FN': 253, 'TN': 61716, 'Precision': 1.0, 'Recall': 0.09, 'F1': 0.165, 'Accuracy': 0.996}
intent {'TP': 1671, 'FP': 203, 'FN': 203, 'TN': 14789, 'Precision': 0.892, 'Recall': 0.892, 'F1': 0.892, 'Accuracy': 0.976}
free_text {'TP': 0, 'FP': 1874, 'FN': 0, 'TN': 5996800, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 1.0}
pages_max {'TP': 127, 'FP': 1, 'FN': 151, 'TN': 61715, 'Precision': 0.992, 'Recall': 0.457, 'F1': 0.626, 'Accuracy': 0.998}
categories {'TP': 270, 'FP': 242, 'FN': 1048, 'TN': 329308, 'Precision': 0.527, 'Recall': 0.205, 'F1': 0.295, 'Accuracy': 0.996}
languages {'TP': 114, 'FP': 19, 'FN': 312, 'TN': 4638, 'Precision': 0.857, 'Recall': 0.268, 'F1': 0.408, 'Accuracy': 0.935}
series {'TP': 365, 'FP': 135, 'FN': 397, 'TN': 151933, 'Precision': 0.73, 'Recall': 0.479, 'F1': 0.578, 'Accuracy': 0.997}
themes {'TP': 169, 'FP': 53, 'FN': 127, 'TN': 2003, 'Precision': 0.761, 'Recall': 0.571, 'F1': 0.653, 'Accuracy': 0.923}
types {'TP': 92, 'FP': 0, 'FN': 335, 'TN': 434, 'Precision': 1.0, 'Recall': 0.215, 'F1': 0.355, 'Accuracy': 0.611}
year_from {'TP': 214, 'FP': 39, 'FN': 81, 'TN': 26398, 'Precision': 0.846, 'Recall': 0.725, 'F1': 0.781, 'Accuracy': 0.996}
year_to {'TP': 208, 'FP': 43, 'FN': 87, 'TN': 22972, 'Precision': 0.829, 'Recall': 0.705, 'F1': 0.762, 'Accuracy': 0.994}
periods {'TP': 71, 'FP': 43, 'FN': 378, 'TN': 1058, 'Precision': 0.623, 'Recall': 0.158, 'F1': 0.252, 'Accuracy': 0.728}
moods {'TP': 56, 'FP': 0, 'FN': 211, 'TN': 1068, 'Precision': 1.0, 'Recall': 0.21, 'F1': 0.347, 'Accuracy': 0.842}
authors {'TP': 119, 'FP': 17, 'FN': 446, 'TN': 261342, 'Precision': 0.875, 'Recall': 0.211, 'F1': 0.34, 'Accuracy': 0.998}
publishers {'TP': 367, 'FP': 26, 'FN': 310, 'TN': 83106, 'Precision': 0.934, 'Recall': 0.542, 'F1': 0.686, 'Accuracy': 0.996}
TOTAL {'TP': 3868, 'FP': 2695, 'FN': 4339, 'TN': 7019280, 'Precision': 0.589, 'Recall': 0.471, 'F1': 0.524, 'Accuracy': 0.999}

Intent: book_query
intent {'TP': 2, 'FP': 349, 'FN': 349, 'TN': 2459, 'Precision': 0.006, 'Recall': 0.006, 'F1': 0.006, 'Accuracy': 0.779}
free_text {'TP': 0, 'FP': 351, 'FN': 0, 'TN': 1123200, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 1.0}
books {'TP': 0, 'FP': 0, 'FN': 527, 'TN': 172516, 'Precision': -1, 'Recall': 0.0, 'F1': -1, 'Accuracy': 0.997}
categories {'TP': 0, 'FP': 11, 'FN': 0, 'TN': 3609, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.997}
authors {'TP': 0, 'FP': 20, 'FN': 0, 'TN': 17920, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.999}
themes {'TP': 0, 'FP': 10, 'FN': 0, 'TN': 60, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.857}
publishers {'TP': 0, 'FP': 6, 'FN': 0, 'TN': 1039, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.994}
year_from {'TP': 0, 'FP': 7, 'FN': 0, 'TN': 567, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.988}
year_to {'TP': 0, 'FP': 7, 'FN': 0, 'TN': 483, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.986}
languages {'TP': 0, 'FP': 4, 'FN': 0, 'TN': 64, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.941}
series {'TP': 0, 'FP': 23, 'FN': 0, 'TN': 6067, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.996}
periods {'TP': 0, 'FP': 1, 'FN': 0, 'TN': 4, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.8}
TOTAL {'TP': 2, 'FP': 789, 'FN': 876, 'TN': 1327988, 'Precision': 0.003, 'Recall': 0.002, 'F1': 0.002, 'Accuracy': 0.999}

Intent: feedback_like
intent {'TP': 13, 'FP': 116, 'FN': 116, 'TN': 916, 'Precision': 0.101, 'Recall': 0.101, 'F1': 0.101, 'Accuracy': 0.8}
free_text {'TP': 0, 'FP': 129, 'FN': 0, 'TN': 412800, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 1.0}
similar_to_books {'TP': 0, 'FP': 0, 'FN': 139, 'TN': 97413, 'Precision': -1, 'Recall': 0.0, 'F1': -1, 'Accuracy': 0.999}
series {'TP': 0, 'FP': 11, 'FN': 0, 'TN': 3179, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.997}
languages {'TP': 0, 'FP': 1, 'FN': 0, 'TN': 16, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.941}
themes {'TP': 0, 'FP': 2, 'FN': 0, 'TN': 12, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.857}
year_from {'TP': 0, 'FP': 3, 'FN': 0, 'TN': 243, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.988}
year_to {'TP': 0, 'FP': 3, 'FN': 0, 'TN': 207, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.986}
authors {'TP': 0, 'FP': 5, 'FN': 0, 'TN': 2686, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.998}
publishers {'TP': 0, 'FP': 4, 'FN': 0, 'TN': 623, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.994}
categories {'TP': 0, 'FP': 1, 'FN': 0, 'TN': 361, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.997}
TOTAL {'TP': 13, 'FP': 275, 'FN': 255, 'TN': 518456, 'Precision': 0.045, 'Recall': 0.049, 'F1': 0.047, 'Accuracy': 0.999}

Intent: similar_book
intent {'TP': 211, 'FP': 151, 'FN': 151, 'TN': 2745, 'Precision': 0.583, 'Recall': 0.583, 'F1': 0.583, 'Accuracy': 0.907}
free_text {'TP': 0, 'FP': 362, 'FN': 0, 'TN': 1158400, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 1.0}
similar_to_books {'TP': 316, 'FP': 109, 'FN': 395, 'TN': 338736, 'Precision': 0.744, 'Recall': 0.444, 'F1': 0.556, 'Accuracy': 0.999}
publishers {'TP': 0, 'FP': 13, 'FN': 0, 'TN': 2704, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.995}
series {'TP': 0, 'FP': 27, 'FN': 0, 'TN': 7803, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.997}
themes {'TP': 0, 'FP': 15, 'FN': 0, 'TN': 83, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.847}
categories {'TP': 0, 'FP': 13, 'FN': 0, 'TN': 4693, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.997}
authors {'TP': 0, 'FP': 30, 'FN': 0, 'TN': 23292, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.999}
similar_to_authors {'TP': 0, 'FP': 12, 'FN': 0, 'TN': 132, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.917}
TOTAL {'TP': 527, 'FP': 732, 'FN': 546, 'TN': 1538588, 'Precision': 0.419, 'Recall': 0.491, 'F1': 0.452, 'Accuracy': 0.999}

Intent: feedback_dislike
periods {'TP': 0, 'FP': 1, 'FN': 0, 'TN': 4, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.8}
intent {'TP': 5, 'FP': 115, 'FN': 115, 'TN': 845, 'Precision': 0.042, 'Recall': 0.042, 'F1': 0.042, 'Accuracy': 0.787}
free_text {'TP': 0, 'FP': 120, 'FN': 0, 'TN': 384000, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 1.0}
similar_to_books {'TP': 0, 'FP': 0, 'FN': 134, 'TN': 98356, 'Precision': -1, 'Recall': 0.0, 'F1': -1, 'Accuracy': 0.999}
series {'TP': 0, 'FP': 6, 'FN': 0, 'TN': 1734, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.997}
categories {'TP': 0, 'FP': 4, 'FN': 0, 'TN': 1444, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.997}
year_from {'TP': 0, 'FP': 1, 'FN': 0, 'TN': 81, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.988}
year_to {'TP': 0, 'FP': 1, 'FN': 0, 'TN': 69, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.986}
authors {'TP': 0, 'FP': 4, 'FN': 0, 'TN': 3584, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.999}
themes {'TP': 0, 'FP': 2, 'FN': 0, 'TN': 12, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.857}
TOTAL {'TP': 5, 'FP': 254, 'FN': 249, 'TN': 490129, 'Precision': 0.019, 'Recall': 0.02, 'F1': 0.019, 'Accuracy': 0.999}

Intent: clarification_answer
intent {'TP': 8, 'FP': 28, 'FN': 28, 'TN': 260, 'Precision': 0.222, 'Recall': 0.222, 'F1': 0.222, 'Accuracy': 0.827}
free_text {'TP': 0, 'FP': 36, 'FN': 0, 'TN': 115200, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 1.0}
themes {'TP': 0, 'FP': 1, 'FN': 0, 'TN': 6, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.857}
TOTAL {'TP': 8, 'FP': 65, 'FN': 28, 'TN': 115466, 'Precision': 0.11, 'Recall': 0.222, 'F1': 0.147, 'Accuracy': 0.999}

Intent: unknown
intent {'TP': 25, 'FP': 0, 'FN': 0, 'TN': 200, 'Precision': 1.0, 'Recall': 1.0, 'F1': 1.0, 'Accuracy': 1.0}
free_text {'TP': 0, 'FP': 25, 'FN': 0, 'TN': 80000, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 1.0}
publishers {'TP': 0, 'FP': 2, 'FN': 0, 'TN': 416, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.995}
TOTAL {'TP': 25, 'FP': 27, 'FN': 0, 'TN': 80616, 'Precision': 0.481, 'Recall': 1.0, 'F1': 0.649, 'Accuracy': 1.0}

Intent: greeting
intent {'TP': 3, 'FP': 11, 'FN': 11, 'TN': 101, 'Precision': 0.214, 'Recall': 0.214, 'F1': 0.214, 'Accuracy': 0.825}
free_text {'TP': 0, 'FP': 14, 'FN': 0, 'TN': 44800, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 1.0}
TOTAL {'TP': 3, 'FP': 25, 'FN': 11, 'TN': 44901, 'Precision': 0.107, 'Recall': 0.214, 'F1': 0.143, 'Accuracy': 0.999}




## NLU parser extra run for categories testing
===  Total performance ===
categories {'TP': 414, 'FP': 155, 'FN': 266, 'TN': 140502, 'Precision': 0.728, 'Recall': 0.609, 'F1': 0.663, 'Accuracy': 0.997}
intent {'TP': 424, 'FP': 3, 'FN': 3, 'TN': 851, 'Precision': 0.993, 'Recall': 0.993, 'F1': 0.993, 'Accuracy': 0.995}
free_text {'TP': 0, 'FP': 324, 'FN': 0, 'TN': 104328, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.997}
moods {'TP': 10, 'FP': 190, 'FN': 41, 'TN': 14709, 'Precision': 0.05, 'Recall': 0.196, 'F1': 0.08, 'Accuracy': 0.985}
pages_max {'TP': 47, 'FP': 2, 'FN': 14, 'TN': 3536, 'Precision': 0.959, 'Recall': 0.77, 'F1': 0.855, 'Accuracy': 0.996}
pages_min {'TP': 47, 'FP': 2, 'FN': 14, 'TN': 3657, 'Precision': 0.959, 'Recall': 0.77, 'F1': 0.855, 'Accuracy': 0.996}
themes {'TP': 48, 'FP': 437, 'FN': 25, 'TN': 78080, 'Precision': 0.099, 'Recall': 0.658, 'F1': 0.172, 'Accuracy': 0.994}
series {'TP': 49, 'FP': 1, 'FN': 57, 'TN': 4997, 'Precision': 0.98, 'Recall': 0.462, 'F1': 0.628, 'Accuracy': 0.989}
periods {'TP': 59, 'FP': 51, 'FN': 34, 'TN': 351, 'Precision': 0.536, 'Recall': 0.634, 'F1': 0.581, 'Accuracy': 0.828}
year_from {'TP': 49, 'FP': 7, 'FN': 13, 'TN': 3013, 'Precision': 0.875, 'Recall': 0.79, 'F1': 0.831, 'Accuracy': 0.994}
languages {'TP': 76, 'FP': 27, 'FN': 6, 'TN': 1267, 'Precision': 0.738, 'Recall': 0.927, 'F1': 0.822, 'Accuracy': 0.976}
year_to {'TP': 47, 'FP': 5, 'FN': 15, 'TN': 2598, 'Precision': 0.904, 'Recall': 0.758, 'F1': 0.825, 'Accuracy': 0.992}
types {'TP': 68, 'FP': 4, 'FN': 19, 'TN': 95, 'Precision': 0.944, 'Recall': 0.782, 'F1': 0.855, 'Accuracy': 0.876}
authors {'TP': 82, 'FP': 30, 'FN': 32, 'TN': 7665, 'Precision': 0.732, 'Recall': 0.719, 'F1': 0.726, 'Accuracy': 0.992}
publishers {'TP': 69, 'FP': 4, 'FN': 46, 'TN': 5585, 'Precision': 0.945, 'Recall': 0.6, 'F1': 0.734, 'Accuracy': 0.991}
similar_to_books {'TP': 0, 'FP': 1, 'FN': 0, 'TN': 0, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.0}
TOTAL {'TP': 1489, 'FP': 1243, 'FN': 585, 'TN': 371234, 'Precision': 0.545, 'Recall': 0.718, 'F1': 0.62, 'Accuracy': 0.995}

===  Performance per intent ===

Intent: recommend_book
categories {'TP': 414, 'FP': 155, 'FN': 266, 'TN': 140502, 'Precision': 0.728, 'Recall': 0.609, 'F1': 0.663, 'Accuracy': 0.997}
intent {'TP': 424, 'FP': 3, 'FN': 3, 'TN': 851, 'Precision': 0.993, 'Recall': 0.993, 'F1': 0.993, 'Accuracy': 0.995}
free_text {'TP': 0, 'FP': 324, 'FN': 0, 'TN': 104328, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.997}
moods {'TP': 10, 'FP': 190, 'FN': 41, 'TN': 14709, 'Precision': 0.05, 'Recall': 0.196, 'F1': 0.08, 'Accuracy': 0.985}
pages_max {'TP': 47, 'FP': 2, 'FN': 14, 'TN': 3536, 'Precision': 0.959, 'Recall': 0.77, 'F1': 0.855, 'Accuracy': 0.996}
pages_min {'TP': 47, 'FP': 2, 'FN': 14, 'TN': 3657, 'Precision': 0.959, 'Recall': 0.77, 'F1': 0.855, 'Accuracy': 0.996}
themes {'TP': 48, 'FP': 437, 'FN': 25, 'TN': 78080, 'Precision': 0.099, 'Recall': 0.658, 'F1': 0.172, 'Accuracy': 0.994}
series {'TP': 49, 'FP': 1, 'FN': 57, 'TN': 4997, 'Precision': 0.98, 'Recall': 0.462, 'F1': 0.628, 'Accuracy': 0.989}
periods {'TP': 59, 'FP': 51, 'FN': 34, 'TN': 351, 'Precision': 0.536, 'Recall': 0.634, 'F1': 0.581, 'Accuracy': 0.828}
year_from {'TP': 49, 'FP': 7, 'FN': 13, 'TN': 3013, 'Precision': 0.875, 'Recall': 0.79, 'F1': 0.831, 'Accuracy': 0.994}
languages {'TP': 76, 'FP': 27, 'FN': 6, 'TN': 1267, 'Precision': 0.738, 'Recall': 0.927, 'F1': 0.822, 'Accuracy': 0.976}
year_to {'TP': 47, 'FP': 5, 'FN': 15, 'TN': 2598, 'Precision': 0.904, 'Recall': 0.758, 'F1': 0.825, 'Accuracy': 0.992}
types {'TP': 68, 'FP': 4, 'FN': 19, 'TN': 95, 'Precision': 0.944, 'Recall': 0.782, 'F1': 0.855, 'Accuracy': 0.876}
authors {'TP': 82, 'FP': 30, 'FN': 32, 'TN': 7665, 'Precision': 0.732, 'Recall': 0.719, 'F1': 0.726, 'Accuracy': 0.992}
publishers {'TP': 69, 'FP': 4, 'FN': 46, 'TN': 5585, 'Precision': 0.945, 'Recall': 0.6, 'F1': 0.734, 'Accuracy': 0.991}
similar_to_books {'TP': 0, 'FP': 1, 'FN': 0, 'TN': 0, 'Precision': 0.0, 'Recall': -1, 'F1': -1, 'Accuracy': 0.0}
TOTAL {'TP': 1489, 'FP': 1243, 'FN': 585, 'TN': 371234, 'Precision': 0.545, 'Recall': 0.718, 'F1': 0.62, 'Accuracy': 0.995}