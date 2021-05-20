# Calculate the accuracy of a baseline that simply predicts "London" for every
#   example in the dev set.
# Hint: Make use of existing code.
# Your solution here should only be a few lines.
import utils

line_count = len(open('birth_dev.tsv', 'r').readlines())
preds = ['London'] * line_count
total, correct = utils.evaluate_places('birth_dev.tsv', preds)
print('Correct: {} out of {}: {}%'.format(
    correct, total, correct/total*100))
