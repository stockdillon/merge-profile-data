# TESTING

## Unit Testing
- Would write unit tests, starting with the most granular classes that are least likely significantly change during early development
- For more complex classes, TDD would be useful
    - Determine a use case, write tests that assert expected outcomes for different possible scenarios and edge cases
- These would be executed for each PR as part of CICD pipelines to prevent regression

## Integration Testing
- Add Newman cli steps to CI/CD pipeline to execute requests and assert expectations programatically  

## Postman
- Would create a Postman collection that includes requests for each use case and edge case (to be executed & verified manually)
- Later, automate in Postman. Write javascript assertions for expected status codes or field values

## e2e testing
- Coming from an Angular background, I'm familiar with Protractor and Cypress for e2e testing
- Assuming there is a client-side application for this, you can e2e test with these tools to confirm API is being consumed without issue
