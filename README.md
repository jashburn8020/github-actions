# GitHub Actions

- [GitHub Actions](#github-actions)
  - [Understanding GitHub Actions](#understanding-github-actions)
    - [The components of GitHub Actions](#the-components-of-github-actions)
      - [Workflows](#workflows)
      - [Events](#events)
      - [Jobs](#jobs)
      - [Actions](#actions)
      - [Runners](#runners)
    - [Create an example workflow](#create-an-example-workflow)
    - [Viewing the activity for a workflow run](#viewing-the-activity-for-a-workflow-run)
    - [Sources](#sources)
  - [Finding and customizing actions](#finding-and-customizing-actions)
    - [Adding an action to your workflow](#adding-an-action-to-your-workflow)
      - [Adding an action from the same repository](#adding-an-action-from-the-same-repository)
      - [Adding an action from a different repository](#adding-an-action-from-a-different-repository)
      - [Referencing a container on Docker Hub](#referencing-a-container-on-docker-hub)
    - [Using release management for your custom actions](#using-release-management-for-your-custom-actions)
    - [Sources](#sources-1)
  - [Essential features of GitHub Actions](#essential-features-of-github-actions)
    - [Using variables in your workflows](#using-variables-in-your-workflows)
    - [Adding scripts to your workflow](#adding-scripts-to-your-workflow)
    - [Sharing data between jobs](#sharing-data-between-jobs)
    - [Sources](#sources-2)
  - [About workflows](#about-workflows)
    - [Using starter workflows](#using-starter-workflows)
    - [Advanced workflow features](#advanced-workflow-features)
      - [Storing secrets](#storing-secrets)
    - [Sources](#sources-3)

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
- A workflow must contain the following basic components:
  - one or more **events** that will trigger the workflow
  - one or more **jobs**, each of which will execute on a runner machine and run a series of one or more steps
  - each **step** can either run a script that you define or run an action
- A repository can have multiple workflows
  - build and test pull requests
  - deploy your application every time a release is created
  - add a label every time someone opens a new issue
- You can reference a workflow within another workflow
- See [Workflow syntax for GitHub Actions](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions)

#### Events

- A specific activity in a repository that triggers a workflow run
- An activity can originate from GitHub when someone
  - creates a pull request
  - opens an issue
  - pushes a commit to a repository
- You can also trigger a workflow run
  - on a schedule
  - by posting to a REST API (triggers a [`repository_dispatch`](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#repository_dispatch) event)
  - manually
- See [Triggering a workflow](https://docs.github.com/en/actions/using-workflows/triggering-a-workflow) and [Events that trigger workflows](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows)

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
- "About Workflows - GitHub Docs." _GitHub Docs_, 2022, [docs.github.com/en/actions/using-workflows/about-workflows](https://docs.github.com/en/actions/using-workflows/about-workflows). Accessed 18 June 2022.

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

### Sharing data between jobs

- Store files in GitHub as _artifacts_
  - if your job generates files that you want to share with another job in the same workflow
  - if you want to save the files for later reference
- Artifacts: files created when you build and test your code
  - binary or package files, test results, screenshots, log files
- Artifacts are associated with the workflow run where they were created and can be used by another job
- All actions and workflows called within a run have write access to that run's artifacts
- You can use the [`upload-artifact` action](https://github.com/actions/upload-artifact) to upload artifacts
- The [`download-artifact` action](https://github.com/actions/download-artifact) can be used to download previously uploaded artifacts during a workflow run
- You can use the `upload-artifact` and `download-artifact` actions to share data between jobs in a workflow
  - to download an artifact from the same workflow run, your download job should specify `needs:` _`upload-job-name`_ so it doesn't start until the upload job finishes
- See [`.github/workflows/passing-data.yml`](.github/workflows/passing-data.yml)

### Sources

- "Essential Features of GitHub Actions - GitHub Docs." _GitHub Docs_, 2022, [docs.github.com/en/actions/learn-github-actions/essential-features-of-github-actions](https://docs.github.com/en/actions/learn-github-actions/essential-features-of-github-actions). Accessed 17 June 2022.
- "Storing Workflow Data as Artifacts - GitHub Docs." _GitHub Docs_, 2022, [docs.github.com/en/actions/using-workflows/storing-workflow-data-as-artifacts](https://docs.github.com/en/actions/using-workflows/storing-workflow-data-as-artifacts). Accessed 17 June 2022.

## About workflows

### Using starter workflows

- GitHub provides preconfigured starter workflow that you can customize to create your own continuous integration workflow
- GitHub analyzes your code and shows you CI starter workflow that might be useful for your repository
- See the [actions/starter-workflows](https://github.com/actions/starter-workflows) repository and [Creating starter workflows for your organization](https://docs.github.com/en/actions/using-workflows/creating-starter-workflows-for-your-organization)

### Advanced workflow features

#### Storing secrets

- If your workflows use sensitive data, such as passwords or certificates, you can save these in GitHub as _secrets_ and then use them in your workflows as environment variables
- Secrets are encrypted environment variables that you create in an organization, repository, or repository [environment](https://docs.github.com/en/actions/deployment/targeting-different-environments/using-environments-for-deployment)
- To create secrets for a repository:
  - repository > Settings > Secrets > Actions > New repository secret
- Secrets can also be created at the repository environment and organization levels
- To provide an action with a secret as an input or environment variable, you can use the [`secrets` context](https://docs.github.com/en/actions/learn-github-actions/contexts#secrets-context) to access secrets you've created in your repository
  - if a secret has not been set, the return value of an expression referencing the secret will be an empty string
- Note: GitHub automatically redacts secrets printed to the log, but you should avoid printing secrets to the log intentionally
- See [`.github/workflows/workflow-secret.yml`](.github/workflows/workflow-secret.yml)

#### Creating dependent jobs

- By default, the jobs in your workflow all run in parallel at the same time
- If you have a job that must only run after another job has completed, use the `needs` keyword to create this dependency
  - if one of the jobs fails, all dependent jobs are skipped
  - if you need the jobs to continue, use the `if` conditional statement

```yml
jobs:
  job1:
  job2:
    needs: job1
  job3:
    # Always run after job1 and job2 have completed, regardless of whether they were successful
    if: ${{ always() }}
    needs: [job1, job2]
```

### Using a matrix

- A matrix strategy lets you use variables in a single job definition to automatically create multiple job runs that are based the combinations of the variables
  - e.g., to test your code in multiple versions of a language or operating systems
  - created using the **`strategy`** keyword, which receives the build options as an array
- By default, GitHub will maximize the number of jobs run in parallel depending on runner availability
- The order of the variables in the matrix determines the order in which the jobs are created
  - unless you specify a maximum using [`max-parallel`](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#jobsjob_idstrategymax-parallel)
- The variables that you define become properties in the [`matrix` context](https://docs.github.com/en/actions/learn-github-actions/contexts#matrix-context)
- See [`.github/workflows/multi-dimension-matrix-strategy.yml`](.github/workflows/multi-dimension-matrix-strategy.yml)

### Sources

- "About Workflows - GitHub Docs." _GitHub Docs_, 2022, [docs.github.com/en/actions/using-workflows/about-workflows](https://docs.github.com/en/actions/using-workflows/about-workflows). Accessed 18 June 2022.
- "Encrypted Secrets - GitHub Docs." _GitHub Docs_, 2022, [docs.github.com/en/actions/security-guides/encrypted-secrets](https://docs.github.com/en/actions/security-guides/encrypted-secrets). Accessed 18 June 2022.
- "Using Jobs in a Workflow - GitHub Docs." _GitHub Docs_, 2022, [docs.github.com/en/actions/using-jobs/using-jobs-in-a-workflow](https://docs.github.com/en/actions/using-jobs/using-jobs-in-a-workflow). Accessed 19 June 2022.
- "Using a Matrix for Your Jobs - GitHub Docs." _GitHub Docs_, 2022, [docs.github.com/en/actions/using-jobs/using-a-matrix-for-your-jobs](https://docs.github.com/en/actions/using-jobs/using-a-matrix-for-your-jobs). Accessed 20 June 2022.
  ‌
