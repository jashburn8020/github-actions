# GitHub Actions

## Understanding GitHub Actions

### Overview

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

## Sources
