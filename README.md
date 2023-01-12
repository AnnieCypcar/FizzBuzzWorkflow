# FizzBuzzWorkflow

The FizzBuzzWorkflow is a Google Cloud Workflow available at the protected endpoint:

https://workflowexecutions.googleapis.com/v1/projects/sound-chalice-232414/locations/us-central1/workflows/fizzbuzz_workflow/executions

Remaining to do:
1. figure out a way to authenticate from a client
2. find out how to correctly pass input to the workflow entry point (the below curl responds 400)

```
curl \                                     
--request POST "https://workflowexecutions.googleapis.com/v1/projects/sound-chalice-232414/locations/us-central1/workflows/fizzbuzz_workflow/executions" \
--header "Authorization: Bearer "$(gcloud auth application-default print-access-token) \
--header 'Content-Type: application/json' \
--data-raw '{
    "input": 15
}'
```