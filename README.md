# FizzBuzzWorkflow

The FizzBuzzWorkflow is a Google Cloud Workflow available at the protected endpoint:

https://workflowexecutions.googleapis.com/v1/projects/sound-chalice-232414/locations/us-central1/workflows/fizzbuzz_workflow/executions

Remaining to do:
1. figure out a way to authenticate from a client
~~2. find out how to correctly pass input to the workflow entry point (the below curl responds 400)~~

```
gcloud workflows run fizzbuzz_workflow \
--data='{"input":15}'

```
Response:
```
Waiting for execution [b578d67e-15a8-4468-bd24-b58890fa25dd] to complete...done.                                                                                                                       
argument: '{"input":15}'
duration: 4.057084158s
endTime: '2023-01-12T13:02:15.580519235Z'
name: projects/206072839442/locations/us-central1/workflows/fizzbuzz_workflow/executions/b578d67e-15a8-4468-bd24-b58890fa25dd
result: '{"body":{"answer":["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]},"code":200,"headers":{"Alt-Svc":"h3=\":443\";
  ma=2592000,h3-29=\":443\"; ma=2592000,h3-Q050=\":443\"; ma=2592000,h3-Q046=\":443\";
  ma=2592000,h3-Q043=\":443\"; ma=2592000,quic=\":443\"; ma=2592000; v=\"46,43\"","Cache-Control":"private","Content-Length":"101","Content-Type":"application/json","Date":"Thu,
  12 Jan 2023 13:02:15 GMT","Function-Execution-Id":"0blbnir4tr3r","Server":"Google
  Frontend","X-Cloud-Trace-Context":"1c94164efe04da2a40b0d1bdca7b4150;o=1"}}'
startTime: '2023-01-12T13:02:11.523435077Z'
state: SUCCEEDED
status:
  currentSteps:
  - routine: main
    step: return_result
workflowRevisionId: 000001-ed4
```

```
curl --request POST "https://workflowexecutions.googleapis.com/v1/projects/sound-chalice-232414/locations/us-central1/workflows/fizzbuzz_workflow/executions" \
--header "Authorization: Bearer "$(gcloud auth application-default print-access-token) \
--header 'Content-Type: application/json' \
--data '{
    "input": 15
}'
```