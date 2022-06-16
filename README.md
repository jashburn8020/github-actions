# GitHub Actions

## Understanding GitHub Actions

- Continuous integration and continuous delivery (CI/CD) platform
  - automate your build, test, and deployment pipeline
  - create workflows that build and test every pull request to your repository, or deploy merged pull requests to production
- Run workflows when other events happen in your repository
  - e.g., add the appropriate labels whenever someone creates a new issue in your repository
- Provides Linux, Windows, and macOS virtual machines to run your workflows
  - or you can host your own self-hosted runners in your own data center or cloud infrastructure

### The components of GitHub Actions

- **Workflow**: triggered when an event occurs in your repository
  - pull request being opened or an issue being created
- Workflow contains one or more **jobs** which can run in sequential order or in parallel
  - each job runs inside its own virtual machine **runner** or container
  - has one or more **steps** that either run
    - a script that you define or
    - an **action** - reusable extension

#### Workflows

- Configurable automated process that will run one or more jobs
  - defined by a YAML file checked in to your repository
  - triggered
    - by an event in your repository
    - manually
    - at a defined schedule
- Defined in the **`.github/workflows`** directory in a repository
- A repository can have multiple workflows
  - build and test pull requests
  - deploy your application every time a release is created
  - add a label every time someone opens a new issue
- You can reference a workflow within another workflow

#### Events

- A specific activity in a repository that triggers a workflow run
- An activity can originate from GitHub when someone
  - creates a pull request
  - opens an issue
  - pushes a commit to a repository
- You can also trigger a workflow run
  - on a schedule
  - by posting to a REST API
  - manually

#### Jobs

- A set of steps in a workflow that execute on the same runner
- Each step is either a shell script that will be executed, or an action that will be run
- Steps are executed in order and are dependent on each other
- Can share data from one step to another
- Can configure a job's dependencies with other jobs
  - by default, jobs have no dependencies and run in parallel with each other
  - e.g., build jobs will run in parallel, and when they have all completed successfully, the packaging job will run

#### Actions

- A custom application for the GitHub Actions platform that performs a complex but frequently repeated task
- Help reduce the amount of repetitive code that you write in your workflow files, e.g.
  - pull your git repository from GitHub
  - set up the correct toolchain for your build environment
  - set up the authentication to your cloud provider
- You can write your own actions, or you can find actions to use in the GitHub Marketplace

#### Runners

- A server that runs your workflows when they're triggered
  - a single job at a time
- GitHub provides Ubuntu Linux, Microsoft Windows, and macOS runners
- Each workflow run executes in a fresh, newly-provisioned virtual machine
- You can host your own runners

### Create an example workflow

- GitHub Actions uses YAML syntax to define the workflow
- Each workflow is stored as a separate YAML file in your code repository
  - in a directory named **`.github/workflows`**
- See [`workflows/learn-github-actions.yml`](workflows/learn-github-actions.yml)

### Viewing the activity for a workflow run

- When your workflow is triggered, a **workflow run** is created that executes the workflow
- You can see a visualization graph of the run's progress and view each step's activity

### Sources

- "Understanding GitHub Actions - GitHub Docs." _GitHub Docs_, 2022, [docs.github.com/en/actions/learn-github-actions/understanding-github-actions](https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions). Accessed 4 June 2022.

## Finding and customizing actions

- The actions you use in your workflow can be defined in:
  - the same repository as your workflow file
  - any public repository
  - a published Docker container image on Docker Hub
- [GitHub Marketplace](https://github.com/marketplace/actions/) is a central location for you to find actions created by the GitHub community

### Adding an action to your workflow

#### Adding an action from the same repository

- Reference the action with either the ‌`{owner}/{repo}@{ref}` or `./path/to/dir` syntax
- Example repository file structure:

```text
|-- hello-world (repository)
|   |__ .github
|       └── workflows
|           └── my-first-workflow.yml
|       └── actions
|           |__ hello-world-action
|               └── action.yml
```

- Example workflow file:

```yml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      # This step checks out a copy of your repository.
      - uses: actions/checkout@v3
      # This step references the directory that contains the action.
      - uses: ./.github/actions/hello-world-action
```

#### Adding an action from a different repository

- Reference the action with the `{owner}/{repo}@{ref}` syntax
  - must be stored in a public repository

```yml
jobs:
  my_first_job:
    steps:
      - name: My first step
        uses: actions/setup-node@v3
```

#### Referencing a container on Docker Hub

- Reference the action with the `docker://{image}:{tag}` syntax

```yml
jobs:
  my_first_job:
    steps:
      - name: My first step
        uses: docker://alpine:3.8
```

### Using release management for your custom actions

- Tags: `uses: actions/javascript-action@v1.0.1`
- SHAs: `uses: actions/javascript-action@172239021f7ba04fe7327647b213799853a9eb89`
- Branches: `uses: actions/javascript-action@main`

### Sources

- "Finding and Customizing Actions - GitHub Docs." _GitHub Docs_, 2022, [docs.github.com/en/actions/learn-github-actions/finding-and-customizing-actions](https://docs.github.com/en/actions/learn-github-actions/finding-and-customizing-actions). Accessed 5 June 2022.

## Essential features of GitHub Actions

### Using variables in your workflows

- GitHub Actions include [default environment variables](https://docs.github.com/en/actions/learn-github-actions/environment-variables#default-environment-variables) for each workflow run
- To use custom environment variables
  - set in your YAML workflow file
  - see [`.github/workflows/env-vars.yml`](.github/workflows/env-vars.yml)

### Adding scripts to your workflow

- You can use actions to run scripts and shell commands, which are then executed on the assigned runner
- See [`.github/workflows/script-in-workflow.yml`](.github/workflows/script-in-workflow.yml)
