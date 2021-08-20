# merge-profile-data


## References
- https://gist.github.com/nitaku/10d0662536f37a087e1b  
- https://docs.github.com/en/rest/reference/orgs
- https://developer.atlassian.com/bitbucket/api/2/reference/resource/workspaces  

## Endpoints
- GET /profile?github={organization_name}&bitbucket={team_name}  
- GET /members?github={organization_name}&bitbucket={team_name}  
- GET /repositories?github={organization_name}&bitbucket={team_name}  
- GET /projects?github={organization_name}&bitbucket={team_name}  
- GET /packages?github={organization_name}&bitbucket={team_name}  

GitHub organization_name & BitBucket team_name as query params  
Allows us extensibility option to merge more than 2 sources/organizations in the future if needed


## Overview
The components of this work in progress are:
- /src folder
    - Simple Python HTTP server that accepts requests on `localhost:5000`
        - Processes HTTP requests and sends `profile` response as JSON
    - Class hierarchy
        - [Profile](src/profiles/profile.py)
        - [Repository](src/profiles/repository.py)
        - [BusinessEntity](src/profiles/business_entity.py)
        - [Organization](src/profiles/github/organization.py)
        - [Team](src/profiles/bitbucket/team.py)
- Postman collection demonstrating usage of the /profile endpoint
- [Documentation](documentation/README.md) - which addresses items from the prompt
