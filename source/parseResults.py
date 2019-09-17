# parseResults.py: Read the output file and parse the scores.
# put part of output file and scores into result.json

import os
import json

info = ""
scores = None
results = {}
outputFileLen = None
outputSizeLimit = 50000
outputLines = None

def addLine(line, maxLen):
    global info
    if len(line) > maxLen - len(info):
        return False
    info += line
    return True

try:
    outputFileLen = os.stat('/var/run/grader/output').st_size
    with open('/var/run/grader/output', 'r') as outputf:
        outputLines = outputf.readlines()
        scores = json.loads(outputLines[-1])
except Exception as e:
    info = "Failed to find scores from grading output: %s\n\n" % e

if scores:
    tests = []
    total = 0.0
    for t in scores['scores']:
        tests.append({'name': t,
                      'max_score': 1,
                      'score': scores['scores'][t]
        })
        total += float(scores['scores'][t])
    results['score'] = total
    results['tests'] = tests

if outputFileLen and \
   outputFileLen <= outputSizeLimit - len(info):
    # output need not truncation
    info += ''.join(outputLines)
elif outputFileLen:
    info += 'The middle of the output file has been removed.\n'
    info += 'Removed text is marked with ###########.\n'

    # Take the first half of the output
    for line in outputLines:
        if not addLine(line, outputSizeLimit/2):
            break

    middleMark = '######### The removed output was here.\n'
    info += middleMark

    # compute where the second half starts
    accumulated = len(middleMark)
    totalLines = len(outputLines)
    secondHalfStart = totalLines - 1
    for lineNum in reversed(range(0, totalLines)):
        if len(outputLines[lineNum]) > outputSizeLimit/2 - accumulated:
            break
        accumulated += len(outputLines[lineNum])
        secondHalfStart = lineNum

    # put the second half in
    for lineNum in range(secondHalfStart, totalLines):
        info += outputLines[lineNum]

results['output'] = info
assert len(info) <= outputSizeLimit

with open('/var/run/grader/results.json', 'w', encoding='utf-8') as resultsf:
    json.dump(results, resultsf, indent=4)
