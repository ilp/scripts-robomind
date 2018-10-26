import json
import subprocess
import argparse

parser = argparse.ArgumentParser(description='run fdr assertion and get traces if has counterexample')
parser.add_argument('-p','--pathCSP', required=True, help="path to csp assertion")
args = vars(parser.parse_args())

path_csp = args["pathCSP"]

main_result = subprocess.check_output("refines --format=json --quiet " + path_csp, shell = True)
main_result = json.loads(main_result)

results = main_result.get('results')
event_map = main_result.get('event_map')
print results
for r in results:
    counterexamples = r.get('counterexamples')
if counterexamples == []:
    trace = []
for c in counterexamples:
    trace = c.get('implementation_behaviour').get('trace')

traces = []
for i in range(0, len(trace)):
    if trace[i] != 1:
        traces.append(event_map.get(str(trace[i])))

print json.dumps(traces)