from pprint import pprint

from .visualization import histogram

def transform_results(results):
    assert len(results) > 0, 'Cannot post-process empty results'
    first = list(results.values())[0]

    trials = dict()
    for i in range(len(first)):
        trial_measurement = dict()
        for qubit, measurements in results.items():
            trial_measurement[qubit] = measurements[i]
        trials[i] = trial_measurement
    return trials

def postprocess(results):
    results = transform_results(results)
    histogram(results)
